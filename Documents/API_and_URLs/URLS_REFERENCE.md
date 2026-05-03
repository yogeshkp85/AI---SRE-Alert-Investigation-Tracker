# 🌐 URLs Reference - AI - SRE Alert Investigation Tracker

## Quick Access URLs

### Main Interfaces

| Interface | URL | Description |
|-----------|-----|-------------|
| **Dashboard** | http://localhost:5000/dashboard.html | Live incident monitoring with metrics and charts |
| **Alert Tracker Form** | http://localhost:5000/form.html | Create and submit new incident reports |
| **Administrator** | http://localhost:5000/admin.html | Admin panel for management (PIN: 9999) |
| **URLs Reference** | http://localhost:5000/urls.html | This page - all URLs in one place |

---

## API Endpoints

### Health & Status
```
GET http://localhost:5000/api/health
```
Check if the API is running and healthy.

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2026-05-03T12:34:56.789012"
}
```

---

### Incidents

#### Get All Incidents
```
GET http://localhost:5000/api/incidents
```
Retrieve all incidents from the database.

**Response**:
```json
{
  "count": 20,
  "incidents": [...],
  "timestamp": "2026-05-03T12:34:56.789012"
}
```

#### Create New Incident
```
POST http://localhost:5000/api/incidents
Content-Type: application/json

{
  "Date": "2026-05-03",
  "Shift": "S1",
  "Alert": "Payment Gateway Timeout",
  "Assigned To": "John Doe",
  "Status": "In Progress",
  "Incident Category": "P1",
  "Shift Lead": "Jane Smith"
}
```

#### Update Incident
```
PUT http://localhost:5000/api/incidents/<row_number>
Content-Type: application/json

{
  "Status": "Completed",
  "Assigned To": "Jane Smith"
}
```

#### Delete Incident (Admin Only)
```
DELETE http://localhost:5000/api/admin/incidents/<row_number>
```
Requires admin authentication.

---

### Admin Operations

#### Admin Login
```
POST http://localhost:5000/api/admin/login
Content-Type: application/json

{
  "pin": "9999"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Admin authenticated successfully"
}
```

#### Admin Logout
```
POST http://localhost:5000/api/admin/logout
```

#### Get Team Members
```
GET http://localhost:5000/api/admin/teams
```
Requires admin authentication.

#### Add Team Member
```
POST http://localhost:5000/api/admin/teams
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-0123"
}
```

#### Update Team Member
```
PUT http://localhost:5000/api/admin/teams/<name>
Content-Type: application/json

{
  "email": "newemail@example.com",
  "phone": "+1-555-0456"
}
```

#### Delete Team Member
```
DELETE http://localhost:5000/api/admin/teams/<name>
```

#### Get Audit Log
```
GET http://localhost:5000/api/admin/audit-log
```
Requires admin authentication.

---

### Data Export

#### Export as CSV
```
GET http://localhost:5000/api/export/csv
```
Downloads all incidents as a CSV file.

---

### Filters & Statistics

#### Get Filter Values
```
GET http://localhost:5000/api/incidents/filters
```
Get available values for filtering (years, months, persons, categories).

#### Get MTTR Statistics
```
GET http://localhost:5000/api/incidents/mttr
```
Get Mean Time To Resolution statistics and trends.

#### Get Categories
```
GET http://localhost:5000/api/categories
```
Get available categories, shifts, time slots, and statuses.

---

## Dashboard Features

### URL
```
http://localhost:5000/dashboard.html
```

### Key Features
- 📊 Real-time incident metrics
- 🔍 Advanced filtering (date, category, status, person, shift)
- 📈 Charts and trends (30-day view)
- ⏱️ MTTR (Mean Time To Resolution) tracking
- 📋 Incident table with pagination (50 per page)
- 🖨️ Print incident details
- 📥 Export to CSV

### Filters Available
- Year
- Month
- Date
- Person (Assigned To)
- Shift Lead
- Shift (S1, S2, On Call)
- Category (P1, P2, P3, P4)
- Status (In Progress, Pending, Completed)

---

## Alert Tracker Form Features

### URL
```
http://localhost:5000/form.html
```

### Key Features
- 📋 Comprehensive incident entry form
- ✓ Form validation
- 💾 Auto-save functionality
- 🔄 Error handling and recovery
- 📝 All required fields clearly marked

### Form Fields
- Date
- Shift
- Incident Category (P1-P4)
- Shift Lead
- Time Slot
- Alert Report Time
- Alert Description
- Assigned To
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
- Status

---

## Administrator Panel Features

### URL
```
http://localhost:5000/admin.html
```

### Authentication
- **PIN**: 9999
- **Session-based**: Secure session management

### Tabs

#### 1. Incidents Tab
- View all incidents
- Edit incident details
- Delete incidents
- Real-time updates

#### 2. Team Members Tab
- Add new team members
- Edit team member details
- Delete team members
- Manage assignments

#### 3. Audit Log Tab
- View all admin actions
- Track changes
- User activity log
- Timestamp tracking

---

## URLs Reference Page

### URL
```
http://localhost:5000/urls.html
```

### Features
- 🚀 Quick access buttons to all interfaces
- 📋 All URLs in one place
- 📋 API endpoints reference
- 💾 Copy-to-clipboard functionality
- ℹ️ System information and credentials

---

## Server Information

### Base URL
```
http://localhost:5000
```

### Port
```
5000
```

### Database
```
incident-tracker.xlsx
```

### Admin PIN
```
9999
```

---

## Quick Copy URLs

### Interfaces
```
Dashboard:    http://localhost:5000/dashboard.html
Form:         http://localhost:5000/form.html
Admin:        http://localhost:5000/admin.html
URLs:         http://localhost:5000/urls.html
```

### API
```
Health:       http://localhost:5000/api/health
Incidents:    http://localhost:5000/api/incidents
Export CSV:   http://localhost:5000/api/export/csv
```

---

## Browser Bookmarks

You can bookmark these URLs for quick access:

1. **Dashboard** - http://localhost:5000/dashboard.html
2. **Form** - http://localhost:5000/form.html
3. **Admin** - http://localhost:5000/admin.html
4. **URLs** - http://localhost:5000/urls.html

---

## Testing URLs

### Test the API
```bash
# Health check
curl http://localhost:5000/api/health

# Get all incidents
curl http://localhost:5000/api/incidents

# Export CSV
curl http://localhost:5000/api/export/csv > incidents.csv
```

---

## Troubleshooting

### Can't access URLs?
1. Verify Flask is running: `python app.py`
2. Check port 5000 is available
3. Verify localhost is accessible
4. Check firewall settings

### Admin PIN not working?
- Default PIN: **9999**
- Check caps lock is off
- Verify you're on the correct admin page

### API endpoints not responding?
1. Check Flask console for errors
2. Verify the endpoint URL is correct
3. Check request method (GET, POST, DELETE, etc.)
4. Verify Content-Type header for POST requests

---

## Last Updated
**Date**: May 3, 2026
**Version**: 1.0
**Status**: Active

---

## Support

For issues or questions:
1. Check the URLs Reference page: http://localhost:5000/urls.html
2. Review API documentation above
3. Check Flask console for error messages
4. Verify all services are running
