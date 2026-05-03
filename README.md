# AI - SRE Alert Investigation Tracker

A comprehensive incident tracking and management system designed for SRE (Site Reliability Engineering) teams to efficiently investigate, track, and resolve alerts and incidents.

## 📋 Overview

The AI - SRE Alert Investigation Tracker is a web-based application that provides:

- **Alert Submission Form** - Easy-to-use interface for reporting incidents
- **Interactive Dashboard** - Real-time visualization of incidents with advanced filtering and analytics
- **Admin Panel** - Comprehensive management interface for administrators
- **Audit Logging** - Complete audit trail of all system actions
- **MTTR Tracking** - Mean Time To Resolution metrics and analytics
- **Banking-Grade UI** - Professional, enterprise-ready interface

## 🚀 Features

### Form Interface
- Submit incidents with comprehensive details
- Automatic timestamp tracking
- Real-time Excel synchronization
- Success notifications
- Responsive design

### Dashboard
- Real-time incident visualization
- Advanced filtering (Year, Month, Date, Person, Category, Shift, Status)
- KPI metrics (Total Incidents, Category Breakdown, SLA Breaches, MTTR)
- Data visualizations with Chart.js
- Sortable table with pagination
- Modal detail view for incident inspection
- Auto-refresh every 10 seconds
- Export to CSV functionality

### Admin Panel
- Secure PIN-based authentication
- Incident management (Create, Read, Update, Delete)
- Team member management
- Audit log viewer
- Batch operations
- Professional admin interface

### Backend
- Flask-based REST API
- Excel-based data storage
- File locking for concurrent updates
- MTTR calculation engine
- Comprehensive audit logging
- Data validation and error handling

## 📁 Project Structure

```
.
├── app.py                          # Flask backend application
├── incident-tracker.xlsx           # Excel data storage
├── incident-tracker.xlsx.backup    # Backup of Excel file
├── templates/
│   ├── form.html                   # Incident submission form
│   ├── dashboard.html              # Analytics dashboard
│   ├── admin.html                  # Admin management panel
│   └── urls.html                   # URLs reference page
├── Documents/                      # Comprehensive documentation
│   ├── 01_Project_Overview/
│   ├── 02_System_Status_Reports/
│   ├── 03_Implementation_Guides/
│   ├── 04_Task_Completion_Reports/
│   ├── 05_Bug_Fixes_and_Debugging/
│   ├── 06_Testing_Guides/
│   ├── 07_Feature_Documentation/
│   ├── 08_Quick_References/
│   ├── 09_Setup_and_Configuration/
│   └── 10_Archived_Old_Files/
├── .kiro/
│   └── specs/
│       └── incident-tracker-enhancements/
│           ├── requirements.md     # Feature requirements
│           ├── design.md           # System design
│           └── tasks.md            # Implementation tasks
└── README.md                       # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-SRE-Alert-Investigation-Tracker.git
   cd AI-SRE-Alert-Investigation-Tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask openpyxl
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Form: http://localhost:5000/form.html
   - Dashboard: http://localhost:5000/dashboard.html
   - Admin: http://localhost:5000/admin.html
   - URLs: http://localhost:5000/urls.html

## 📊 API Endpoints

### Incident Management
- `GET /api/incidents` - Retrieve all incidents
- `POST /api/incidents` - Create new incident
- `GET /api/incidents/<id>` - Get incident details
- `PUT /api/incidents/<id>` - Update incident
- `DELETE /api/incidents/<id>` - Delete incident

### Filters & Analytics
- `GET /api/incidents/filters` - Get available filter values
- `GET /api/incidents/mttr` - Get MTTR statistics

### Admin Operations
- `POST /api/admin/login` - Admin authentication
- `POST /api/admin/logout` - Admin logout
- `POST /api/admin/incidents/<id>` - Admin update incident
- `DELETE /api/admin/incidents/<id>` - Admin delete incident
- `GET /api/admin/audit-log` - Retrieve audit log

### Team Management
- `GET /api/team/members` - Get team members
- `POST /api/team/members` - Add team member
- `PUT /api/team/members/<id>` - Update team member
- `DELETE /api/team/members/<id>` - Delete team member

## 🔐 Security

- Admin PIN-based authentication (default: 9999)
- Session management for admin users
- Comprehensive audit logging
- Input validation and sanitization
- File locking for concurrent access
- HTTPS-ready configuration

## 📈 Data Structure

The system tracks 27 incident fields:

1. Date
2. Shift
3. Incident Category (P1, P2, P3, P4)
4. Status
5. Alert
6. Assigned To
7. Shift Lead
8. RITM
9. Alert Time
10. SLA Status
11. Root Cause
12. Incident Description
13. Resolution
14. Verification Status
15. Additional Task/Improvement
16. Created At (Timestamp)
17. Completed At (Timestamp)
18. MTTR (Minutes)
19. Last Modified By
20. Last Modified At
21. Audit Log ID
22. And more...

## 🧪 Testing

Comprehensive testing guides are available in `Documents/06_Testing_Guides/`:

- Unit testing
- Integration testing
- Property-based testing
- Performance testing
- Security testing
- User acceptance testing
- Responsive design testing

## 📚 Documentation

Complete documentation is organized in the `Documents/` folder:

- **Setup & Configuration** - Installation and configuration guides
- **Implementation Guides** - Feature implementation details
- **Testing Guides** - Testing procedures and checklists
- **Bug Fixes** - Known issues and resolutions
- **Quick References** - Quick lookup guides

## 🔄 Workflow

### For End Users
1. Access the Form at `/form.html`
2. Fill in incident details
3. Submit the form
4. View incidents on Dashboard at `/dashboard.html`
5. Use filters and analytics to analyze incidents

### For Administrators
1. Access Admin Panel at `/admin.html`
2. Login with PIN (default: 9999)
3. Manage incidents (Create, Read, Update, Delete)
4. Manage team members
5. Review audit logs

## 🚀 Deployment

The application is production-ready and can be deployed to:
- Local servers
- Cloud platforms (AWS, Azure, GCP)
- Docker containers
- Traditional web servers

See `Documents/09_Setup_and_Configuration/` for deployment guides.

## 📝 License

This project is proprietary and confidential.

## 👥 Support

For issues, questions, or feature requests, please contact the development team.

## 🎯 Roadmap

- [ ] Real-time WebSocket notifications
- [ ] Advanced analytics and reporting
- [ ] Machine learning-based incident categorization
- [ ] Mobile app
- [ ] Integration with external incident management systems
- [ ] Custom dashboard widgets
- [ ] Advanced search capabilities

## 📞 Contact

For more information, please refer to the documentation in the `Documents/` folder or contact the project maintainers.

---

**Last Updated:** May 3, 2026  
**Version:** 1.0.0  
**Status:** Production Ready
