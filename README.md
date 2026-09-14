# Website Portofolio

## Deskripsi Proyek

Proyek ini merupakan *website* portofolio personal yang dikembangkan sebagai bagian dari mata kuliah Pemograman Berbasis Platform (PBP). *Website* ini menyajikan informasi dasar mengenai diri saya, riwayat pendidikan, kemampuan, serta informasi relevan lainnya.

Proyek ini menggunakan Django sebagai framework web dengan menerapkan konsep Model-View-Template (MVT). Website dikembangkan menggunakan HTML dan CSS, dengan data portofolio yang disimpan dan dikelola melalui model Django. Implementasi saat ini berfokus pada pembuatan website portofolio yang rapi dan responsif serta menerapkan konsep-konsep HTML5, CSS3, dan Django yang dipelajari selama sesi tutorial dan perkuliahan.

## Struktur Proyek
```text
myportofolio/
├── portofolio/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
├── media/
│   └── projects/
├── manage.py
├── requirements.txt
└── README.md
...
```
## Setup

### 1. Kloning Repositori

```bash
git clone <repository-url>
cd myportofolio
```

### 2. Membuat dan Mengaktifkan Virtual Enviroment

Windows:

Jika menggunakan Command Prompt
```cmd
python -m venv env
env\Scripts\activate
```
Jika menggunakan Git Bash
```bash
python -m venv env
source env/Scripts/activate
```

### 3. Mengunduh Dependensi

```bash
pip install -r requirements.txt
```

### 4. Migrasi Django

```bash
python manage.py migrate
```

### 5. Jalankan Development Server

```bash
python manage.py runserver
```

Website tersebut kemudian dapat diakses melalui *local development server*.

## Weekly Progress

### Tutorial 01

* Membuat struktur awal *website* portofolio.
* Mengimplementasikan struktur HTML dasar dan *styling*.
* Membuat tata letak responsif awal.
* Menambahkan informasi pribadi.

### Tugas 01

* Menambahkan bagian *Skills* dengan kartu *skill* yang dapat digunakan kembali.
* Menambahkan efek *hover* menggunakan CSS.
* Menambahkan bagian *Education*.
* Melanjutkan penyempurnaan responsivitas untuk layar yang lebih kecil.
* Mengelola pengembangan menggunakan *feature branch* dan pesan *commit* Git yang deskriptif.
* Membuat dokumentasi detail untuk *website* portofolio

### Toturial 02
* Membuat aplikasi Django beserta konfigurasi model
* Mengimplementasi model dasar
* Menghubungkan *view* dengan template
* Mengonfigurasi *routing URL*
* Menerapkan unit *testing*

### Tugas 02
* Menambahkan model *project* untuk menyimpan data proyek
* Menambahkan halaman proyek yang menampilkan data proyek
* Menambahkan fitur *upload* gambar dan link untuk setiap proyek
* Menambahkan *unit tests* untuk halaman dan model *Project*
* Menambahkan dokumentasi dan refleksi terkait implementasi *Project*

## Pertanyaan Reflektif

## Tugas 1

### 1. Penggunaan Elemen Semantik HTML5

Ya, saya menggunakan elemen semantik HTML5 seperti `<section>` untuk mengatur berbagai bagian portofolio. Sebagai contoh, bagian kemampuan (Skills) dan Pendidikan (Education) direpresentasikan menggunakan elemen `<section>` yang terpisah.

Elemen semantik membantu saya menyusun struktur *website* statis berdasarkan maksud setiap bagian, daripada memperlakukan seluruh halaman sebagai sekumpulan elemen `<div>` biasa. Hal ini membuat kode HTML lebih mudah dibaca dan dipelihara karena strukturnya sendiri menunjukkan fungsi atau makna dari setiap bagian halaman tersebut. 

Untuk portofolio statis, hal ini sangat bermanfaat karena *website* tersebut terdiri dari beberapa bagian berbeda yang ditampilkan pada halaman yang sama. Penggunaan `<section>` mempermudah pemisahan bagian-bagian tersebut sekaligus menjaga struktur HTML tetap sederhana dan mudah dimengerti. Selain itu, hal ini memberikan landasan yang lebih baik untuk membantu pengembangan *website* di kemudian hari. Saya tidak menggunakan setiap jenis elemen semantik yang tersedia, seperti `<article>` atau `<aside>`, karena konten portofolio saya saat ini tidak memerlukan artikel ataupun konten tambahan di bagian samping.

