# 🚀 Incident Tracker System - Setup Guide

**Payment Transaction Incident Management System - Option B (Excel-Based)**

---

## 📋 What You Have

1. **incident-tracker.xlsx** - Master Excel file (database)
2. **app.py** - Python Flask service (backend)
3. **form.html** - Incident entry form (secured with PIN)
4. **dashboard.html** - Live tracking dashboard (real-time SLA timers)
5. **SETUP.md** - This file (instructions)

---

## ⚙️ Prerequisites

- **Python 3.7+** (check: `python3 --version`)
- **Windows, Mac, or Linux**

---

## 🔧 Installation Steps

### Step 1: Check Python Installation

```bash
python3 --version
```

Should show Python 3.7 or higher.

---

### Step 2: Install Required Libraries

Open terminal/command prompt and run:

```bash
pip install flask flask-cors openpyxl
```

Or on some systems:

```bash
pip3 install flask flask-cors openpyxl
```

---

### Step 3: Create a Working Directory

Create a folder on your computer (e.g., `incident-tracker`):

```bash
mkdir incident-tracker
cd incident-tracker
```

---

### Step 4: Copy Files to Working Directory

Copy these files to your `incident-tracker` folder:
- `app.py`
- `incident-tracker.xlsx`
- `form.html`
- `dashboard.html`

**Folder structure should look like:**
```
incident-tracker/
├── app.py
├── incident-tracker.xlsx
├── form.html
├── dashboard.html
└── SETUP.md (this file)
```

---

### Step 5: Start the Python Service

Open terminal/command prompt in the `incident-tracker` folder and run:

```bash
python3 app.py
```

**Expected output:**
```
============================================================
🚀 Incident Tracker Service Starting
============================================================
✓ Excel file: incident-tracker.xlsx
✓ API running on: http://localhost:5000
✓ Form: http://localhost:5000/form.html
✓ Dashboard: http://localhost:5000/dashboard.html
============================================================
```

---

### Step 6: Open in Browser

Once the service is running, open your browser and visit:

**For Entry Form:**
```
http://localhost:5000/form.html
```

**For Live Dashboard:**
```
http://localhost:5000/dashboard.html
```

---

## 🔐 PIN Authentication

The form requires PIN to access:

- **Early Shift (S1):** `1111`
- **Main Shift (S2):** `2222`
- **Night Shift (On Call):** `3333`

Enter PIN → Form auto-selects your shift → Fill in details → Submit

---

## 📊 How to Use

### Adding a New Incident

1. Open **form.html** in browser
2. Enter your PIN (form auto-locks shift)
3. Fill in all required fields (marked with *)
4. Click **Submit** → Data saves to Excel automatically
5. Dashboard auto-refreshes in 10 seconds

### Viewing Live Status

1. Open **dashboard.html** in browser
2. Dashboard shows all incidents with:
   - SLA timer (countdown to deadline)
   - Color-coded severity (Critical/High/Medium)
   - Current status
   - Team member assignment
   - Auto-refreshes every 10 seconds

### Filtering Incidents

On dashboard:
- Filter by **Date**
- Filter by **Shift** (S1/S2/On Call)
- Filter by **Status** (In Progress/Pending/Completed)
- **Export to CSV** for reports

---

## 📝 Excel File Structure

**Column Headers (20 columns):**

```
A: Date                      (YYYY-MM-DD format)
B: Shift                     (S1, S2, On Call)
C: Time Slot                 (7-8 AM, 8-9 AM, etc.)
D: Alert Report Time         (HH:MM format)
E: Alert                     (Text - alert description)
F: Assigned To               (Team member name)
G: RITM                      (Reference number)
H: STIP Incident             (Reference number)
I: Incident Raised           (Reference number)
J: Email                     (Subject/details)
K: DB Giant                  (Database details)
L: Type Comms                (Communication type)
M: Incident Comms            (Incident communication)
N: Batch Reportable          (Yes/No)
O: Final Comms               (Final communication)
P: CR                        (Yes/No)
Q: Implementation            (Yes/No)
R: Verification              (Text)
S: Issue Communication       (Text)
T: Additional Task/Improvement (In Progress/Pending/Completed)
U: Status                    (In Progress/Pending/Completed)
```

---

## 🛑 Stopping the Service

Press **Ctrl+C** in the terminal where the service is running.

---

## 🔄 Restarting the Service

Each time you restart your computer or want to use the system again:

1. Open terminal in `incident-tracker` folder
2. Run: `python3 app.py`
3. Open browser to form.html or dashboard.html

---

## 🐛 Troubleshooting

### "Port 5000 already in use"

Another application is using port 5000. Either:
- Close the other application
- Or edit `app.py` line: change `PORT = 5000` to `PORT = 5001`

### "ModuleNotFoundError: No module named 'flask'"

Run: `pip install flask flask-cors openpyxl`

### "incident-tracker.xlsx not found"

Ensure the Excel file is in the same folder as `app.py`

### Form not connecting to Excel

- Check if `app.py` is running (you should see "running on..." message)
- Check browser console (F12) for error messages
- Ensure Excel file is not open in Microsoft Excel (it locks the file)

### Dashboard shows no incidents

- Check if data was actually submitted in the form
- Refresh dashboard (F5 or click Refresh button)
- Check the Excel file directly to see if rows were added

---

## 📱 Accessing from Other Computers

If you want other team members to access the form/dashboard:

**Find your computer IP:**

Windows:
```bash
ipconfig
```
Look for "IPv4 Address" (usually 192.168.x.x)

Mac/Linux:
```bash
ifconfig
```

**Other users access via:**
```
http://YOUR_IP:5000/form.html
http://YOUR_IP:5000/dashboard.html
```

Replace `YOUR_IP` with your actual IP address.

**Note:** Firewall might block access. You may need to allow Python through firewall.

---

## 🔒 Making It Production-Ready (Optional)

For a more robust setup:

1. **Use a proper web server** (Gunicorn, uWSGI)
2. **Add HTTPS/SSL** (Let's Encrypt)
3. **Database backup** (automated daily)
4. **User authentication** (instead of simple PIN)
5. **Email notifications** (when SLA breached)

Contact your IT team if you want these features.

---

## 📞 Support

If you encounter issues:

1. Check error messages in terminal where `app.py` is running
2. Check browser console (F12 → Console tab)
3. Verify all 4 files are in correct folder
4. Ensure Python 3.7+ is installed
5. Try restarting the service

---

## ✅ Quick Start Checklist

- [ ] Python 3.7+ installed
- [ ] Flask, flask-cors, openpyxl installed
- [ ] All 4 files in same folder
- [ ] `app.py` running (can see "🚀 Incident Tracker Service Starting")
- [ ] Form accessible at http://localhost:5000/form.html
- [ ] Dashboard accessible at http://localhost:5000/dashboard.html
- [ ] Can log in with PIN (1111/2222/3333)
- [ ] Can submit incident
- [ ] Dashboard shows new incident (refreshes every 10 sec)
- [ ] Excel file gets updated with new row

---

**System ready to go! 🚀**
