<img width="1070" height="887" alt="image" src="https://github.com/user-attachments/assets/ce126fb8-5b86-4ec0-adbd-0434d22e6f78" />web: https://razan-muhammad-kakibola.pbp.cs.ui.ac.id/

<!-- TUGAS 1:

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
    Tidak ada, karena topik tutorial 1 masih dapat dimengerti dengan mudah dan masih belum terlalu kompleks. Tetapi, asisten dosen pada tutorial 0 sangat membantu ketika troubleshooting masalah (karena saya masih sangat baru terhadap Django) -->

<!-- TUGAS 3:
    1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

        Ans: Data Delivery merupakan proses pemindahan data dari satu tempat ke tempat lain. Tanpa data delivery, maka platform berbasis internet atau wireless communication tidak mungkin terjadi karena suatu device (client) perlu mengirim semacam data yang akan diproses oleh suatu server (dan vice versa). Dari segi development, suatu platform memiliki banyak komponen/modul. Data delivery diperlukan agar semua komponen dapat saling menerima/mengirim data yang penting untuk tujuan platform.

    2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

        Ans: Menurut saya JSON lebih baik karena lebih mudah dibaca (less clutter than XML) dan lebih efisien dalam syntax-nya. Ex:
        (JSON) name: "el moment"
        (XML) <field name = "name" type = "CharField">ElMomentos</field> 
        dari format, JSON lebih human readable, apalagi jika terdapat banyak attribut.

    3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

        Ans: is_valid() berfungsi sebagai validator data form. method tsb mengecek apakah tipe data sesuai dengan tujuan dan ketentuan khusus (seperti max_char_length), dan menyimpan error ke atribut .errors jika terdapat data yang tidak sesuai. Tanpa method tersebut, data kotor/yang tidak diinginkan dapat masuk ke dalam database platform.

    4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
W
        Ans: Kita membutuhkan csrf_token untuk mencegah serangan Cross-Site Request Forgery. Jika crsf_token tidak ditambahkan, maka form tidak dapat diproses (403 Forbidden (CSRF Verification Failed)). Penyerang dapat memanfaatkan vulnerability ini dengan membuat kode HTML yang malicious. Jika suatu User masuk ke website ini, sang penyerang dapat membuat korban melakukan aksi tertentu yang menguntungkan penyerang, seperti me-reset akun korban pada suatu website.

    5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    
        Ans:

        Prelim: di views.py menambah:
        from main.models import Product
        from main.forms import ProductForm
        from django.http import HttpResponse
        from django.core import serializers

        agar object object tertentu dapat digunakan oleh fungsi-fungsi di views.py.

        1) pada views.py, membuat fungsi show_xml dan show_json dengan parameter 'request'.  dan isi:
        prod_list = Product.objects.all()
        (xml/json)_data = serializers.serialize("(xml/json)", prod_list)
        return HttpResponse((xml/json)_data), content_type="application/(xml/json)")

        2) masih di views.py, membuat fungsi show_xml_by_id dan show_json_by_id dengan parameter 'request' dan 'pk = prod_id' dengan isi:
            try:
            prod_item = Product.objects.filter(pk=prod_id)
            (xml/json)_data = serializers.serialize("(xml/json)", prod_item)
            return HttpResponse((xml/json)_data, content_type="application/xml")
        except Product.DoesNotExist:
            return HttpResponse(status=404) --jika produk tidak ada, akan mengeluarkan error

        3) di main/urls.py pada urlpatterns, menambah:
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:prod_id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:prod_id>/', show_json_by_id, name='show_json_by_id')

        agar fungsi-fungsi tersebut terjalan dan ditunjukkan ketika (url/xml/id product) dimasukkan ke address bar

        4) membuat file 'forms.py' di folder 'main'. dan mengimport ModelForm dari django.forms dan juga Product dari main.models. Membuat class bernama ProductForm dengan parameter ModelForm dan fields = ["name", "price", "category","description", "thumbnail", "is_featured"]. Fields ini digunakkan agar user/admin dapat memasukkan input ke dalam masing-masing kategori/field saat add_product.html ditunjukkan.

        5) Memodifikasi file 'main.html' dan menambahkan:
        <a href="{% url 'main:add_product' %}">
            <button>+ Add Product</button> --berfungsi sebagai tombol penambahan produk, ngeredirect ke fungsi/webpage add_product
        </a>

        <p><a href="{% url 'main:show_product' prod.id %}"><button>Details</button></a></p> --berfungsi sebagai tombol yang akan meredirect user ke detail produk

        6) Membuat folder 'templates' di root directory dan 'base.html' di dalamnya. .html file ini akan digunakan sebagai dasar dari exstensi webpage lain (seperti add_product dan show_product)

        7) Membuat file 'show_product.html' dan 'add_product.html' di 'main/templates' dan memodifikasinya agar dapat menampilkan nama, harga, deskripsi, dan thumbnail/gambar. Atau untuk kasus add_product, memodifikasinya agar dapat mengirim input. Kedua html ini mengextend dari file base.html.

        8) Menambah:
        path('add-product/', add_product, name = 'add_product' ),
        path('product/<str:id>/', show_product, name = 'show_product'),
        pada urls.py di urlpatterns agar webpage dapat meredirect ke kedua .html tersebut

        EXTRA NOTES:
        menambah CSRF Trusted Origins dengan url pws pada settings.py 
    
    6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
        Ans: Tidak pada saat ini, asdos saya (Kak marco) sangat membantu ketika saya mengalami kesulitan (yg sepertinya berdasarkan masalah dari sisi schema di PWS) dan saya hanya mengharap bahwa work ethic tim asdos tetap terjaga

