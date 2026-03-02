<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,4,19&height=240&section=header&text=penSource%20Bookshelf&fontSize=62&fontColor=ffffff&fontAlignY=42&desc=A%20modern%20digital%20library%20with%20an%20immersive%20flipbook%20reader.&descAlignY=63&descSize=16&descColor=94a3b8&animation=fadeIn" width="100%"/>

</div>

<br>

<div align="center">

```
   Django  ·  PostgreSQL  ·  Supabase  ·  Turn.js  ·  PDF.js
```

</div>

<br>

<div align="center">

[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![License](https://img.shields.io/badge/License-MIT-fbbf24?style=for-the-badge)](LICENSE)

<br>

[![Stars](https://img.shields.io/github/stars/stebyvarghese1/bookshelf?style=flat-square&color=fbbf24&label=⭐%20Stars)](https://github.com/stebyvarghese1/bookshelf/stargazers)
&nbsp;
[![Forks](https://img.shields.io/github/forks/stebyvarghese1/bookshelf?style=flat-square&color=38bdf8&label=Forks)](https://github.com/stebyvarghese1/bookshelf/forks)
&nbsp;
[![Built by](https://img.shields.io/badge/by-Steby%20Varghese-a78bfa?style=flat-square)](https://github.com/stebyvarghese1)

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 01 `&nbsp;&nbsp; THE PRODUCT

</div>

<br>

<div align="center">

<table>
<tr>
<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/d3cf9a39-8534-4e01-9195-b9a3ca4fcbb7?raw=true" width="100%"/>
<br><br>
<b>📚 HOME DASHBOARD</b>
<br>
<sub>Browse and discover your entire library at a glance.</sub>
</td>
<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/a945274e-509e-4cba-aad1-0e85fcd06727?raw=true" width="100%"/>
<br><br>
<b>🔍 BOOK VIEW</b>
<br>
<sub>Immersive reader with realistic 3D page-turn effects.</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/3aa2812b-579b-4a30-aa3a-01b4de7d0f80?raw=true" width="100%"/>
<br><br>
<b>⚙️ ADMIN PANEL</b>
<br>
<sub>Full library management — upload, edit, curate.</sub>
</td>
<td align="center" width="50%">

```
  ╭──────────────────────────────╮
  │                              │
  │   Light & Dark mode          │
  │   Mobile · Tablet · Desktop  │
  │   Global search              │
  │   Realistic page-turning     │
  │   S3-compliant media         │
  │   JWT-ready auth             │
  │                              │
  ╰──────────────────────────────╯
```

</td>
</tr>
</table>

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 02 `&nbsp;&nbsp; THE IDEA

</div>

<br>

> ### *"The charm of turning a real page — delivered through a screen."*

<br>

**OpenSource Bookshelf** is a full-stack digital library platform that makes managing and reading books feel *alive*. Built on Django's robust backend and powered by Turn.js for lifelike 3D page-flip animations, it bridges the gap between the warmth of physical books and the convenience of digital access.

Whether you're an admin curating a vast collection or a reader searching for your next favourite — Bookshelf has you covered.

```
  ┌─────────────────────────────────────────────────────────┐
  │  📚  Administrators  →  Full CRUD library management    │
  │  👓  Readers         →  Immersive flipbook experience   │
  │  🌐  Everyone        →  Responsive on any device        │
  └─────────────────────────────────────────────────────────┘
```

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 03 `&nbsp;&nbsp; FEATURES

</div>

<br>

**🛡️ Admin Experience**

<div align="center">

| &nbsp; | Feature | Description |
|--------|---------|-------------|
| 🗂️ | **Intuitive Dashboard** | Manage your entire library from a clean responsive admin panel |
| ✏️ | **Full CRUD** | Upload, edit, and curate book metadata effortlessly |
| 🔒 | **Secure Auth** | Robust credentials management with PostgreSQL-backed security |
| 👁️ | **Live Previews** | Verify book covers and content before publishing |

</div>

<br>

**📖 Reader Experience**

<div align="center">

| &nbsp; | Feature | Description |
|--------|---------|-------------|
| 📄 | **Interactive Flipbook** | Realistic 3D page-turning effects powered by Turn.js |
| 🔍 | **Global Search** | Find books instantly by title, author, or description |
| 🌙 | **Light / Dark Mode** | Comfortable reading in any environment |
| 📱 | **Fully Responsive** | Optimised for mobile, tablet, and desktop viewports |

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 04 `&nbsp;&nbsp; ARCHITECTURE

</div>

<br>

<div align="center">

```
  ┌────────────────────┐
  │   Client Browser   │
  │  PDF.js · Turn.js  │
  └────────┬───────────┘
           │  HTTP / JSON
           ▼
  ┌────────────────────┐         ┌─────────────────────┐
  │   Django Server    │◀───────▶│   PostgreSQL DB      │
  │   Python 3 · DRF   │         │   Books · Users      │
  └────────┬───────────┘         │   Metadata           │
           │  Media Stream       └─────────────────────┘
           ▼
  ┌────────────────────┐
  │  Supabase Storage  │
  │  S3-Compliant      │
  │  Book PDFs · Covers│
  └────────────────────┘
```

</div>

<br>

<div align="center">

| Layer | Technology |
|-------|-----------|
| 🎨 **Frontend** | HTML5 · CSS3 · Bootstrap 5 · jQuery · Turn.js · PDF.js |
| ⚙️ **Backend** | Django 4.2+ · Python · Django REST Framework |
| 🗄️ **Database** | PostgreSQL |
| 🖼️ **Storage** | Supabase (S3-compliant) |
| 🔐 **Auth** | Django Auth · JWT Ready |

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 05 `&nbsp;&nbsp; GETTING STARTED

</div>

<br>

**Step 1 — Clone**
```bash
git clone https://github.com/stebyvarghese1/bookshelf.git
cd bookshelf
```

**Step 2 — Virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
```

**Step 3 — Configure database**

In `config/settings.py` or `.env`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookshelf_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Step 4 — Migrate & create admin**
```bash
python manage.py makemigrations
python manage.py migrate

python manage.py shell
>>> from books.models import AdminUser
>>> admin = AdminUser(username="admin")
>>> admin.set_password("admin123")
>>> admin.save()
```

**Step 5 — Launch**
```bash
python manage.py runserver
```

<div align="center">

> 🟢 &nbsp;**`http://127.0.0.1:8000`** &nbsp;— your library is open.

</div>

<br>
<br>

---

<div align="center">

## &nbsp;&nbsp;&nbsp;` 06 `&nbsp;&nbsp; ROADMAP

</div>

<br>

<div align="center">

```
  🔲  AI-powered read-aloud  (TTS accessibility integration)
  🔲  Categories, tags & custom collections
  🔲  Reader profiles with bookmarks & reading progress
  🔲  PWA support for offline reading
```

</div>

<br>
<br>

---

<br>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,4,19&height=130&section=footer&animation=fadeIn" width="100%"/>

### Built with ❤️ by [Steby Varghese](https://github.com/stebyvarghese1)

[![GitHub](https://img.shields.io/badge/GitHub-stebyvarghese1-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/stebyvarghese1)
&nbsp;
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-a78bfa?style=flat-square&logo=firefox&logoColor=white)](https://portfolio-v3ia.onrender.com/)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/steby-varghese)

<br>

**⭐ Star this repo if it made reading feel magical again!**

Licensed under [MIT](LICENSE)

</div>
