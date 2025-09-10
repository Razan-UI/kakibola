web: https://razan-muhammad-kakibola.pbp.cs.ui.ac.id/


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 
    1) Membuat repositori github bernama "kakibola" di lokal dan server github

    2) via Terminal, menjalankan 'python -m venv env' di folder tsb. agar project tsb memiliki instalasi python dan package lain yang terpisah/terisolasi (agar tidak memiliki konflik di satu project dengan project lain)

    3) menjalankan 'env\Scripts\activate' untuk mengaktivkan env

    4) menginstall dependencies sepert {django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3, python-dotenv} dalam requirements.txt dan menjalankan pip install-r requirements.txt

    5) membuat Django Project dengan menjalankan 'django-admin startproject kaki_bola .' di terminal

    6) menambah 'PRODUCTION=False' di .env file. Line tersebut ditambahkan ketika melakukan testing/development agar dapat mendebug lebih mudah.

    7) membuat file .env.prod dengan isi:
    DB_NAME=<nama database>
    DB_HOST=<host database>
    DB_PORT=<port database>
    DB_USER=<username database>
    DB_PASSWORD=<password database>
    SCHEMA=tugas_individu
    PRODUCTION=True

    data diambil dari email yang dikirim di email UI. file ini digunakan untuk prod deployment di server

    8) di settings.py, menambahkan:
    `import os
    from dotenv import load_dotenv
    load_dotenv()`
    agar environment variables dapat diload 

    9) di file yang sama, menambahkan '["localhost", "127.0.0.1"]' di ALLOWED_HOSTS agar dapat mengakses aplikasi web melalui lokal host

    10) menambah:
    
    'if PRODUCTION:
        # Production: gunakan PostgreSQL dengan kredensial dari environment variables
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                }
            }
        }
    else:
        # Development: gunakan SQLite
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }' di settings.py pada bagian DATABASES

    11) membuat migrasi dengan python makemigrations dan migrate

    12) membuat project baru di Pacil Web Service bernama kakibola dan mendeploy local project ke PWS melalui git remote add pws, git branch -M master (utk membuat branch origin) dan git push pws master agar perubahan lokal dapat dideploy.

    13) pada Tab environs, menambahkan text dari file .env.prod dari local project. 

    14) menambah url deployment PWS ke ALLOWED_HOSTS di settings.py local agar project tsb dapat diakses oleh PWS.

    15) Balik ke project local, membuat aplikasi dengan naman 'main' dengan menjalankan 'python manage.py startapp main' di Terminal

    16) mendaftarkan 'main' di INSTALLED_APPS pada settings.py

    17) membuat File .html baru di folder 'templates' dan menambahkan beberapa header yang dikaitkan dengan variable pada views.py (on that later)

    18) menambah atribut yang sesuai dengan deskripsi tugas di models.py (name, price, desc, thumbnail, category, is_featured) dengan datatype yang sesuai.

    19) mengulang tahapan migrasi dengan python makemigrations dan migrate.

    20) di views.py, menambah line 'from django.shortcuts import render' agar template html dapat di-render.

    21) membuat fungsi dengan parameter 'request' yang menerima permintaan http dan mengembalikan variabel-variabel yang sesuai di dalam dictionary yang tertera agar dapat digunakan oleh file html.

    22) [Routing] membuat file urls.py di folder 'main' sebagai konfigurasi routing aplikasi

    23) mengisi file tsb dengan:
    'from django.urls import path       (mendefinisikan pola url)
    from main.views import show_main    (memanggil fungsi dari step 21 saat url cocok)

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]'

    24) di urls.py pada folder 'kaki_bola', menambah ', include' pada line 'from django.urls import path' 

    25) menambah 'path('', include('main.urls')),' ke dalam urlpatterns = [] untuk mengimport pola rute URL dari aplikasi main

    26) melakukan git push pws master untuk mengupdate versi deployment project ini

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
-> Terdapat file .drawio dan .svg bernama "BaganGambar" di repository ini dengan jawaban pertanyaan ini

3. Jelaskan peran settings.py dalam proyek Django!
    settings.py berisi semua konfigurasi dari instalasi project Django agar project tsb dapat dijalankan sesuai dengan rencana. Mengatur hal-hal seperti INSTALLED_APPS (list daftar aplikasi yang diaktifkan), ALLOWED_HOSTS (daftar nama domain yang dapat mengakses/melayani project Django tsb), dan TEMPLATES (mengatur dimana Django dapat mencari .html file) 

4. Bagaimana cara kerja migrasi database di Django?
    migrasi pada Djano bekerja seperti commit-push pada git.
    misalkan models.py telah diubah dan 'python manage.py makemigrations' dijalankan. Maka Django akan membandingkan versi models.py saat ini dengan iterasi sebelumnya. Jika ada, makan Django akan membuat file baru di folder 'migrations' (dalam project ini terdapat di main/migrations). Ketika 'python manage.py migrate' dijalankan, sama saja seperti 'push' pada git. Perubahan tsb. akan diterapkan ke dalam database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan        pembelajaran pengembangan perangkat lunak?
    Utamanya karena berdasarkan Python dan developer tidak perlu berinteraksi dengan SQL secara langsung karena Django memiliki Object-Relational Mapper. Python juga dapat dikatakan lebih "beginner-friendly" daripada bahasa pemrograman lain karena memiliki dynamic typing (salah satu alasannya)

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada, karena topik tutorial 1 masih dapat dimengerti dengan mudah dan masih belum terlalu kompleks. Tetapi, asisten dosen pada tutorial 0 sangat membantu ketika troubleshooting masalah (karena saya masih sangat baru terhadap Django)
    