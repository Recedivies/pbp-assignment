<div align="center" style="padding-bottom: 10px">
<h1>Tugas 3 PBP</h1>
</div>

## _Deployment_

Repositori ini telah di-_deploy_ ke Heroku. Anda dapat mengunjungi [di sini](https://pbp-tugas2-recedivies.herokuapp.com/).

## Perbedaan JSON, XML, dan HTML

Pertama, HTML merupakan kode yang digunakan pada menampilkan _web page_ dan isinya. Sama halnya seperti XML, tetapi HTML tidak digunakan untuk transfer data seperti XML atau JSON. Namun, HTML jika digunakan bersamaan dengan _framework_ tertentu, maka kita dapat memasukkan sebuah data ke dalam suatu tag HTML.

JSON dan XML keduanya digunakan untuk transfer dan menyimpan data. Keduanya menggunakan teks yang dapat mudah dibaca manusia dan lebih mudah untuk digunakan, sehingga banyak digunakan pada aplikasi web maupun _mobile_. Namun, keduanya berbeda dalam berbagai aspek, baik dari penerapan, format data, struktur data, dan bahkan keamanan. Pertama, ukuran dari file JSON lebih kecil. Maka dari itu, transfer data biasanya lebih cepat dibandingkan XML. Cara data disimpan dalam XML juga berbeda dari JSON. Bahasa _markup_ menyimpan data menggunakan tag dan dalam struktur pohon, sebaliknya, JSON menyimpannya dalam bentuk seperti map yang merupakan pasangan key-value dan dapat menggunakan array. Sebagai contoh perbedaan format XML dan JSON:

### JSON:

```json
{
  "student": [
    {
      "id": "01",
      "name": "John",
      "lastname": "Doe"
    },
    {
      "id": "02",
      "name": "Jane",
      "lastname": "Doe"
    }
  ]
}
```

### XML:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <student>
    <id>01</id>
    <name>John</name>
    <lastname>Doe</lastname>
  </student>
  <student>
    <id>02</id>
    <name>Jane</name>
    <lastname>Doe</lastname>
  </student>
</root>
```

## Mengapa kita perlu _data delivery_ dalam pengimplementasian sebuah _platform_?

Dalam pengembangan web atau _mobile_ platform, pasti banyak interaksi dimana pengguna dapat mengirim, menerima, menyimpan, atau menampilkan suatu informasi di halaman depan. Untuk melakukan hal tersebut, maka kita perlu proses transfer data yang dilakukan antara sisi client dan sisi server. Biasanya, dari sisi client akan melakukan _request_ ke sisi server. Nantinya, dari sisi server akan melakukan pemrosesan data, kemudian dikirim _response_ berupa data. Untuk melakukan proses _request_ dan _response_ tadi, maka kita perlu _data delivery_ dan format data untuk melakukan transfer data antar _stack_.

## Cara implementasi point 1 sampai 3

### **1.** Membuat aplikasi baru bernama **mywatchlist**

Pertama, pastikan sudah di dalam _virtual environment_ untuk tugas 3 ini dan sudah terinstall _package_ nya yang ada di file `requirements.txt`. Untuk membuat aplikasi baru, pastikan juga sudah berada di root direktori (ada **manage.py**) dan melakukan perintah berikut:

```shell
$ python3 manage.py startapp mywatchlist
```

Setelah _command_ di atas dijalankan, maka akan membuat direkotri **mywatchlist**, seperti berikut:

```
mywatchlist/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Untuk mendaftarkan app yang sudah dibuat, perlu ditambahkan aplikasi **mywatchlist** ke dalam variable `INSTALLED_APPS`.

```
INSTALLED_APPS = [
    ...,
    "mywatchlist",
]
```

### **2.** Menambahkan _path_ **mywatchlist** sehingga pengguna dapat mengakses ke `http://localhost:8000/mywatchlist`.

Pertama, perlu untuk memetakan ke URL, untuk itu perlu menunjuk root URLconf ke app **mywatchlist**. Dalam **project_django/urls.py** perlu ditambahkan **include()** dalam **urlpatterns** seperti berikut:

```
path("mywatchlist/", include("mywatchlist.urls")),
```

sehingga pengguna dapat mengakses ke suatu URL yang mengarah ke route **/mywatchlist/**.

### **3.** Membuat sebuah model **MyWatchList** yang memiliki beberapa atribut.

Dalam langkah ini, kita akan membuat model **MyWatchList** yang memiliki 5 atribut. Di dalam file **mywatchlist/models.py** ditambahkan kode berikut:

```python
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    release_date = models.DateField()
    review = models.TextField()
```

Terdapat 5 attribut, yang pertama `watched`, field yang tepat untuk menentukan apakah sudah ditonton atau belum adalah **BooleanField**. Kedua, `title`, field yang tepat adalah **CharField** yang biasanya di-_setting_ max nya adalah 255 berhubung judul tidak bakal lebih dari itu. Ketiga, ada `rating`, field nya adalah **IntegerField** dengan menambahkan sebuah _validator_ untuk memastikan yang terisi ke database hanya boleh dalam rentang 1 sampai 5. Keempat, ada `release_date`, fieldnya adalah **DateField** yang cocok untuk mencatat tahub-bulan-tanggal tanpa ada _time_ nya. Terakhir ada `review`, field yang tepat adalah **TextField** karena kita tidak tahu pasti berapa panjang string yang akan dimasukkan nantinya.

Setelah itu, buat migrasi skema model. Kemudian, jalankan migrate untuk menerapkan skema model tadi ke _database_

```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate

```

## Mengakses tiga URL dengan Postman

#### Format HTML

![Format HTML](https://user-images.githubusercontent.com/71712404/190842531-dec80128-14db-43cb-82bd-0df8e95f9a7f.png)

#### Format XML

![Format XML](https://user-images.githubusercontent.com/71712404/190845913-58eb796f-9933-4f9f-b29c-712f42e8a0c3.png)

#### Format JSON

![Format JSON](https://user-images.githubusercontent.com/71712404/190845901-105d4028-44d4-4b89-af13-96449ebdadfb.png)
