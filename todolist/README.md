<div align="center" style="padding-bottom: 10px">
<h1>Tugas 4 PBP</h1>
</div>

## _Deployment_

Repositori ini telah di-_deploy_ ke Heroku. Anda dapat mengunjungi [di sini](https://pbp-tugas2-recedivies.herokuapp.com/).

## Kegunaan {% csrf_token %} pada elemen `<form>`

CSRF token adalah suatu token aman yang acak yang digunakan untuk mencegah dari serangan CSRF (Cross Site Request Foreign). CSRF di sini hanya memastikan bahwa hanya formulir yang berasal dari _trusted_ domain yang dapat digunakan untuk membuat suatu formulir. Untuk semua _request_ yang tidak menggunakan HTTP _method_ GET, HEAD, OPTIONs, atau TRACE, maka cookie CSRF harus ada. Apabila tidak ada `{{% csrf_token %}}` pada elemen `<form>`, maka django akan memberikan pesan _error_ bahwa situs tersebut memerlukan cookie CSRF saat mengirim formulir.

## Membuat elemen `<form>` secara manual

membuat `<form>` dapat dilakukan secara manual tanpa menggunakan `{{form.as_table}}`. Caranya:
membuat semua field yang ingin diinput oleh pengguna dengan tag `<input type="<menyesuaikan fieldnya>"/>` beserta text fieldnya. Kemudian, di bagian paling bawah pengisian form, diberi sebuah tag `<input type="submit"/>` yang digunakan sebagai submisi dari field yang telah diisi dalam formulir.

## Proses alur data

Pertama, ketika pengguna melakukan submisi melalui HTML form, maka dilakukan _request_ dengan method HTTP POST ke server. Dari server, mengecek jika _request_ nya valid atau tidak. Jika valid maka dilakukan penyimpanan data tersebut ke _database_ sehingga nantinya data yang telah disimpan akan muncul pada _template_ HTML.

## Implementasi Tugas 4

### **1.** Membuat aplikasi baru bernama **todolist**

Pertama, pastikan sudah di dalam _virtual environment_ untuk tugas 4 ini dan sudah terinstall _package_ nya yang ada di file `requirements.txt`. Untuk membuat aplikasi baru, pastikan juga sudah berada di root direktori (ada **manage.py**) dan melakukan perintah berikut:

```shell
$ python3 manage.py startapp todolist
```

Setelah _command_ di atas dijalankan, maka akan membuat direkotri **todolist**, seperti berikut:

```
todolist/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Untuk mendaftarkan app yang sudah dibuat, perlu ditambahkan aplikasi **todolist** ke dalam variable `INSTALLED_APPS`.

```
INSTALLED_APPS = [
    ...,
    "todolist",
]
```

### **2.** Menambahkan _path_ **todolist** sehingga pengguna dapat mengakses ke `http://localhost:8000/todolist`.

Pertama, perlu untuk memetakan ke URL, untuk itu perlu menunjuk root URLconf ke app **todolist**. Dalam **project_django/urls.py** perlu ditambahkan **include()** dalam **urlpatterns** seperti berikut:

```
path("todolist/", include("todolist.urls")),
```

sehingga pengguna dapat mengakses ke suatu URL yang mengarah ke route **/todolist/**.

### **3.** Membuat sebuah model **todolist** yang memiliki beberapa atribut.

Dalam langkah ini, kita akan membuat model **todolist** yang memiliki 5 atribut. Di dalam file **todolist/models.py** ditambahkan kode berikut:

```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

Terdapat 5 attribut, yang pertama `user`, fieldnya adalah **ForeignKey** yang berarti ForeignKey ini me*refrence* ke table User (many-to-one). Kedua, ada `date`, fieldnya adalah **DateTimeField** yang cocok untuk mencatat kapan _task_ tersebut dibuat. Ketiga, `title`, field yang tepat adalah **CharField** yang biasanya di-_setting_ max nya adalah 255 berhubung judul _task_ tidak akan lebih dari itu. Keempat, ada `description`, field yang tepat adalah **TextField** karena kita tidak tahu pasti berapa panjang string yang akan dimasukkan nantinya. Terakhir, `is_finished`, field yang tepat adalah **BooleanField** dengan default _value_ nya False, field ini untuk menandakan bahwa _task_ tersebut sudah selesai atau belum.

Setelah itu, buat migrasi skema model. Kemudian, jalankan migrate untuk menerapkan skema model tadi ke _database_

```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### **4.** Mengimplementasikan form registrasi, _login_, dan _logout_

Di dalam berkas `views.py`, buat fungsi **_register_**, kemudian menggunakan fungsi _built-in_ django yaitu `UserCreationForm` untuk membuat formulir registrasi pengguna yang ada di berkas `register.html`.

Untuk form _login_, buat fungsi **login_user** yang menggunakan fungsi _built-in_ django yaitu `authenticate` untuk memverifikasi kredensial pengguna (**username** dan **password**) ketika membuat submisi formulir _login_ yang ada di berkas `login.html`.

Kemudian, form _logout_, buat fungsi **logout_user** yang menggunakan fungsi _built-in_ django yaitu `logout` untuk menghapus seluruh data _session_ pada pengguna.

### **5.** Membuat halaman utama **todolist** yang memuat username pengguna, tombol `Tambah Task Baru`, tombol logout, serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.

Pertama, membuat fungsi untuk `show_todolist` untuk menampilkan data username pengguna, dan tabel yang berisi informasi _task_ yang bersesuaian dengan pengguna.

```python
@login_required(login_url="/todolist/login/")
def show_todolist(request):
    user = request.user
    todolist = Task.objects.filter(user=user)
    return render(
        request,
        template_name="todolist.html",
        context={
            "todolist": todolist,
            "username": user.username,
        },
    )
```

sehingga, nanti di berkas `todolist.html` dapat diloop todolist dan juga dapat menggunakan data username pengguna.

Kemudian, di berkas `todolist.html` tambahkan tombol `Tambah Task Baru` untuk mengarahkan ke formulir pembuatan _task_ yang nanti akan ke _route_ **/create-task/**.

dan yang terakhir tambahkan juga tombol untuk _logout_

```html
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
```

untuk melakukan _logout_ user.

### **6.** Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

Membuat file `forms.py` di direkotri app **todolist** untuk pembuatan _task_. Karena data yang perlu dimasukkan pengguna hanya _title_ dan _description_, maka isi form nya seperti berikut:

```python
class TaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description", widget=forms.Textarea)
```

Nanti, di dalam berkas `create-task.html`, dapat dibuat halaman form untuk pembuatan _task_ menggunakan _generator_ `{{ form.as_table }}`

### **7.** Membuat routing sehingga beberapa fungsi dapat diakses melalui URL

Membuat file `urls.py` untuk memetakan fungsi yang telah dibuat pada langkah sebelumnya di direktori app **todolist**. Membuat urlpatterns yang berisi:

```python
urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("create-task/", create_task, name="create-task"),
    path("update-task/<int:pk>/", update_task, name="update-task"),
    path("delete-task/<int:pk>/", delete_task, name="delete-task"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
```

sehingga beberapa fungsi dapat diakses melalui URL di atas.

### **8.** Melakukan deployment

Pada template GitHub untuk tugas ini, sudah terdapat konfigurasi untuk melakukan _deployment_ ke Heroku. Pada tahap ini, saya menggunakan Heroku CLI untuk mengkonfigurasi semua hal terkait _deployment_. Langkah-langkah konfigurasinya sebagai berikut:

- login ke Heroku CLI: `heroku login`
- Membuat heroku app: `heroku create pbp-tugas2-recedivies`
- Membuat API Token: `heroku authorizations:create`
- Menyimpan konfigurasi variable di Heroku:
  ```
  heroku config:set HEROKU_API_KEY=<API Token> HEROKU_APP_NAME=pbp-tugas2-recedivies
  ```
- Menyimpan konfigurasi variable seperti di Heroku pada GitHub bagian Secrets (`Settings -> Secret -> Actions`)
- Jalankan workflows GitHub Actions. Setelah itu, seharusnya app sudah ter*deploy* di `https://pbp-tugas2-recedivies.herokuapp.com/`

### **9.** Membuat dua akun pengguna dan tiga dummy data menggunakan model `Task`

Pada tahap ini, cara mengimplementasikannya dengan membuat _custom_ _command_ django `manage.py` baru. Untuk lebih jelasnya terdapat di file seed.py pada direktori: `project_django` -> `management` -> `commands` -> `seed.py`. Nanti pada saat fase _release_ ke Heroku, di `Procfile` dijalankan _command_ `python manage.py seed --mode=refresh` untuk melakukan _seeding_ _dummy_ _data_ di _database server_ Heroku secara otomatis.

<div align="center" style="padding-bottom: 10px">
<h1>Tugas 5 PBP</h1>
</div>

## Perbedaan inline, internal, dan external CSS

1. Inline Styles: CSS dimasukkan di dalam tag pembuka HTML dengan _attribute_ `style="<properties:value>;"`.

2. Internal (Embedded) Style Sheet: CSS dibuat di dalam tag `<style>...</style>` di bagian `HEAD` dari dokumen HTML.

3. External Style Sheet: CSS dibuat di file yang terpisah. Untuk memakainya, ditautkan ke berkas HTML melalui tag `<link>` di bagian `HEAD`.

Untuk prioritas, dari nomor 1 memiliki prioritas tertinggi yang diikuti oleh nomor-nomor selanjutnya.

## Tag HTML5

HTML5 menambahkan banyak elemen blok semantik, yang biasanya hanya menggunakan tag `<div>`. Contohnya seperti:

1. `<header>`
   Elemen dapat digunakan untuk menandai kalau itu merupakan `header` dari halaman web.

2. `<main>`
   Elemen dapat digunakan untuk menandai konten utama dari halaman web, tidak termasuk `header`, `footer`, dan navigasi menu lainnya. Sebaiknya hanya ada satu tag `main` di berkas HTML.

3. `<section>`
   Elemen dapat digunakan untuk menandai setiap bagian konten dalam halaman web.

4. `<footer>`
   Elemen dapat digunakan untuk menandai kalau itu merupakan `footer` dari halaman web.

## CSS Selector

Tipe-tipe CSS Selector yang saya ketahui dan biasanya sering dipakai adalah:

1. `*`
   Contoh pemakaiannya: `* { }`
   Selector ini sifatnya universal sehingga berlaku untuk **semua** elements yang ada di HTML.

2. `nama-tag`
   Contoh pemakaiannya: `h1 { }`
   Tag Selector, yang berarti hanya berlaku untuk semua elemen tertentu yang dipilih. Untuk contoh di atas, berarti untuk semua elemen `<h1>`.

3. `#nama-id`
   Contoh pemakaiannya: `#header { }`
   ID Selector, yang berarti memilih elemen dengan id yang **unik**. Untuk contoh di atas, berarti tag dengan _attribute_ `id="header"`.

4. `.nama-class`
   Contoh pemakaiannya: `.card { }`
   Class Selector, yang berarti memilih elemen dengan class. Untuk contoh di atas, berarti tag dengan _attribute_ `class="card"`.

5. `:nama-pseudo`
   Contoh pemakaiannya: `card:hover { }`
   Pseudo-Class Selector, yang berarti memilih elemen dengan class dengan didefinisikan _state_ khusus. Untuk contoh di atas, berarti class `card` akan melakukan sesuatu ketika di*hover*(saat kursor berada di atasnya).

## Implementasi Tugas 5

### **1.** Kustomisasi templat untuk halaman login, register, dan create-task

Membuat halaman login, register, dan create-task menjadi di tengah layar. Dengan cara, membuat id `#form` beserta properties-properties yang dibutuhkan di berkas `style.css`.

### **2.** Kustomisasi halaman utama todo list menggunakan _cards_

Membuat Class Selector CSS `.card` di berkas `style.css` untuk mengatur border dan juga margin. Untuk pembuatan `card` nya dapat menggunakan `template` dari Bootstrap dengan class `card`.

### **3.** Membuat keempat halaman yang dikustomisasi menjadi _responsive_

Membuat `Media Query`, pertama pada halaman utama todo list, jika `Media Query` nya kecil, maka akan muncul _hamburger menu_ untuk menampilkan tombol logout. Untuk tasks _card_, secara otomatis _responsive_ dengan menggunakan class bawaan Bootstrap. Untuk ketiga halamannya, dibuat _responsive_ ketika *max-width*nya sudah 600px, maka dapat di*scroll* untuk tetap bisa mengisi formulirnya.
