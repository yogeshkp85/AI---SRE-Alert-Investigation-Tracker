# ⚡ Quick Start Summary - 5 Minutes Setup

For your friend to get the project running in 5 minutes!

---

## 🎯 The Process in 5 Steps

### Step 1: Clone the Repository (1 minute)

Open terminal/command prompt and run:

```bash
git clone https://github.com/yogeshkp85/AI---SRE-Alert-Investigation-Tracker.git
cd AI---SRE-Alert-Investigation-Tracker
```

### Step 2: Create Virtual Environment (1 minute)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies (1 minute)

```bash
pip install flask openpyxl
```

### Step 4: Run the Application (1 minute)

```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

### Step 5: Open in Browser (1 minute)

Visit these URLs:

| Interface | URL | Purpose |
|-----------|-----|---------|
| **Form** | http://localhost:5000/form.html | Submit incidents |
| **Dashboard** | http://localhost:5000/dashboard.html | View analytics |
| **Admin** | http://localhost:5000/admin.html | Manage incidents (PIN: 9999) |
| **URLs** | http://localhost:5000/urls.html | Quick reference |

---

## ✅ Verification Checklist

After setup, verify:

- [ ] Terminal shows "Running on http://127.0.0.1:5000"
- [ ] Form page loads without errors
- [ ] Dashboard displays correctly
- [ ] Can submit a test incident
- [ ] Incident appears on dashboard

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "python not found" | Install Python from https://www.python.org/downloads/ |
| "No module named flask" | Run: `pip install flask openpyxl` |
| "Port 5000 in use" | Change port in app.py or close other apps |
| "Cannot find incident-tracker.xlsx" | Ensure you're in project root directory |
| "Connection refused" | Flask server not running - run `python app.py` |

---

## 📁 What Gets Downloaded

```
AI---SRE-Alert-Investigation-Tracker/
├── app.py                    # Backend
├── templates/                # HTML interfaces
│   ├── form.html
│   ├── dashboard.html
│   ├── admin.html
│   └── urls.html
├── incident-tracker.xlsx     # Database
├── Documents/                # 60+ guides
├── README.md                 # Full documentation
└── SETUP_GUIDE_FOR_NEW_USERS.md  # Detailed setup
```

---

## 🚀 You're Ready!

Your friend can now:

1. ✅ Submit incidents via the form
2. ✅ View analytics on the dashboard
3. ✅ Manage incidents in the admin panel
4. ✅ Export data to CSV
5. ✅ Track MTTR and SLA metrics

---

## 📚 For More Details

- **Full Setup Guide:** `SETUP_GUIDE_FOR_NEW_USERS.md`
- **Project Overview:** `README.md`
- **Testing Guides:** `Documents/06_Testing_Guides/`
- **Feature Documentation:** `Documents/07_Feature_Documentation/`

---

## 💡 Pro Tips

1. **Keep Flask running** - Don't close the terminal while using the app
2. **Default Admin PIN** - Use `9999` to login to admin panel
3. **Auto-refresh** - Dashboard refreshes every 10 seconds automatically
4. **Export Data** - Use the dashboard export button to save as CSV
5. **Test Data** - Submit test incidents to see the system in action

---

## 🔄 Common Commands

```bash
# Start the app
python app.py

# Stop the app
Ctrl + C

# Deactivate virtual environment
deactivate

# Reactivate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Update dependencies
pip install --upgrade flask openpyxl
```

---

## 📞 Need Help?

1. Check `SETUP_GUIDE_FOR_NEW_USERS.md` for detailed troubleshooting
2. Review `README.md` for project overview
3. Check `Documents/` folder for comprehensive guides
4. Review code comments in `app.py`

---

**That's it! Your friend is ready to go! 🎉**
