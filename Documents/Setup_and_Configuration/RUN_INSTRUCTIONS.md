# How to Run the System

## Prerequisites
- Python 3.7+
- pip (Python package manager)
- Excel file: `incident-tracker.xlsx` (in project root)

---

## Step 1: Install Dependencies

Run this command once to install all required packages:

```bash
pip install flask flask-cors openpyxl
```

**Expected output:**
```
Successfully installed flask-2.x.x flask-cors-4.x.x openpyxl-3.x.x
```

---

## Step 2: Prepare the Data

### Option A: Add New Columns & Populate Test Data (Recommended)

```bash
# First, add 7 new columns to Excel
python migration_script.py

# Then, populate with 25 test entries
python populate_dummy_data.py
```

**Expected output:**
```
✓ Migration completed successfully
✓ Backup created: incident-tracker.xlsx.backup
✓ 7 new columns added

✓ Populated 25 dummy incidents
✓ Data saved to incident-tracker.xlsx
```

### Option B: Use Existing Data

If you already have data in the Excel file, skip the above and proceed to Step 3.

---

## Step 3: Start the Backend Server

```bash
python app.py
```

**Expected output:**
```
======================================================================
🚀 AI - SRE Alert Investigation Tracker
   Banking/Financial Institution Grade
======================================================================
✓ Excel file: incident-tracker.xlsx
✓ API running on: http://localhost:5000
✓ Form: http://localhost:5000/form.html
✓ Dashboard: http://localhost:5000/dashboard.html
✓ Admin: http://localhost:5000/admin.html
✓ Admin PIN: 9999
======================================================================
```

**Keep this terminal open while using the system.**

---

## Step 4: Access the Interfaces

Open your web browser and navigate to:

### 1. Incident Entry Form
```
http://localhost:5000/form.html
```
- **PIN**: 1111, 2222, or 3333
- **Purpose**: Submit new incidents
- **Features**: All 27 fields, validation, timestamps

### 2. Live Dashboard
```
http://localhost:5000/dashboard.html
```
- **No authentication required**
- **Purpose**: View and analyze incidents
- **Features**: KPIs, charts, filters, sorting, pagination

### 3. Admin Panel
```
http://localhost:5000/admin.html
```
- **PIN**: 9999
- **Purpose**: Manage incidents and team members
- **Features**: CRUD operations, audit log, team management

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Run `pip install flask flask-cors openpyxl`

### Issue: "Permission denied" when running Python scripts
**Solution**: 
- Close Excel if it's open
- Or run Command Prompt as Administrator
- Or use: `python migration_script.py` instead of just the filename

### Issue: "Address already in use" on port 5000
**Solution**: 
- Another app is using port 5000
- Kill the process: `lsof -ti:5000 | xargs kill -9` (Mac/Linux)
- Or restart your computer

### Issue: Dashboard shows blank metrics
**Solution**: 
- Ensure Excel file has data
- Run `python populate_dummy_data.py`
- Refresh the page (F5)

### Issue: Admin login fails
**Solution**: 
- Verify PIN is exactly: 9999
- Check backend is running
- Check browser console for errors (F12)

### Issue: Charts not rendering
**Solution**: 
- Check internet connection (Chart.js CDN)
- Refresh page (F5)
- Check browser console for errors (F12)

---

## Stopping the Server

To stop the backend server:

1. Go to the terminal where `python app.py` is running
2. Press `Ctrl+C`
3. You should see: `KeyboardInterrupt`

---

## File Structure

```
project-root/
├── app.py                          # Flask backend
├── incident-tracker.xlsx           # Excel data file
├── migration_script.py             # Add new columns
├── populate_dummy_data.py          # Add test data
├── templates/
│   ├── form.html                   # Incident entry form
│   ├── dashboard.html              # Live dashboard
│   └── admin.html                  # Admin panel
├── .kiro/
│   └── specs/
│       └── incident-tracker-enhancements/
│           ├── requirements.md
│           ├── design.md
│           ├── tasks.md
│           └── BRANDING_GUIDE.md
├── SETUP.md                        # Setup guide
├── QUICK_START.md                  # Quick reference
├── FIXES_APPLIED.md                # What was fixed
├── COMPLETION_SUMMARY.md           # Project summary
├── VERIFICATION_CHECKLIST.md       # Testing checklist
└── RUN_INSTRUCTIONS.md             # This file
```

---

## API Endpoints (for reference)

### Public Endpoints
- `GET /api/health` - Health check
- `GET /api/incidents` - Get all incidents
- `GET /api/incidents/filters` - Get filter values
- `GET /api/incidents/mttr` - Get MTTR statistics
- `GET /api/teams` - Get team members
- `GET /api/categories` - Get dropdown categories
- `POST /api/incidents` - Create new incident
- `GET /api/export/csv` - Export as CSV

### Admin Endpoints (requires PIN)
- `POST /api/admin/login` - Admin login
- `POST /api/admin/logout` - Admin logout
- `POST /api/admin/incidents/<row>` - Update incident
- `DELETE /api/admin/incidents/<row>` - Archive incident
- `GET /api/admin/audit-log` - Get audit log

---

## Performance Tips

1. **Dashboard**: Filters are applied client-side for instant response
2. **Auto-refresh**: Every 10 seconds, preserves current filters
3. **Pagination**: 25 rows per page for optimal performance
4. **Charts**: Rendered with Chart.js for smooth animations
5. **Export**: CSV export includes filtered data only

---

## Security Notes

1. **PINs**: Change default PINs in production
2. **CORS**: Enabled for local development only
3. **Sessions**: Admin sessions are server-side managed
4. **Audit Log**: All admin actions are logged
5. **File Locking**: Prevents concurrent write conflicts

---

## Next Steps

1. ✅ Run `python app.py`
2. ✅ Open http://localhost:5000/dashboard.html
3. ✅ Verify 25 incidents display
4. ✅ Test filters and charts
5. ✅ Try admin panel (PIN: 9999)
6. ✅ Submit a test incident via form

---

## Support

For issues:
1. Check the troubleshooting section above
2. Review FIXES_APPLIED.md for recent changes
3. Check browser console (F12) for errors
4. Verify backend is running: `python app.py`
5. Ensure Excel file is not locked

---

**System is ready to use!** 🚀
