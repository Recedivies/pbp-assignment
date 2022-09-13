<div align="center" style="padding-bottom: 10px">
<h1>Tugas 2 PBP</h1>
</div>

## _Deployment_

Repositori ini telah di-_deploy_ ke Heroku. Anda dapat mengunjungi [di sini](https://pbp-tugas2-recedivies.herokuapp.com/).

## Cara Kerja Django

![image](https://user-images.githubusercontent.com/71712404/189476605-b5224948-3b07-4c1d-a563-6196f4d7b150.jpg)

> Bagan di atas menunjukkan tampilan dari arsitektur webapp. Django merupakan _framework_ yang berstruktur MVT (Model-View-Template). Alur dari diagram tersebut dan kaitannya pada file-file yang terdapat di django app adalah sebagai berikut.

Pertama, _client_ memberikan _request_ ke server Django. Setiap _request_ dari _client_ akan diproses pertama kali oleh Routing (**urls.py**) untuk menentukan View yang akan dieksekusi. Berikutnya, fungsi yang ada di View (**views.py**) akan melakukan pemrosesan _request_ dari _client_. Apabila dalam pemrosesan memerlukan pemanggilan _database_, maka di dalam View akan melakukan _query_ ke Model (**models.py**), kemudian _database_ akan mengembalikan hasil _query_ ke View. Setelah _request_ sudah diproses, hasil proses tersebut akan dipetakan ke dalam _template_ HTML (berkas **html**) yang akan menampilkan data-data dan halaman web ke _client_ sebagai _response_ dari server Django.

## Apakah kita dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?

_virtual environment_ digunakan untuk mengelola _package_ untuk berbagai proyek. Dengan menggunakan _virtual environment_, kita dapat membuat _environment_ terisolasi dimana _package_ dan versi yang diinstall hanya berlaku di folder/proyek tertentu tanpa mempengaruhi proyek lainnya. Oleh karena itu, sangat dianjurkan menggunakan _virtual environment_ untuk setiap proyek Django untuk menghindari tumpang tindih pada versi _package_ yang digunakan.

Walaupun demikian, kita dapat membuat aplikasi Django tanpa menggunakan _virtual environment_. Versi dan _package_ yang kita install, nantinya akan diinstall secara global. Dengan kata lain, jika kita tidak menggunakan _virtual environment_, kita dapat menjalankan aplikasi Django dengan versi global _package_.

## Cara implementasi pada tugas ini

Mengimplementasikan konsep MVT (Model-View-Template) pada folder ini (**katalog**):

1. Membuat sebuah fungsi pada file `views.py`

   Pertama, buat sebuah fungsi index dengan parameter _request_. Karena di dalam folder **templates** terdapat berkas HTML, artinya kita perlu memetakan hasil _request_ _client_ ke dalam _template_ HTML untuk menampilkan data.

   Pada tugas ini, kita perlu menampilkan data `nama`, `student_id`, dan `catalog_items`. Untuk me _render_ _response_ terdapat fungsi bawaan Django yaitu: `render`. Menambahkan kode seperti berikut:

   ```
   return render(request=request, template_name="katalog.html", context=context)
   ```

   kita perlu memberikan 3 parameter untuk keperluan ini, yaitu: parameter pertama adalah _request_ diisi dengan _request_ yang didapat dari argumen fungsi yang sudah dibuat, parameter kedua adalah _template_name_ diisi dengan nama berkas HTML yang ingin digunakan yaitu `katalog.html`, dan parameter terakhir adalah _context_ diisi dengan _dictionary_ yang menyimpan `nama`, `student_id`, dan `catalog_items`. Dikarenakan kita perlu melakukan _query_ ke _database_, maka value dari key `catalog items` diambil dari hasil _query_ pada models.

2. Membuat routing pada file `urls.py`

   Pertama, konfigurasi file tersebut di folder `project_django` untuk menambahkan semua url dari `urls.py` pada direktori app **katalog** ke `urls.py` di direktori utama (**project_django**) dengan menambahkan kode seperti berikut:

   ```
   path("katalog/", include('katalog.urls'))
   ```

   artinya menambahkan semua `urls.py` yang ada di app **katalog** dimana url nya diawali dengan `katalog/`.

   Selanjutnya membuat file `urls.py` untuk memetakan fungsi yang telah dibuat pada langkah sebelumnya di direktori app **katalog**. Membuat urlpatterns yang berisi:

   ```
   path(route="", view=index, name="katalog")
   ```

   Pada parameter kedua kita memilih fungsi mana yang akan dieksekusi oleh route. Pada kasus ini, fungsi `index` yang sudah dibuat tadi. Untuk parameter ketiga digunakan untuk merujuk ke suatu fungsi tertentu yang digunakan di html.

3. Memetakan data ke dalam berkas HTML di dalam folder **templates**

   Di dalam file `katalog.html` kita dapat menggunakan _template engines_ `jinja` untuk menampilkan data dari `context` yang sudah di berikan pada parameter ketiga. Sebagai contoh: key nama dalam `context` dapat digunakan di berkas HTML dengan cara:

   ```
   <p>{{name}}</p>
   ```

   maka value dari key nama akan dirender di halaman web.

4. Melakukan _deployment_
   Pada template GitHub untuk tugas ini, sudah terdapat konfigurasi untuk melakukan _deployment_ ke Heroku. Pada tahap ini, saya menggunakan heroku CLI untuk mengkonfigurasi semua hal terkait _deployment_. Langkah-langkah konfigurasinya sebagai berikut:

   - login ke Heroku CLI: `heroku login`
   - Membuat heroku app: `heroku create pbp-tugas2-recedivies`
   - Membuat API Token: `heroku authorizations:create`
   - Menyimpan konfigurasi variable di Heroku:
     ```
     heroku config:set HEROKU_API_KEY=<API Token> HEROKU_APP_NAME=pbp-tugas2-recedivies
     ```
   - Menyimpan konfigurasi variable seperti di Heroku pada GitHub bagian Secrets (`Settings -> Secret -> Actions`)
   - Jalankan workflows GitHub Actions. Setelah itu, seharusnya app sudah ter*deploy* di `https://pbp-tugas2-recedivies.herokuapp.com/`
