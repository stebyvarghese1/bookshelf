# <p align="center">🪶 OpenSource Bookshelf</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
</p>

<p align="center">
  <strong>A modern, high-performance digital bookshelf and flipbook reader.</strong><br>
  Experience the charm of physical reading in a digital world.
</p>

---

## 🌟 Introduction

**OpenSource Bookshelf** is a sophisticated digital library platform designed for seamless book management and an immersive reading experience. Built with **Django** for a robust backend and **Turn.js** for a realistic page-turning interface, it bridges the gap between traditional books and digital accessibility.

Whether you are an administrator managing a vast collection or a reader looking for your next favorite book, Bookshelf provides an intuitive and responsive environment.

---

## 📸 Preview

<div align="center">

<table>
<tr>
<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/d3cf9a39-8534-4e01-9195-b9a3ca4fcbb7?raw=true" width="100%" />
<br/>
<b>📚 Home Dashboard</b>
</td>

<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/a945274e-509e-4cba-aad1-0e85fcd06727?raw=true" width="100%" />
<br/>
<b>🔍 Book view</b>
</td>
</tr>

<tr>
<td align="center" width="50%">
<img src="https://github.com/user-attachments/assets/3aa2812b-579b-4a30-aa3a-01b4de7d0f80?raw=true" width="100%" />
<br/>
<b>📖 Admin Book Details</b>
</td>

</tr>
</table>

</div>

---

## 🚀 Key Features

### 🛡️ Administrative Power
- **Intuitive Dashboard**: Manage your entire library through a clean, responsive admin interface.
- **Full CRUD Support**: Seamlessly upload, edit, and curate book Metadata.
- **Secure Authentication**: Robust admin credentials management and PostgreSQL data security.
- **Live Previews**: Instantly verify book covers and content before publishing.

### 📖 Reader Experience
- **Interactive Flipbook**: Realistic 3D page-turning effects powered by Turn.js.
- **Global Search**: Effortlessly find books by title, author, or description.
- **Theme Versatility**: Switch between **Light** and **Dark** modes for comfortable reading.
- **Universal Access**: Fully optimized for mobile, tablet, and desktop viewports.

---

## 🛠️ Technical Architecture

```text
[ Client Browser ] <---- HTTP/JSON ----> [ Django Server ]
      ^                                       |
      |                                       |
[ PDF.js / Turn.js ] <--- Media Stream --- [ Supabase Storage ]
                                              |
                                       [ PostgreSQL DB ]
```

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, Bootstrap 5, jQuery, Turn.js, PDF.js |
| **Backend** | Django 4.2+, Python |
| **Database** | PostgreSQL |
| **Storage** | Supabase (S3 Compliant) |
| **Auth** | Django Rest Framework (JWT Ready) |

---

## ⚡ Installation & Setup

### 1. Clone & Navigate
```bash
git clone https://github.com/stebyvarghese1/bookshelf.git
cd bookshelf
```

### 2. Environment Setup
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Database Configuration
Configure your PostgreSQL credentials in `config/settings.py` or `.env`:
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

### 4. Initialize & Launch
```bash
python manage.py makemigrations
python manage.py migrate

# Create Admin User
python manage.py shell
# >>> from books.models import AdminUser
# >>> admin = AdminUser(username="admin")
# >>> admin.set_password("admin123")
# >>> admin.save()

python manage.py runserver
```

---

## 🗺️ Roadmap & Future Enhancements

- [ ] **AI-Powered Read Aloud**: Integration of TTS for accessibility.
- [ ] **Advanced Organization**: Categories, tags, and custom collections.
- [ ] **Reader Profiles**: Personalized bookmarks and reading progress.
- [ ] **Offline Support**: PWA capabilities for reading without internet.
---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👤 Author

**Steby Varghese (King’sGuard)**  

<p align="left">
  <a href="https://github.com/stebyvarghese1">
    <img src="https://img.shields.io/badge/GitHub-stebyvarghese1-black?style=for-the-badge&logo=github" alt="GitHub" />
  </a>
</p>
