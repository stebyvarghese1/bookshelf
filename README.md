# 🪶 OpenSource Bookshelf

A modern, responsive, and open-source digital bookshelf built using **Django** and **PostgreSQL**, where users can browse, search, and read books online using an integrated **flipbook reader**.  
Admins can upload, edit, and manage books easily through a simple, user-friendly admin interface.

---

## 📚 Features

### 🧑‍💻 For Admin
- Upload new books with cover, author, and description.  
- Edit or delete existing books.  
- Update admin credentials.  
- Manage data securely in PostgreSQL.  
- Access responsive dashboard with navigation and live preview.

### 📖 For Users
- Browse all books with cover and title.  
- Read books online using **Flipbook Reader** (Turn.js + PDF.js).  
- Search books by title or author.  
- Light/Dark theme support.  
- Fully responsive for mobile and desktop.

---
### 📖 Screenshorts
![Preview](https://github.com/stebyvarghese1/bookshelf/blob/main/Screenshot%202025-12-14%20144023.png?raw=true
)(https://github.com/stebyvarghese1/bookshelf/blob/main/Screenshot%202025-12-14%20144351.png?raw=true)


## ⚙️ Tech Stack

| Layer | Technology Used |
|-------|------------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript (jQuery), Turn.js, PDF.js |
| **Backend** | Django (Python) |
| **Database** | PostgreSQL |
| **Cloud Storage** | Supabase |
| **Version Control** | Git & GitHub |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/opensource-bookshelf.git
cd opensource-bookshelf
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookshelf_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Admin User
```bash
python manage.py shell
```
Then run:
```python
from books.models import AdminUser
admin = AdminUser(username="admin")
admin.set_password("admin123")
admin.save()
exit()
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```
Access it at **http://127.0.0.1:8000/**

---

## 🌗 Theme & UI

- Light/Dark mode toggle.  
- Adaptive responsive design.  
- Smooth Flipbook display.  
- “Read Aloud” feature (TTS planned).

---

## 🧠 Modules

1. **Admin Module** – Manage books and credentials.  
2. **User Module** – Browse, search, and read books.  
3. **Flipbook Reader Module** – Interactive page-turner.  
4. **Theme Module** – Switch light/dark mode.  
5. **Search Module** – Real-time book filtering.

---

## 🗄️ Database Design

| Table | Fields |
|--------|--------|
| **Book** | id, title, author, about, cover_url, file_url, uploaded_at |
| **AdminUser** | id, username, password |

---

## 🧩 Future Enhancements
- Add **Read Aloud** (Text-to-Speech).  
- Add **Book Categories** & **Favorites**.  
- User accounts & authentication.  
- Reading progress analytics.

---

## 🧑‍🤝‍🧑 Contributing

1. Fork the repo.  
2. Create a new branch (`feature/your-feature`).  
3. Commit & push your changes.  
4. Open a Pull Request.

---

## 🧾 License

Licensed under the **MIT License**.

---

## 💬 Credits

Developed by **King’sGuard**  
🎓 Ethical Hacking & MCA Student  
Open-Source Contributor | Passionate about clean web apps  