### 2. Tantangan pengaturan CSS responsif

Salah satu tantangan utama yang saya hadapi adalah mempertahankan tata letak saat lebar layar berkurang. Versi desktop memiliki ruang horizontal yang cukup untuk menempatkan elemen secara berdampingan, namun tata letak yang sama bisa terasa terlalu padat di layar ponsel.

Sebagai contoh, pada bagian *Skills*, saya menggunakan *Flexbox* dengan *flex-wrap* agar kartu-kartu *skills* dapat berpindah ke baris berikutnya saat ruang horizontal tidak mencukupi. Hal ini memungkinkan kartu-kartu tersebut mempertahankan ukurannya tanpa harus menjadi terlalu kecil. Pada bagian *Education*, saya menggunakan tata letak *flex* horizontal untuk layar yang lebih besar dan mengubahnya menjadi tata letak vertikal untuk layar yang lebih kecil, sehingga informasi riwayat pendidikan tetap mudah dibaca dan memiliki ruang yang memadai.

### 3. Batasan Website Statis

Salah satu keterbatasan yang saya temui pada portofolio statis saya saat ini adalah perlunya menambahkan dan memperbarui informasi secara manual di dalam kode HTML. Hal ini masih bisa ditangani selama portofolio hanya memuat beberapa bagian, namun bisa merepotkan seiring bertambahnya informasi baru, seperti proyek, keterampilan, atau pencapaian baru. Sebagai contoh, penambahan beberapa proyek baru akan mengharuskan saya membuat setiap entri proyek secara manual di dalam HTML. Keterbatasan lainnya adalah *website* tersebut tidak memiliki cara untuk memproses atau menyimpan masukan pengguna. Hal ini berarti fitur seperti *contact form* tidak dapat menyimpan atau memproses pesan tanpa adanya *backend*.

Untuk iterasi berikutnya, saya ingin membuat bagian proyek menjadi dinamis dengan menyimpan informasi proyek di dalam basis data dan menampilkannya menggunakan Django. Hal ini akan memungkinkan saya untuk menambah atau memperbarui proyek tanpa harus mengubah struktur HTML setiap kali ada perubahan. Saya juga ingin menambahkan formulir kontak yang dapat memproses pesan melalui *backend* Django.

## Tugas 2
### 1. Alur yang Terjadi Ketika Pengguna Membuka Halaman Portofolio Baru

Ketika pengguna membuka halaman portofolio yang baru, permintaan pertama kali masuk ke `urls.py` proyek. `urls.py` proyek kemudian menggunakan `include()` untuk mengarahkan permintaan ke *URL configuration* aplikasi `main`. `urls.py` aplikasi kemudian mencocokkan URL yang diminta, misalnya `project/`, dengan fungsi *view* `show_project`. 

Fungsi *view* `show_project` mengambil data proyek dari model `Project` menggunakan `Project.objects.all()`. Data yang diperoleh kemudian ditempatkan di dalam *dictionary* *context* dan diteruskan ke template `project.html` menggunakan fungsi `render()` milik Django.

Template ini menggunakan Django Template Language untuk melakukan perulangan pada data proyek serta menampilkan judul, deskripsi, gambar, dan tautan untuk setiap proyek. Terakhir, Django menghasilkan halaman HTML dan mengirimkannya kembali ke browser, tempat pengguna dapat melihat proyek-proyek tersebut.

### 2. Mengapa Data Bagian Portofolio Baru Sebaiknya Disimpan pada Model

Menyimpan data portofolio dalam sebuah model membuat aplikasi lebih mudah dipelihara dan dikembangkan. Daripada mengubah HTML secara manual setiap kali ingin menambah, menghapus, atau memperbarui proyek, saya cukup mengubah data yang tersimpan di dalam basis data.

