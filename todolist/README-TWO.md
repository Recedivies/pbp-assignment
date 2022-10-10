<div align="center" style="padding-bottom: 10px">
<h1>Tugas 6 PBP</h1>
</div>

## Perbedaan antara _asynchronous programming_ dengan _synchronous programming_

Pada _synchronous programming_ melakukan pekerjaan dengan mengeksekusi baris program satu persatu secara hirarki. Task akan akan dieksekusi sesuai dengan urutan dan prioritas task. Hal ini berdampak pada waktu eksekusi akan menjadi lama karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

Sedangkan, pada _asynchronous programming_ tidak melakukan suatu task dengan eksekusi baris program satu persatu, melainkan melakukan task tanpa harus terikat dengan proses lain yang artinya setiap task sifatnya _independent_, untuk waktu eksekusi akan lebih cepat dibanding _synchronous programming_ ketika banyak task yang perlu diproses dalam waktu bersamaan.

## Paradigma _Event-Driven Programming_ dan contoh penerapannya pada tugas ini

Paradigma _Event-Driven Programming_ adalah salah satu teknik pemrograman yang konsep kejadiannya tergantung dari _event_ tertentu. Pada dasarnya, konsep _Event-Driven Programming_ sama seperti paradigma _Procedure_ yang memiliki input, proses, dan output. Yang membedakannya, alur programnya ditentukan oleh suatu _event_ untuk mengeksekusi programnya.

Contoh penerapannya dalam tugas ini ada saat pengimplementasian AJAX POST.

```js
$(`#${id}-delete-task`).click(() => {
  ...
});
```

Potongan kode di atas terdapat fungsi jQuery `$()` yang akan mengeksekusi ketika **button** dengan id `${id}-delete-task` diklik oleh _user_.

## Penerapan asynchronous programming pada AJAX

Pertama, ketika sebuah _event_ terjadi pada halaman web, misalnya tombol submit ditekan, maka JavaScript AJAX akan mengirimkan sebuah _request_ ke server. Setelah server memproses _request_ tersebut, server mengembalikan _response_ ke halaman web. Kemudian, _response_ akan dibaca oleh JavaScript yang nantinya dapat memanipulasikan halaman menggunakan HTML DOM.

## Implementasi Tugas 6

### **1.** AJAX GET

Pertama, membuat _view_ baru untuk mengembalikan data **Task** dalam bentuk JSON.

```py
def show_todolist_json(request):
    user = request.user
    data = Task.objects.filter(user=user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
```

Kemudian, membuat _path_ `/todolist/json` untuk mengarah ke view di atas.

```py
path("json/", show_todolist_json, name="show_todolist_json"),
```

Terakhir, dengan menggunakan AJAX GET, dapat melakukan _request_ ke server, yang nanti data _response_ nya dapat ditampilkan oleh JavaScript.

```js
$(document).ready(function () {
  ...
  $.get("http://127.0.0.1:8000/todolist/json/", (data) => {
    ...
  }
});
```

### **2.** AJAX POST

Pertama, membuat tombol `Add Task` yang dapat membuka **Modal** form untuk menambahkan _task_. Kemudian, membuat _view_ baru untuk menambahkan _task_ ke dalam _database_.

Membuat path `/todolist/add/` yang mengarah ke view di atas

```py
path("add/", add_task_ajax, name="add_task_ajax"),
```

Ketika _user_ mensubmit form di **Modal**, maka dengan AJAX POST akan melakukan _request_ ke server dengan _request body_ yang sudah diinput. Kemudian, _response_ dari server akan dibaca oleh JavaScript dan dapat dimanupulasi menggunakan HTML DOM sehingga dapat melakukan _refresh_ pada halaman utama secara _asinkronus_.

```js
$("#form-create-task").submit((e) => {
  e.preventDefault();
  $.post("http://127.0.0.1:8000/todolist/add/", {
    ...
  })
});
```
