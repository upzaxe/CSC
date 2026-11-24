# CANDLE 2026 — GitHub Pages

Website statis Cendekia Student Challenge 2026. Sudah dirakit dan siap dipublikasikan; tidak membutuhkan npm, Python, backend, atau API untuk menampilkan halaman.

## Publikasi di GitHub Pages

1. Ekstrak ZIP. Buat repository GitHub publik, misalnya `candle-2026`.
2. Unggah **seluruh isi** hasil ekstraksi (bukan file ZIP atau folder pembungkus). Pastikan `index.html` ada di root repository, bersama `css/`, `js/`, `assets/`, `components/`, dan `preview/`.
3. Commit ke branch `main`. Masuk ke **Settings → Pages → Build and deployment**.
4. Pilih **Deploy from a branch**, branch **main**, folder **/(root)**, lalu **Save**.
5. Setelah deployment berhasil, buka alamat yang ditampilkan GitHub, biasanya `https://USERNAME.github.io/candle-2026/`.

`.nojekyll` adalah file kosong yang menonaktifkan pemrosesan Jekyll. Jika uploader menyembunyikan file tersebut, buat file `.nojekyll` secara langsung di root GitHub. Semua path CSS, JS, dan gambar relatif agar mendukung URL project GitHub Pages.

## Pengeditan

- `index.html`: halaman website siap pakai. Edit langsung untuk perubahan konten cepat.
- `css/`: desain terpisah per bagian; `js/`: interaksi; `assets/images/`: aset visual.
- `components/`: sumber HTML modular. Jika Anda mengedit komponen, jalankan `python build.py` secara lokal lalu commit hasil `index.html` dan `preview/`. Jangan menjalankan build setelah mengedit index langsung tanpa menyelaraskan komponen, karena build akan menimpa index.
- `preview/00-index.html`: galeri review komponen dan aset; tersedia juga setelah publikasi dengan menambahkan `/preview/00-index.html` pada URL proyek.
- `build.py`: utilitas opsional untuk pengembangan, bukan syarat hosting.

## Catatan sebelum publikasi resmi

Ini adalah prototipe frontend. Tidak memiliki database peserta, autentikasi, atau verifikasi pembayaran. Tautan pendaftaran CSC/MAC belum tersedia; gunakan kontak panitia yang tercantum. Periksa ulang tautan ACR, guidebook/QR, serta izin publikasi aset dan kontak sebelum digunakan resmi. Tautan eksternal membutuhkan internet.
