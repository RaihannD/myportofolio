# Website Portofolio

## Deskripsi Proyek

Proyek ini merupakan *website* portofolio personal yang dikembangkan sebagai bagian dari mata kuliah Pemograman Berbasis Platform (PBP). *Website* ini menyajikan informasi dasar mengenai diri saya, riwayat pendidikan, kemampuan, serta informasi relevan lainnya.

Proyek ini menggunakan Django sebagai framework web dengan menerapkan konsep Model-View-Template (MVT). Website dikembangkan menggunakan HTML dan CSS, dengan data portofolio yang disimpan dan dikelola melalui model Django. Implementasi saat ini berfokus pada penerapan operasi *CRUD (Create, Read, Update, Delete)*, menerapkan autentikasi dan otorisasi, AJAX/JavaScript, perlindungan XSS, serta melanjutkan pembuatan website portofolio yang rapi dan responsif serta menerapkan konsep-konsep HTML5, CSS3, dan Django yang dipelajari selama sesi tutorial dan perkuliahan.

## Struktur Proyek
```text
myportofolio/
├── main/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_project.py
│   │   ├── 0003_project_tech_stack_alter_project_image_and_more.py
│   │   ├── 0004_project_starred_by.py
│   │   ├── 0005_project_uuid.py
│   │   └── 0006_experience_starred_by.py
│   ├── admin.py
│   ├── apps.py
│   ├── api_urls.py
│   ├── api_views.py
│   ├── forms.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── tests_api.py
│   ├── urls.py
│   └── views.py
├── portofolio/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── __init__.py
├── templates/
│   ├── components/
│   │   ├── experience_delete_modal.html
│   │   ├── experience_form_modal.html
│   │   ├── project_delete_modal.html
│   │   ├── project_form_modal.html
│   │   ├── project_star.html
│   │   └── toast.html
│   ├── base.html
│   ├── experience.html
│   ├── experience_form.html
│   ├── index.html
│   ├── login.html
│   ├── project.html
│   ├── projects_form.html
│   └── register.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   ├── CSS3.png
│   │   ├── github.png
│   │   ├── HTML5.png
│   │   ├── java.png
│   │   ├── Python.svg
│   │   └── raihan.jpeg
│   └── js/
│       └── toast.js
├── manage.py
├── requirements.txt
└── README.md
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

### Tutorial 03

* Mengimplementasi `base.html` sebagai template dasar
* Me-*refactor* berkas `project.html` agar melakukan extend dari `base.html`
* Menambahkan `ModelForm` untuk mengelola data *project*.
* Menambahkan fitur *Create, Read, * dan *Delete* untuk *experience*.
* Mengimplementasi data delivery dengan JSON

### Tugas 03

* Me-*refactor* setiap berkas html yang identik dengan melakukan extend dari `base.html`
* Menambahkan `ModelForm` untuk mengelola data *experience*.
* Mengimplementasikan fitur *Create, Read, Update,* dan *Delete* untuk *experience*.
* Menambahkan *search* berdasarkan nama pengalaman.
* Menambahkan *JSON endpoint* serta proses *serialization* dan *deserialization* data.
* Menambahkan halaman dan komponen *form* untuk menambah dan mengubah pengalaman.
* Menambahkan *delete confirmation modal* untuk menghapus pengalaman.

### Tutorial 04
* Mengimplementasi autentikasi (daftar, login, logout)
* Menampilkan status login di navbar
* Menerapkan session dan cookies
* Mengatur hak akses pengguna

### Tugas 04
* Menerapkan peran Editor melalui Django Group atau Permission.
* Menerapkan pembatasan hak akses di sisi server (server-side check).
* Menyembunyikan tombol/kontrol aksi (create, update, delete) pada template bagi pengguna yang tidak berhak.
* Mengimplementasikan view `toggle_star` (POST & `{% csrf_token %}`) untuk memberi/membatalkan star (maksimal satu star per pengguna) serta menampilkan jumlah total star dan status pengguna.
* Memastikan endpoint JSON dari Tugas 3 tetap berfungsi tanpa membocorkan informasi sensitif.
* Menambahkan relasi `ManyToManyField` ke model User

### Tutorial 05
* Mengimplementasi notifikasi Toast
* Menampilkan data proyek dengan AJAX
* Menerapkan *search Debouncing* pada pencarian proyek
* Membuat modal sebagai form untuk menambahkan proyek
* Menambahkan data proyek dengan AJAX
* Melindungi aplikasi dari XSS

### Tugas 05
* Menampilkan data pengalaman dengan AJAX
* Menerapkan *search Debouncing* pada pencarian pengalaman
* Menambahkan data pengalaman dengan Modal dan AJAX
* Menerapkan notifikasi toast
* Melindungi aplikasi dari XSS

### Tutorial 07
* Mengimplementasi *serializer* untuk *projects*
* Mengimplementasi API daftar dan tambah
* Mengimplementasi API detail, update, delete
* Mengimpelemtasi API star untuk *projects*
* Mengintegrasi API dengan AJAX

### Tugas 06

* Menambahkan `ExperienceSerializer` dengan daftar field eksplisit, validasi teks, serta informasi jumlah dan status *star*.
* Menambahkan relasi *star* pada model `Experience` beserta migrasinya.
* Membuat API Experience untuk daftar, pencarian, tambah, detail, edit, hapus, dan *star* di bawah prefix `/api/v1/`.
* Menerapkan hak akses API Experience untuk pengunjung, pengguna biasa, Editor, dan pemilik portofolio.
* Mengintegrasikan API dengan AJAX
* Mengimplementasi *permission class* untuk otorisasi
* Menambahkan pengujian API Experience untuk hak akses, validasi, *star*, data yang tidak ditemukan, dan CSRF.
* Mengizinkan Editor mengubah data *projects* melalui API dan modal pada halaman Projects, sementara pembuatan dan penghapusan tetap khusus pemilik portofolio.

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

## Tugas 3
### 1. Mengapa menggunakan `ModelForm` dan mengapa perlu `{% csrf_token %}`

`ModelForm` digunakan karena dapat membuat form berdasarkan model Django yang sudah dibuat. Dengan `ModelForm`, kita tidak perlu mendefinisikan setiap field dan proses validasinya secara manual di HTML. Django juga dapat melakukan validasi data dan menyimpan data yang sudah valid langsung ke database menggunakan `form.save()`. Hal ini membuat kode menjadi lebih singkat dan mengurangi kemungkinan adanya kesalahan saat membuat form secara manual.

`{% csrf_token %}` digunakan untuk melindungi form dari serangan **Cross-Site Request Forgery (CSRF)**. Token ini memastikan bahwa request `POST` yang dikirim berasal dari form yang dibuat oleh aplikasi kita, bukan dari situs lain yang mencoba melakukan request atas nama pengguna. Django akan memeriksa token tersebut sebelum memproses request.

### 2. Mengapa JSON lebih disukai dibandingkan XML dalam pengembangan web modern?

JSON lebih banyak digunakan karena memiliki struktur yang sederhana dan lebih ringkas dibandingkan XML. JSON juga menggunakan format yang mirip dengan struktur data yang umum digunakan dalam JavaScript, seperti object dan array, sehingga lebih mudah digunakan dalam aplikasi web.

Selain itu, JSON biasanya menghasilkan data yang lebih kecil karena tidak membutuhkan banyak tag pembuka dan penutup seperti XML. JSON juga mudah dibaca oleh manusia dan mudah diproses oleh berbagai bahasa pemrograman. Oleh karena itu, JSON sering digunakan untuk pertukaran data antara frontend dan backend melalui API.

### 3. Bagaimana alur view mengembalikan data portofolio dalam bentuk JSON dan mengapa perlu serialization?

Ketika endpoint JSON pada view diakses, view terlebih dahulu mengambil data `Experience` dari database menggunakan Django ORM. Data tersebut kemudian dapat difilter berdasarkan parameter yang diberikan oleh pengguna, misalnya `title`.

Setelah mendapatkan queryset, data tersebut diubah menjadi format JSON menggunakan fungsi `serializers.serialize()`. Hasil JSON kemudian dikembalikan menggunakan `HttpResponse` dengan `content_type="application/json"`.

Serialization diperlukan karena objek model Django atau queryset yang diambil dari database tidak secara langsung berbentuk JSON. JSON hanya dapat merepresentasikan data dalam bentuk seperti object, array, string, angka, dan boolean. Dengan melakukan serialization, data model Django diubah menjadi format yang dapat dikirim melalui HTTP dan digunakan oleh aplikasi lain atau frontend.

## Tugas 5
### 1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

Debouncing adalah pengaturan yang menunda eksekusi suatu fungsi hingga pengguna berhenti melakukan tindakan selama jangka waktu tertentu. Dalam fitur pencarian berbasis AJAX, hal ini berarti permintaan pencarian baru dikirim setelah pengguna berhenti mengetik selama jeda waktu singkat. Hal ini penting karena tanpa debouncing, setiap penekanan tombol dapat memicu permintaan AJAX baru. Sebagai contoh, mengetik kata "Python" bisa saja mengirimkan enam permintaan terpisah. Debouncing mengurangi permintaan yang tidak perlu, menurunkan beban kerja server, serta menjadikan fitur pencarian lebih efisien.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`await` digunakan untuk menunggu selesainya sebuah Promise sebelum melanjutkan ke baris kode berikutnya. Karena `fetch()` mengembalikan sebuah Promise, penggunaan `await fetch()` memungkinkan kita menunggu hingga server memberikan respons sebelum memproses respons tersebut.

Jika kita tidak menggunakan `await`, eksekusi kode akan langsung berlanjut sementara permintaan masih diproses. Akibatnya, kita akan mendapatkan Promise, bukan data respons yang sebenarnya, ini berarti kita tidak dapat mengakses data respons atau JSON secara langsung sebagaimana mestinya. Kita harus menangani Promise tersebut menggunakan `.then()` atau pendekatan asinkron lainnya.

### 3. Jelaskan apa itu serangan XSS dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

XSS, atau *Cross-Site Scripting*, adalah serangan keamanan di mana penyerang menyisipkan kode JavaScript atau HTML berbahaya ke dalam data yang nantinya ditampilkan kepada pengguna lain. Jika aplikasi menyisipkan data ini ke dalam halaman sebagai HTML tanpa melakukan *escaping* dengan benar, browser dapat menafsirkan kode berbahaya tersebut dan mengeksekusinya. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan karena JavaScript sering kali membuat elemen HTML secara dinamis menggunakan nilai yang diterima dari server. Jika nilai-nilai tersebut disisipkan langsung ke dalam HTML tanpa melakukan *escaping* terlebih dahulu, konten yang dikendalikan pengguna dapat berubah menjadi HTML atau JavaScript yang dapat dieksekusi. Template Django memberikan perlindungan dengan melakukan *escaping* otomatis pada variabel saat dirender secara normal.

## Tugas 6

### 1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan `PUT` dan `PATCH` beserta contoh kapan masing-masing sebaiknya digunakan!

REST (*Representational State Transfer*) adalah gaya arsitektur untuk merancang komunikasi antara sistem melalui resource. Dalam API REST, resource dikenali melalui URL, lalu diakses atau diubah menggunakan metode HTTP seperti `GET`, `POST`, `PUT`, `PATCH`, dan `DELETE`. Mengembalikan JSON saja belum membuat API menjadi RESTful karena JSON hanya format representasi data. API juga perlu menggunakan resource dan metode HTTP dengan makna yang sesuai, mengembalikan status HTTP yang tepat, serta menjaga komunikasi tetap stateless.

`PUT` digunakan untuk mengganti representasi resource dengan data yang dikirim, sehingga klien biasanya mengirim semua field yang diwajibkan. Contohnya, memperbarui seluruh informasi proyek melalui `PUT /api/v1/projects/<id>/`. `PATCH` digunakan untuk memperbarui sebagian field saja, misalnya hanya mengubah judul proyek dengan `PATCH` ke URL yang sama.

### 2. Jelaskan peran *serializer* pada Django REST Framework! Apa keuntungannya dibandingkan merakit *dictionary* secara manual dengan `JsonResponse` seperti pada Tutorial 05?

*Serializer* pada Django REST Framework mengubah objek model atau queryset menjadi representasi data yang dapat dikirim melalui API, misalnya JSON. Serializer juga mengubah input dari request menjadi nilai Python yang dapat digunakan untuk membuat atau memperbarui model, sekaligus memvalidasi input sebelum data disimpan.

Dibandingkan merakit *dictionary* secara manual dengan `JsonResponse` seperti pada Tutorial 05, `ModelSerializer` mengurangi kode berulang karena field dapat dipetakan dari model. Serializer menyediakan validasi yang konsisten dan mendukung proses pembuatan serta pembaruan data. Kita juga dapat menentukan field yang boleh ditampilkan atau diubah sehingga data sensitif tidak ikut terekspos.

### 3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan *permission class* di server, bukan hanya dengan menyembunyikan tombol di *template*?

Autentikasi memeriksa identitas pengguna, misalnya memastikan pengguna sudah masuk menggunakan sesi. Otorisasi menentukan tindakan apa yang boleh dilakukan oleh pengguna tersebut. Di DRF, autentikasi dijalankan oleh *authentication class*, sedangkan hak tindakan diperiksa dengan *permission class*.

Pemeriksaan izin harus dilakukan di server karena pengguna dapat memanggil endpoint secara langsung tanpa menggunakan halaman atau tombol yang disediakan aplikasi. Menyembunyikan tombol pada template hanya mengatur tampilan, hal itu tidak mencegah request langsung ke API. *Permission class* memastikan setiap request tetap diperiksa berdasarkan peran pengguna.

### 4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai `SessionAuthentication`! Mengapa *test* yang memakai `force_authenticate` tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

`SessionAuthentication` menggunakan cookie sesi yang otomatis dikirim browser. Karena browser dapat mengirim cookie tersebut tanpa tindakan eksplisit pengguna, situs lain berpotensi mencoba mengirim request atas nama pengguna yang sedang masuk. Token CSRF membantu memastikan bahwa request yang mengubah data berasal dari halaman aplikasi yang benar. Karena itu, request seperti `POST`, `PUT`, `PATCH`, dan `DELETE` perlu menyertakan token CSRF yang valid.

`force_authenticate` langsung menetapkan pengguna pada request pengujian, sehingga melewati proses login dan pemeriksaan CSRF yang terjadi pada autentikasi sesi. Maka, test dengan `force_authenticate` dapat menguji permission, tetapi tidak membuktikan perlindungan CSRF berjalan. Untuk menguji CSRF, gunakan `APIClient(enforce_csrf_checks=True)`, lakukan login dengan `.login()`, lalu periksa bahwa request tanpa token ditolak.

## AI Disclosure

Saya menggunakan AI pada pengembangan proyek ini sebagai sumber pendukung dalam pengembangan proyek, model yang saya gunakan adalah ChatGPT GPT-5.6 Luna.

Saya menggunakan AI saat menghadapi konsep atau implementasi yang belum saya pahami sepenuhnya. Sebagai contoh, saya memanfaatkannya untuk memperjelas alur kerja *branching* dan *merging* di Git, memahami tata letak CSS, seperti *Flexbox* atau *grid*, serta membantu dalam perancangan instruksi setup.

Perancangan tata letak *website*, implementasi, pengujian, dan pengambilan keputusan akhir tetap saya lakukan sendiri. Saya tidak mengandalkan AI untuk mengerjakan keseluruhan proyek. Saat menggunakan saran dari AI, saya meninjau dan menguji kode atau informasi yang diberikan sebelum memutuskan untuk mengimplementasi kode atau saran yang saya terima.

Pada Tugas 3, saya juga menggunakan AI untuk membantu memahami implementasi `ModelForm`, alur *Create, Read, Update,* dan *Delete* pada fitur *Experience*, serta proses *serialization* dan *deserialization* data JSON. Saya memberikan kode yang sedang saya kerjakan kepada AI dan meminta penjelasan atau bantuan *debugging* berdasarkan struktur proyek yang sudah saya buat, bukan meminta AI untuk membuat keseluruhan fitur dari awal.

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
