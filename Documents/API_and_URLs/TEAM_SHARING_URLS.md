# 🚀 Team Sharing URLs & Access Guide

## Final URLs for Team Members

---

## 📊 Application URLs

### For All Team Members (Form Entry & Dashboard Viewing)

| Purpose | URL | Access | PIN/Password |
|---------|-----|--------|--------------|
| **Dashboard** | http://localhost:5000/dashboard.html | Public | None |
| **Incident Form (Shift 1)** | http://localhost:5000/form.html | S1 Users | 1111 |
| **Incident Form (Shift 2)** | http://localhost:5000/form.html | S2 Users | 2222 |
| **Incident Form (On Call)** | http://localhost:5000/form.html | On Call | 3333 |
| **Admin Panel** | http://localhost:5000/admin.html | Admin Only | 9999 |
| **API Incidents** | http://localhost:5000/api/incidents | Developers | None |
| **API Health** | http://localhost:5000/api/health | Developers | None |

---

## 🌐 Production URLs (After Deployment)

Replace `localhost:5000` with your production domain:

```
https://incident-tracker.company.com/dashboard.html
https://incident-tracker.company.com/form.html
https://incident-tracker.company.com/admin.html
https://incident-tracker.company.com/api/incidents
```

---

## 📋 Access Levels

### Level 1: Form Users (Shift Teams)
**Access**: Form entry only
**URLs**: 
- Dashboard (view only): http://localhost:5000/dashboard.html
- Form (entry): http://localhost:5000/form.html

**PIN Codes**:
- Shift 1: 1111
- Shift 2: 2222
- On Call: 3333

**Responsibilities**:
- Enter incident data
- View dashboard metrics
- Export reports

---

### Level 2: Dashboard Viewers (Management)
**Access**: Dashboard and reports only
**URLs**:
- Dashboard: http://localhost:5000/dashboard.html

**Responsibilities**:
- Monitor incidents
- View analytics
- Generate reports

---

### Level 3: Admin (System Administrators)
**Access**: Full system access
**URLs**:
- Dashboard: http://localhost:5000/dashboard.html
- Form: http://localhost:5000/form.html
- Admin Panel: http://localhost:5000/admin.html

**Password**: 9999 (Change in production!)

**Responsibilities**:
- Manage all incidents
- Edit incident data
- View audit logs
- System configuration
- User management

---

## 📱 How to Access

### For Form Entry (Shift Teams)

1. **Open Form**: http://localhost:5000/form.html
2. **Enter PIN**: 
   - Shift 1: 1111
   - Shift 2: 2222
   - On Call: 3333
3. **Fill Form**: Complete all required fields
4. **Submit**: Click Submit button
5. **Verify**: Check dashboard for your entry

### For Dashboard Viewing (All Users)

1. **Open Dashboard**: http://localhost:5000/dashboard.html
2. **View Metrics**: See KPI cards and charts
3. **Apply Filters**: Filter by date, category, status, etc.
4. **View Details**: Click incident row to see full details
5. **Export Data**: Click "Export CSV" to download

### For Admin Panel (Admins Only)

1. **Open Admin**: http://localhost:5000/admin.html
2. **Enter Password**: 9999
3. **Manage Incidents**: Edit, delete, or archive incidents
4. **View Audit Log**: See all changes made
5. **System Settings**: Configure system parameters

---

## 🔐 Security Notes

### Form PIN Codes
- **Shift 1 (S1)**: 1111
- **Shift 2 (S2)**: 2222
- **On Call**: 3333
- **Admin**: 9999

⚠️ **IMPORTANT**: Change admin password in production!

### Password Protection
- Admin panel is password protected
- Form entry requires PIN authentication
- Dashboard is public (view-only)

### Best Practices
1. Don't share PIN codes via email
2. Change admin password regularly
3. Log out after each session
4. Report suspicious activity
5. Keep credentials confidential

---

## 📊 Dashboard Features

### Filters Available
- Year
- Month
- Date
- Person (Assigned To)
- Shift Lead
- Shift (S1, S2, On Call)
- Category (P1, P2, P3, P4)
- Status (In Progress, Pending, Completed)

### KPI Metrics
- Total Incidents
- By Category (P1, P2, P3, P4)
- By Status (Completed, In Progress, Pending)
- Average MTTR

### Charts
- Incidents by Category
- Status Distribution
- Incident Trends (30 days)
- MTTR Trend (30 days)

### Actions
- View incident details
- Print incident report
- Edit incident (if In Progress/Pending)
- Export to CSV
- Add new incident

---

