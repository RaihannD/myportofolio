import uuid

from django.conf import settings
from django.db import migrations, models


def copy_project_stars_to_backup(apps, schema_editor):
    through = apps.get_model("main", "Project")._meta.get_field("starred_by").remote_field.through
    backup = apps.get_model("main", "ProjectStarredByBackup")
    source = through._meta.db_table
    quote = schema_editor.quote_name
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            f"SELECT project_id, {quote(through._meta.get_field('user').column)} "
            f"FROM {quote(source)}"
        )
        rows = cursor.fetchall()
    backup.objects.bulk_create(
        [backup(old_project_id=project_id, user_id=user_id) for project_id, user_id in rows]
    )


def restore_project_stars(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    through = Project._meta.get_field("starred_by").remote_field.through
    backup = apps.get_model("main", "ProjectStarredByBackup")
    project_ids = {
        row.old_project_id: row.uuid_project_id
        for row in backup.objects.filter(user_id__isnull=True)
    }
    through.objects.bulk_create(
        [
            through(project_id=project_ids[row.old_project_id], user_id=row.user_id)
            for row in backup.objects.filter(user_id__isnull=False)
            if row.old_project_id in project_ids
        ]
    )


def map_old_project_ids(apps, schema_editor):
    # Retain the old integer IDs alongside each UUID while replacing the key.
    Project = apps.get_model("main", "Project")
    backup = apps.get_model("main", "ProjectStarredByBackup")
    # The backup table also stores a mapping for projects without any stars.
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, uuid_id FROM {schema_editor.quote_name(Project._meta.db_table)}"
        )
        project_map = cursor.fetchall()
    backup.objects.bulk_create(
        [
            backup(old_project_id=old_id, uuid_project_id=new_id)
            for old_id, new_id in project_map
        ]
    )


def assign_project_uuids(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    for project in Project.objects.filter(uuid_id__isnull=True).iterator():
        Project.objects.filter(pk=project.pk).update(uuid_id=uuid.uuid4())


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_project_starred_by"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="uuid_id",
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.RunPython(assign_project_uuids, noop),
        migrations.CreateModel(
            name="ProjectStarredByBackup",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("old_project_id", models.BigIntegerField()),
                ("uuid_project_id", models.UUIDField(null=True)),
                ("user_id", models.BigIntegerField(null=True)),
            ],
        ),
        migrations.RunPython(copy_project_stars_to_backup, noop),
        migrations.RunPython(map_old_project_ids, noop),
        migrations.RemoveField(model_name="project", name="starred_by"),
        migrations.RemoveField(model_name="project", name="id"),
        migrations.RenameField(model_name="project", old_name="uuid_id", new_name="id"),
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="project",
            name="starred_by",
            field=models.ManyToManyField(blank=True, related_name="starred_projects", to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(restore_project_stars, noop),
        migrations.DeleteModel(name="ProjectStarredByBackup"),
    ]
