from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Group, User

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_experience_api_returns_experience_data(self):
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        experience = response.json()[0]
        self.assertEqual(experience["pk"], str(self.experience.id))
        self.assertEqual(experience["fields"]["title"], self.experience.title)
        self.assertEqual(experience["fields"]["description"], self.experience.description)
        self.assertEqual(experience["fields"]["category_display"], "Part-Time")
        self.assertTrue(experience["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()[0]["fields"]["is_ongoing"])
        self.assertIsNotNone(response.json()[0]["fields"]["ended_at"])

class ProjectTest(TestCase):
    # Create a sample Project object that will be used by the tests.
    def setUp(self):
        self.project = Project.objects.create(
            title="Website Portofolio",
            description="Website portofolio yang dibuat menggunakan framework Django",
            tech_stack = "Python, Django, HTML, CSS",
            image="https://example.com/image.png",
            project_url="https://github.com/",
            live_demo="",
        )

    # Test that the Project URL is accessible and uses the correct template.
    def test_project_url_is_accessible(self):
        response = self.client.get(reverse("main:show_projects"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")

    def test_project_edit_controls_are_available_to_editor_and_owner(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertContains(response, 'const IS_SUPERUSER = "false" === "true";')
        self.assertNotContains(response, 'id="add-project-button"')

        owner = User.objects.create_superuser(
            username="portfolio-owner", email="owner@example.com", password="test-password",
        )
        self.client.force_login(owner)
        response = self.client.get(reverse("main:show_projects"))
        self.assertContains(response, 'const IS_SUPERUSER = "true" === "true";')
        self.assertContains(response, 'id="add-project-button"')
        self.assertContains(response, "const edit = (IS_SUPERUSER || IS_EDITOR)")

        editor = User.objects.create_user(username="project-editor", password="test-password")
        editor.groups.add(Group.objects.create(name="Editor"))
        self.client.force_login(editor)
        response = self.client.get(reverse("main:show_projects"))
        self.assertContains(response, 'const IS_EDITOR = "true" === "true";')
        self.assertContains(response, 'id="add-project-modal"')
        self.assertNotContains(response, 'id="add-project-button"')

    # Test that the Project model's string representation returns its title.
    def test_project_model(self):
        self.assertEqual(str(self.project), "Website Portofolio")

    # Project data is fetched by JavaScript from the API after the page renders.
    def test_project_page(self):
        response = self.client.get(reverse("main:show_projects"))
    
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, reverse("api:project-list"))
        self.assertContains(response, 'article.className = \'project-card\'')
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_project_api_returns_project_data(self):
        response = self.client.get(reverse("api:project-list"))

        self.assertEqual(response.status_code, 200)
        project = response.json()[0]
        self.assertEqual(project["id"], str(self.project.id))
        self.assertEqual(project["title"], self.project.title)
        self.assertEqual(project["description"], self.project.description)
        self.assertEqual(project["image"], self.project.image)
        self.assertEqual(project["star_count"], 0)
        self.assertFalse(project["is_starred"])

    def test_project_api_filters_by_title(self):
        response = self.client.get(reverse("api:project-list"), {"title": "Website"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual([project["id"] for project in response.json()], [str(self.project.id)])

    def test_empty_project_api_returns_empty_list(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("api:project-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
