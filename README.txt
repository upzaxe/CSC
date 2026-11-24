CANDLE 2026 — Versi Modular
==========================
1. Ekstrak seluruh ZIP terlebih dahulu. Jangan memindahkan index.html sendiri.
2. Buka index.html di Chrome/Firefox untuk melihat website lengkap (offline).
3. Buka preview/00-index.html untuk meninjau tiap bagian atau aset secara terpisah.

STRUKTUR
index.html     : hasil penggabungan seluruh komponen; langsung bisa dibuka.
components/    : sumber HTML masing-masing bagian (9 file).
css/           : CSS dasar, setiap bagian, dialog dan responsif (11 file).
js/            : navigasi mobile dan interaksi dialog (2 file).
assets/images/ : gambar asli yang sebelumnya disematkan sebagai Base64.
preview/       : halaman pratinjau tiap komponen dan galeri gambar.
build.py       : penggabung komponen (Python 3, tanpa paket tambahan).

CARA EDIT
- Edit components/02-hero.html misalnya untuk mengubah hero.
- Edit css/03-hero.css untuk tampilan hero.
- Edit js/modal.js untuk logika pop-up.
- Ganti gambar di assets/images/ dengan nama file yang sama, atau perbarui path.
- Jalankan `python build.py` (atau `python3 build.py`) di folder proyek setelah
  mengedit komponen agar index.html dan preview komponen ikut diperbarui.
- CSS, JS dan gambar langsung terbaca tanpa build selama nama/path tetap sama.
- Jika hanya mengedit index.html secara langsung, perubahan tidak otomatis kembali
  ke components/; build berikutnya akan menimpa index.html.
- Komponen adalah fragmen HTML, bukan halaman mandiri. Untuk memeriksanya di
  browser, gunakan preview/ dengan nama sama.
- Tautan lintas bagian bekerja di index.html. Preview menampilkan satu bagian.
- Link eksternal memerlukan internet. Form resmi CSC/MAC tetap belum tersedia.