POSTMAN IMAGES:<img width="1056" height="954" alt="image" src="https://github.com/user-attachments/assets/c59bde6a-ec28-44d7-b7ea-cc00f7400721" />
<img width="1065" height="990" alt="image" src="https://github.com/user-attachments/assets/f56bc864-cfd6-45d4-9aad-0919b7f92b29" />
<img width="1033" height="646" alt="image" src="https://github.com/user-attachments/assets/5d527832-fad9-47b1-b001-1239ae7df0e1" />
<img width="1017" height="871" alt="image" src="https://github.com/user-attachments/assets/6ceaaed0-8d30-4395-93a2-0fd33a55f24b" />
 -->

<!-- 
TUGAS 4:
    1) Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

    Ans: Django AuthenticationForm adalah form bawaan dari Django yang digunakan untuk mengautentikasi user (login). Form ini menyediakan interface untuk memvalidasi kredensial pengguna via Username dan Password. Kelebihan utama dari form itu adalah ease-of-use dari penggunaanya. AuthenticationForm sudah memiliki beberapa method seperti is_valid() yang memudahkan validasi input dengan melakukannya secara otomatis tanpa mengimplementasi fungsi login secara manual. Tetapi, form tersebut dapat dibilang relatif sederhana dan hanya mendukung autentikasi berdasarkan Username/Password. Sistem autentikasi lain seperti 2-Factor Authentication akan memerlukan kerja yang lebih ekstensif.

    2) Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

    Ans: Autentikasi adalah proses memverifikasi identitas User, sedangkan Otorisasi adalah proses menentukan apa yang diizinkan oleh User yang sudah diautentikasi. Django menyediakan AuthenticationForm untuk autentikasi dan menggunakan Cookies dan SessionID untuk menyimpan status login. Pada proyek ini, Django menggunakan decorator @login_required di views.py dimana hanya User yang sudah login/diautentikasi akan dapat mengakses webpage tsb. 

    3) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

    Ans: Session (Upside) =
    - Relatif lebih aman karena data disimpan di server sehingga informasi sensitif tidak dapat diakses langsung oleh Client. Hanya session ID saja yang dikirim ke Client. 

    - Session dapat menyimpan data yang besar tanpa restriksi ketat dan juga mampu menyimpan objek kompleks seperti JSON.

    Session (Downside)
    - Membebani Server karena harus menyimpan data untuk setiap pengguna yang menggunakan website. 
    - Non-Persistent; Akan hilang saat browser ditutup atau terjadi timeout, tidak cocok untuk penyimpanan jangka panjang.

    Cookies (Upside)
    - Dapat disimpan untuk jangka panjang via expiry date dan tidak akan hilang jika browser ditutup.
    - Tetap disimpan jika tidak terdapat koneksi internet. Website dapat dikonfigurasi agar ingat preferensi User.

    Cookies (Downside)
    - Keamanan relatif lebih rendah karena disimpan dalam bentuk plain-text tanpa enkripsi.
    - Memiliki restriksi 4kb size untuk data-datanya.

    4) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

    Ans: Cookies tidak aman secara default karena cookies dirancang untuk convenience. Cookies rentan oleh vektor serangan siber seperti serangan Cross-Site Request Forgery (CSRF) dimana cookies secara otomatis dikirim dengan setiap request ke domain yang sama, sehingga penyerang dapat melakukan aksi tanpa otorisasi atas nama User yang telah login. Django menangani hal tersebut dengan pengimplementasian CSRF Token via django.middleware.csrf.CsrfViewMiddleware yang otomatis aktif dalam setiap request. CSRF Token akan digenerate untuk setiap session dan Django akan memvalidasi token yang dikirim POST Requests. Jika token tidak valid, maka Django akan menolak request tsb.

    5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Ans:
        1. Mengimport UserCreationForm dan Messages pada views.py agar dapat membuat form registrasi user
        2. Membuat fungsi Register di views.py dengan UserCreationForm, memvalidasi input dengan is_valid() dan memastikan agar request yang dikirim bertipe POST agar tidak disimpan di URL (Request POST dilakukan jika informasi yang dikirim bersifat sensitif). Fungsi ini akan meredirect user ke webpage login dan ngerender register.html
        3. Pada templates/register.html, menambahkan: 
                <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        </div>

        agar registrasi dapat dilihat oleh user dan diproses

        4. Pada urls.py, mengimpor fungsi register dari views.py dan menambahkan urlpatterns dengan path('register/', register, name='register'),

        5. Untuk login, mengimport AuthenticationForm, authenticate, dan login di views.py dan membuat fungsi login_user dengan parameter request dan menambahkan
        if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

        6. Seperti registrasi, login.html perlu dibuat di templates dan memiliki konsep yang mirip. 
            <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet? --jika tidak ada akun
    <a href="{% url 'main:register' %}">Register Now</a>

    7. sama seperti registrasi, pada urls.py, login_user perlu diimpor dari views.py dan ditambahkan pada URLPatterns

    8. Untuk logout, membuat fungsi logout_user di views.py yang mengirim logout(request) dan akan meredirect ke loginpage. Membuat login.html di templates yang berisi tombol yang akan mengarah ke fungsi ini. Sama seperti registrasi dan login, logout_user juga perlu diimpor ke urls.py dan ditambahkan ke URLPatterns.

    9. menambah @login_required(login_url='/login') diatas fungsi show_main dan show_product dan juga mengimport login_required di views.py agar homepage dan product page memerlukan login agar dapat diakses.
    
    10. mengimport datetime, HttpResponseRedirect, dan reverse di views.py.

    11. Menambah user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    pada form.is_valid() di fungsi login_user dan last_login': request.COOKIES.get('last_login', 'Never') di context show_main. Cookies digunakan untuk mengetahui kapan user terakhir kali login.

    12. Pada logout_user, last_login akan didelete agar timer reset.

    13. Menambah kode <h5>Sesi terakhir login: {{ last_login }}</h5> di main.html untuk menampilkan waktu sejak last login. dan <h3>Username: {{name}}</h3> untuk menampilan username

    14. Pada models.py, import User dan di model Product, menambah user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) agar masing-masing produk akan terasosiasi dengan suatu user. Jika sebelumnya tidak dibuat oleh user, maka akan tetap valid. Setelah itu, melakukan migrasi agar memfinalisasi perubahan pada models.py

    15. pada views.py Menambah form = ProductForm(request.POST or None) di add_product dan news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save() dibawah entry is_valid().
    agaar setiap objek akan terhubung ke user penambah produk

    16. menambah:
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        news_list = News.objects.all()
    else:
        news_list = News.objects.filter(user=request.user) //agar produk dapat difilter berdasarkan siapa yang menambah produk tersebut (user yang login atau orang lain)

    di showw_main() dan mengedit context 'name' menjadi request.user.username, (agar name = username di html file)

    17. Menambah:
    <a href="?filter=all">
    <button type="button">All Articles</button>
    </a>
    <a href="?filter=my">
        <button type="button">My Articles</button>
    </a> 

    agar user dapat melihat dan menggunakan filter tersebut di webpage. -->