Contohnya, jika saya ingin menambahkan proyek lain, saya hanya perlu membuat objek `Project` baru. Template yang sama dapat menampilkannya secara otomatis karena template tersebut melakukan perulangan pada objek-objek proyek yang diambil oleh *view*. Hal ini membuat aplikasi lebih mudah dikembangkan. Seiring bertambahnya jumlah proyek, saya tidak perlu membuat elemen HTML baru secara manual untuk setiap proyek. Template dan tampilan dapat tetap hampir sama, sementara basis data menyimpan data portofolio yang sesungguhnya.

### 3. Perbedaan `makemigrations` dan `migrate` dalam Django dan Contoh Model

`makemigrations` dan `migrate` memiliki tujuan yang berbeda. `makemigrations` mendeteksi perubahan pada model Django dan membuat file migrasi yang mendeskripsikan perubahan tersebut. Perintah ini tidak mengubah basis data secara langsung. `migrate` mengambil file-file migrasi tersebut dan menerapkannya pada basis data, sehingga membuat atau memodifikasi tabel dan kolom basis data yang bersangkutan.

Contohnya, ketika saya membuat model `Project` dengan field seperti `title`, `description`, `image`, dan `project_url`, pertama-tama saya menjalankan perintah berikut:

```bash
python manage.py makemigrations
```

Hal ini membuat file migrasi yang mendeskripsikan tabel `Project` yang baru. Kemudian :

```bash
python manage.py migrate
```

Menerapkan migrasi tersebut dan membuat tabel yang sesuai di dalam basis data.

## AI Disclosure

Saya menggunakan AI pada pengembangan proyek ini sebagai sumber pendukung dalam pengembangan proyek, model yang saya gunakan adalah ChatGPT GPT-5.6 Luna.

Saya menggunakan AI saat menghadapi konsep atau implementasi yang belum saya pahami sepenuhnya. Sebagai contoh, saya memanfaatkannya untuk memperjelas alur kerja *branching* dan *merging* di Git, memahami tata letak CSS, seperti *Flexbox* atau *grid*, serta membantu dalam perancangan instruksi setup.

Perancangan tata letak *website*, implementasi, pengujian, dan pengambilan keputusan akhir tetap saya lakukan sendiri. Saya tidak mengandalkan AI untuk mengerjakan keseluruhan proyek. Saat menggunakan saran dari AI, saya meninjau dan menguji kode atau informasi yang diberikan sebelum memutuskan untuk mengimplementasi kode atau saran yang saya terima.

Salah satu keterbatasan yang saya temui saat menggunakan AI adalah sarannya tidak selalu dapat diterapkan secara langsung pada proyek saya. Terkadang beberapa saran yang diberikan lebih rumit daripada yang sebenarnya diperlukan. Oleh karena itu, saya harus memverifikasi sendiri saran-saran tersebut, menguji kodenya, serta terkadang menyederhanakan atau memodifikasi solusi yang diusulkan. Hal ini sangat penting terutama saat bekerja dengan Git atau *troubleshooting* Git, karena menjalankan perintah yang salah dapat mengubah struktur repositori.

### AI Prompting Strategy

Prompt saya mendeskripsikan masalah spesifik yang sedang saya hadapi dengan disertai bagian kode yang relevan atau output di server lokal jika diperlukan. Saya kemudian menggunakan penjelasan yang diberikan untuk memahami konsepnya sebelum memutuskan untuk menggunakan solusi yang diberikan oleh AI.

Untuk pertanyaan seputar pemograman saya biasanya meminta penjelasan mengapa hal tersebut dapat terjadi daripada langsung meminta solusi sudah jadi. Ini membantu saya memahami konsep serta memecahkan masalah CSS, tata letak responsif, serta branching daripada sekadar menyalin kode.

### AI Chat / Prompting Log

AI chat / Prompting Log disediakan dalam bentuk docs :
https://docs.google.com/document/d/1UfjLTFVKztRLaLuK6iaB9szSkNGfCZNJHBG6W8Jvv04/edit?usp=sharing

## Catatan Tambahan

Nama : Raihan Daffa Aprilianda

NPM : 2506620021

Kelas : PBP B