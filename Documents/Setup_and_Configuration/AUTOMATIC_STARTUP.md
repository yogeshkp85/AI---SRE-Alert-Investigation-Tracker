# Automatic Startup Guide

## 🎯 Goal
Run the Flask backend automatically in the background so you can access all three interfaces without manually starting it each time.

---

## ✅ Current Status

**Backend is already running!** ✅

The Flask backend (`python app.py`) is now running in the background and will continue to run. You can access all three interfaces immediately without restarting.

---

## 🌐 Access the Interfaces

### Option 1: Use the Launcher Scripts (Easiest)

#### For Windows (Command Prompt):
```bash
OPEN_ALL_INTERFACES.bat
```

#### For Windows (PowerShell):
```powershell
.\OPEN_ALL_INTERFACES.ps1
```

#### For Mac/Linux:
```bash
open http://localhost:5000/dashboard.html
open http://localhost:5000/admin.html
open http://localhost:5000/form.html
```

### Option 2: Open Manually in Browser

Simply copy and paste these URLs into your browser:

1. **Dashboard**: http://localhost:5000/dashboard.html
2. **Admin Panel**: http://localhost:5000/admin.html (PIN: 9999)
3. **Form**: http://localhost:5000/form.html (PIN: 1111/2222/3333)

---

## 📋 What You Can Do Now

### Dashboard
- View 25 incidents
- See 5 KPI metrics
- View 4 interactive charts
- Apply 8 filters
- Sort and paginate table
- Export to CSV
- View incident details

### Admin Panel
- Login with PIN: 9999
- View all incidents
- Edit incidents
- Add new incidents
- Delete incidents
- Manage team members
- View audit log

### Form
- Login with PIN: 1111, 2222, or 3333
- Submit new incidents
- All 27 fields editable
- Real-time validation

---

## 🔄 Backend Status

### Check if Backend is Running

**Option 1: Check in Browser**
```
http://localhost:5000/api/health
```
You should see: `{"status":"ok","timestamp":"..."}`

**Option 2: Check with Command**
```bash
curl http://localhost:5000/api/health
```

---

## 🛑 Stop the Backend (if needed)

If you need to stop the backend:

1. **In Kiro IDE**: Use the process manager to stop the process
2. **In Command Line**: Press `Ctrl+C` in the terminal where it's running
3. **In Task Manager**: Find "python" process and end it

---

## 🔄 Restart the Backend

If the backend stops or you need to restart it:

```bash
python app.py
```

Or use Kiro's process manager to start it again.

---

## 📊 Test the System

### 1. Open Dashboard
- Should show 25 incidents
- Should show 5 KPI metrics
- Should show 4 charts
- Filters should work

### 2. Open Admin
- Login with PIN: 9999
- Should see incidents table
- Should be able to edit/add/delete

### 3. Open Form
- Login with PIN: 1111, 2222, or 3333
- Should be able to submit incident
- Should see success message

---

## 🚀 Permanent Automatic Startup (Optional)

If you want the backend to start automatically every time you open the project:

### Option 1: Create a Startup Hook (Recommended)

Create a file `.kiro/hooks/startup.json`:

```json
{
  "name": "Auto-start Flask Backend",
  "version": "1.0.0",
  "when": {
    "type": "userTriggered"
  },
  "then": {
    "type": "runCommand",
    "command": "python app.py"
  }
}
```

### Option 2: Use Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger to "At startup"
4. Set action to run: `python app.py` in project directory

### Option 3: Use Mac/Linux Cron

Add to crontab:
```bash
@reboot cd /path/to/project && python app.py
```

---

## 📝 Quick Reference

| What | How | URL |
|------|-----|-----|
| Dashboard | Open in browser | http://localhost:5000/dashboard.html |
| Admin | Open in browser + PIN 9999 | http://localhost:5000/admin.html |
| Form | Open in browser + PIN 1111/2222/3333 | http://localhost:5000/form.html |
| API Health | Check backend status | http://localhost:5000/api/health |
| All Incidents | Get JSON data | http://localhost:5000/api/incidents |

---

## 🎯 Next Steps

1. **Run launcher script**: `OPEN_ALL_INTERFACES.bat` (or .ps1)
2. **Or open manually**: Copy URLs to browser
3. **Test dashboard**: Verify 25 incidents display
4. **Test admin**: Login with PIN 9999
5. **Test form**: Submit a test incident

---

## ✨ Features Available Now

✅ Dashboard with KPIs and charts
✅ Admin panel with CRUD operations
✅ Form for submitting incidents
✅ 8 advanced filters
✅ Auto-refresh every 10 seconds
✅ CSV export
✅ Audit logging
✅ Team management
✅ SLA tracking

---

## 🆘 Troubleshooting

### "Connection refused" error
- Backend might have stopped
- Run: `python app.py` to restart
- Or use Kiro's process manager

### Dashboard shows blank metrics
- Ensure Excel file has data
- Run: `python populate_dummy_data.py`
- Refresh page (F5)

### Admin login fails
- PIN is: 9999
- Check backend is running
- Check browser console (F12)

### Charts not rendering
- Check internet connection (Chart.js CDN)
- Refresh page (F5)

---

## 📞 Support

For issues:
1. Check RUN_INSTRUCTIONS.md
2. Check QUICK_START.md
3. Check browser console (F12)
4. Verify backend is running

---

**Backend is running and ready to use!** 🚀

Use the launcher scripts or open the URLs manually to access all interfaces.