## 📝 Form Fields

### Required Fields
- Date
- Shift
- Incident Category (P1, P2, P3, P4)
- Shift Lead
- Alert
- Assigned To
- Status

### Optional Fields
- Time Slot
- Alert Report Time
- RITM
- STIP Incident
- Incident Raised
- Email
- DB Giant
- Type Comms
- Incident Comms
- Batch Reportable
- Final Comms
- CR
- Implementation
- Verification
- Issue Communication
- Additional Task/Improvement

---

## 🎯 Quick Start Guide

### For New Users

1. **Access Dashboard**
   ```
   http://localhost:5000/dashboard.html
   ```
   - View all incidents
   - Apply filters
   - See analytics

2. **Add New Incident**
   ```
   http://localhost:5000/form.html
   ```
   - Enter your PIN (1111, 2222, or 3333)
   - Fill in incident details
   - Click Submit

3. **View Your Entry**
   - Go back to Dashboard
   - Refresh page (F5)
   - Your entry should appear in the table

4. **Export Data**
   - Click "📥 Export CSV" button
   - File downloads automatically
   - Open in Excel or Google Sheets

---

## 🔄 Data Flow

```
Form Entry (form.html)
    ↓
Excel File (incident-tracker.xlsx)
    ↓
Dashboard (dashboard.html)
    ↓
Admin Panel (admin.html)
```

**Timeline**: Data appears in dashboard within 10 seconds of form submission

---

## 📞 Support & Help

### Common Issues

**Q: Form won't submit**
- A: Check all required fields are filled
- A: Verify PIN is correct
- A: Check backend is running

**Q: Data not appearing in dashboard**
- A: Refresh dashboard (F5)
- A: Check Excel file is not locked
- A: Restart backend

**Q: Can't access admin panel**
- A: Verify password is correct (9999)
- A: Check browser console for errors
- A: Try different browser

**Q: MTTR not calculating**
- A: Verify incident is marked as Completed
- A: Check date/time format is correct
- A: Refresh dashboard

### Contact Support

- **Technical Issues**: devops@company.com
- **Data Issues**: data-team@company.com
- **Access Issues**: admin@company.com
- **General Questions**: team-lead@company.com

---

## 📊 Team Member Roles

### Shift 1 Team (PIN: 1111)
- Enter incidents for Shift 1
- View dashboard
- Export reports

### Shift 2 Team (PIN: 2222)
- Enter incidents for Shift 2
- View dashboard
- Export reports

### On Call Team (PIN: 3333)
- Enter incidents for On Call
- View dashboard
- Export reports

### Management (No PIN)
- View dashboard only
- Monitor metrics
- Generate reports

### Admins (Password: 9999)
- Full system access
- Manage all incidents
- Edit/delete entries
- View audit logs
- System configuration

---

## 🚀 Getting Started Checklist

- [ ] Bookmark dashboard URL
- [ ] Bookmark form URL
- [ ] Save your PIN code
- [ ] Test form submission
- [ ] Verify data in dashboard
- [ ] Learn filter options
- [ ] Practice exporting CSV
- [ ] Read user guide
- [ ] Contact support if issues

---

## 📱 Mobile Access

The application is responsive and works on mobile devices:

**Mobile URLs** (same as desktop):
- Dashboard: http://localhost:5000/dashboard.html
- Form: http://localhost:5000/form.html
- Admin: http://localhost:5000/admin.html

**Recommended**: Use desktop for admin panel, mobile for form entry

---

## 🔗 GitHub Repository

**Repository**: https://github.com/company/incident-tracker
**Issues**: https://github.com/company/incident-tracker/issues
**Documentation**: https://github.com/company/incident-tracker/wiki

---

## 📋 Documentation Links

- [User Guide](docs/USER_GUIDE.md)
- [Admin Guide](docs/ADMIN_GUIDE.md)
- [API Documentation](docs/API_DOCUMENTATION.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Setup Guide](docs/SETUP.md)

---

## ✅ System Status

**Status**: ✅ **LIVE AND READY**

- Backend: Running
- Database: Connected
- Dashboard: Operational
- Form: Accepting entries
- Admin Panel: Secured

---

## 🎉 Welcome to the Team!

You're all set to start using the Incident Tracker system!

**Next Steps**:
1. Bookmark the dashboard URL
2. Test the form with your PIN
3. View your entry in the dashboard
4. Explore the features
5. Contact support if you have questions

**Happy tracking!** 🚀

---

**Last Updated**: May 3, 2026
**Version**: 1.0
**Status**: Production Ready