TUGAS 5:
    1)Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    
    Prioritasnya:
    - Inline Styles seperti <div style="color: red;">Text</div>
    - ID selectors seperti #myID { color: blue; }
    - Classes Selector seperti Kelas: .myClass { color: green; }
    - Element Selector seperti div { color: gray; }

    2) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

    ans: Responsive design sangat penting karena pada era ini terdapat banyak variasi dari device-device digital yang digunakan oleh masyarakat secara luas. Tanpa responsive design, website yang dapat digunakan dan dinavigasi dengan mudah di sebuah PC mungkin saja tidak berfungsi jika diakses dengan device mobile. Lebih spesifiknya, responsive web design akan beradaptasi dengan screen size/resolusi dari banyak device sehingga lebih sedikit incompatibilitas. Salah satu contoh website ini adalah art.yale.edu. Asumsi saya adalah UI/UX website tersebut sengaja dibuat tidak atraktif karena merupakan website tentang art. 

    3) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    ans: 
    Margin = ruang luar elemen yang memisahkan elemen dari yang lainnya
    Border = garis yang membatasi elemen dan berada di antara margin dan padding
    Padding = ruang di dalam elemen, antara konten elemen dan batas (border).

    ketiga hal tersebut dapat diimplementasi dengan menggunakan properti-properti masing masing elemen. ex:
    .element {
    margin: 20px;
    border: 2px solid #000;
    padding: 15px;
    }

    4) Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    ans:
    Flexbox adalah metode placement yang digunakan untuk mendistribusi space diantara elemen dalam satu dimensi (horizontal/vertikal). Flexbox memungkinkan elemen children (flex items) dalam suatu kontainer agar dapat ditambilkan dengan fleksibel. Flexbox responsif dan dapat beradaptasi dengan ukuran layar, selain itu, flexbox dapat digunakan untuk mengatur spacing antar elemen dengan properti seperti align-items dan justify-content.

    Grid layout memungkinkan user untuk mendefinisikan dua dimensi untuk elemen dalam kontainer grid. User dapat menentukan area grid dengan mendefinisikan grid-template-rows dan grid-template-columns, serta menyusun elemen dalam area yang ditentukan.

    5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    ans:  
    1. menambah fitur edit_product ke views.py dan mengaitkannya ke urls.py (dengan mengupdate database)
    2. menambah fitur delete_news ke views.py dan mengimport ke urls.py (dengan prod.delete)
    3. menambahkan tailwind ke base.html 
    4. membuat konfigurasi static files di setting.py dan membuat folder static/css untuk menyimpan global.css dimana file css  tersebut akan digunakan sebagai template tema untuk setiap form.
    5. menghubungkan global.css dan script tailwing ke main.html agar dapaat membuat design di main.html
    6. membuat stylesheet untuk masing-masing html dan juga menggunakan properti-properti seperti flex untuk placement masing-masing elemen. 
    7. mengedit masing-masing elemen dengan text-(color), bg (color), dan hover-(color) agar elemen-elemen tertentu berubah warna ketika cursor berada diatas elemen tersebut
    8. 
 

