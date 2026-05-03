# AI - SRE Alert Investigation Tracker - Enhanced Feature Overview

## Project Branding

**Project Title:** AI - SRE Alert Investigation Tracker
**Color Scheme:** Navy Blue (#001F3F, #003366) & White (#FFFFFF)
**Design Level:** Banking/Financial Institution Enterprise Grade
**Logo:** PNG file space reserved at top-left corner (100x50px)

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    INCIDENT TRACKER SYSTEM                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Form.html   │  │Dashboard.html│  │ Admin.html   │          │
│  │              │  │              │  │              │          │
│  │ • PIN Auth   │  │ • KPI Metrics│  │ • Auth       │          │
│  │ • Entry Form │  │ • Filters    │  │ • Edit All   │          │
│  │ • 20 Fields  │  │ • Charts     │  │ • Audit Log  │          │
│  │ • Submit     │  │ • Table View │  │ • Sync       │          │
│  │ • Validation │  │ • Modal View │  │ • Archive    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                  │                  │                 │
│         └──────────────────┼──────────────────┘                 │
│                            │                                    │
│                    ┌───────▼────────┐                           │
│                    │   Flask API    │                           │
│                    │   (app.py)     │                           │
│                    │                │                           │
│                    │ • REST Endpoints│                          │
│                    │ • Auth Logic   │                           │
│                    │ • MTTR Calc    │                           │
│                    │ • Sync Logic   │                           │
│                    │ • Audit Log    │                           │
│                    └───────┬────────┘                           │
│                            │                                    │
│                    ┌───────▼────────────┐                       │
│                    │ Excel File (.xlsx) │                       │
│                    │                    │                       │
│                    │ • 27 Columns       │                       │
│                    │ • All Incidents    │                       │
│                    │ • Audit Trail      │                       │
│                    │ • MTTR Data        │                       │
│                    └────────────────────┘                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Form.html - Incident Entry Interface

### Features
- **PIN Authentication** - Shift-based access (S1: 1111, S2: 2222, On Call: 3333)
- **Incident Category** - Dropdown (P1, P2, P3, P4)
- **Shift Lead** - Dropdown (16 team members)
- **Additional Task** - Free text entry (unlimited)
- **20+ Fields** - All incident details
- **Real-time Validation** - Required field checking
- **Auto-sync** - Updates Excel immediately

### New Fields
```
Incident Category: [P1 ▼] [P2] [P3] [P4]
Shift Lead: [Select Lead ▼]
Additional Task/Improvement: [Free text area...]
```

---

## Dashboard.html - Analytics & Monitoring Interface

### KPI Metrics Section
```
┌─────────────────────────────────────────────────────────────┐
│                    KEY PERFORMANCE INDICATORS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Total      │  │  By Category │  │  By Status   │     │
│  │ Incidents    │  │              │  │              │     │
│  │     42       │  │ P1: 8        │  │ In Prog: 15  │     │
│  │              │  │ P2: 12       │  │ Pending: 18  │     │
│  │              │  │ P3: 15       │  │ Completed: 9 │     │
│  │              │  │ P4: 7        │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ SLA Breaches │  │ Avg MTTR     │  │ MTTR by Cat  │     │
│  │      3       │  │              │  │              │     │
│  │              │  │ 2h 15m       │  │ P1: 45m      │     │
│  │              │  │              │  │ P2: 1h 30m   │     │
│  │              │  │              │  │ P3: 2h 45m   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Enhanced Filters Section
```
┌─────────────────────────────────────────────────────────────┐
│                    ADVANCED FILTERS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Year: [2024 ▼]  Month: [May ▼]  Date: [2024-05-15 ▼]     │
│ Person: [All ▼]  Category: [All ▼]  Shift: [All ▼]       │
│ Status: [All ▼]  Shift Lead: [All ▼]                      │
│                                                             │
│ [🔄 Refresh]  [Clear All Filters]  [📥 Export CSV]        │
│                                                             │
│ Showing 12 of 42 incidents                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Charts Section
```
┌──────────────────────────────────────────────────────────────┐
│                    DATA VISUALIZATIONS                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │ Incidents by    │  │ Incident Trends │  │ Status      │ │
│  │ Category        │  │ (Last 30 Days)  │  │ Distribution│ │
│  │                 │  │                 │  │             │ │
│  │ P1: ████ 8      │  │ 5 ┤             │  │ In Prog: 36%│ │
│  │ P2: ██████ 12   │  │ 4 ┤    ╱╲       │  │ Pending: 43%│ │
│  │ P3: ████████ 15 │  │ 3 ┤   ╱  ╲     │  │ Completed:21│ │
│  │ P4: ██████ 7    │  │ 2 ┤  ╱    ╲    │  │             │ │
│  │                 │  │ 1 ┤_╱______╲_  │  │             │ │
│  │                 │  │   └─────────── │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ MTTR Trend (Last 30 Days)                            │  │
│  │                                                      │  │
│  │ 3h ┤                                                 │  │
│  │ 2h ┤    ╱╲        ╱╲                                 │  │
│  │ 1h ┤   ╱  ╲      ╱  ╲      ╱╲                       │  │
│  │    ┤__╱____╲____╱____╲____╱__╲__                    │  │
│  │    └──────────────────────────── │  │
│  │    May 1  May 5  May 10 May 15   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Table View Section
```
┌──────────────────────────────────────────────────────────────────────┐
│                    INCIDENTS TABLE (Sortable)                        │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Date ▲ │ Shift │ Category │ Status │ Alert │ Assigned │ MTTR │ SLA │
├────────┼───────┼──────────┼────────┼───────┼──────────┼──────┼─────┤
│ 5/15   │ S2    │ P1       │ Compl. │ DB... │ Raj      │ 45m  │ ✓   │
│ 5/14   │ S1    │ P2       │ In Pr. │ API.. │ Priya    │ 2h   │ ⚠️  │
│ 5/14   │ S2    │ P3       │ Pend.  │ Batch │ Vikram   │ --   │ ✗   │
│ 5/13   │ On C. │ P1       │ Compl. │ Timeout│ Manager A│ 1h30m│ ✓   │
│                                                                      │
│ [< Previous]  Page 1 of 2  [Next >]                                 │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Modal Detail View
```
┌─────────────────────────────────────────────────────────────┐
│ Incident Details                                        [X] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ BASIC INFORMATION                                           │
│ ├─ Date: 2024-05-15                                        │
│ ├─ Shift: S2                                               │
│ ├─ Shift Lead: Vikram Joshi                                │
│ ├─ Category: P1                                            │
│ └─ Time Slot: 2-3 PM                                       │
│                                                             │
│ INCIDENT DETAILS                                            │
│ ├─ Alert: Database timeout on payment processing           │
│ ├─ Assigned To: Raj Kumar                                  │
│ ├─ Alert Time: 14:30                                       │
│ └─ Status: Completed                                       │
│                                                             │
│ RESOLUTION METRICS                                          │
│ ├─ Created: 2024-05-15 14:30                               │
│ ├─ Completed: 2024-05-15 15:15                             │
│ ├─ Time to Resolution: 45 minutes                          │
│ └─ SLA Status: ✓ On Track                                  │
│                                                             │
│ REFERENCE INFORMATION                                       │
│ ├─ RITM: CHG0123456                                        │
│ ├─ STIP: INC0789012                                        │
│ └─ Incident Raised: INC0789012                             │
│                                                             │
│ COMMUNICATION DETAILS                                       │
│ ├─ Email: Payment DB Timeout Alert                         │
│ ├─ DB Giant: Database Connection Pool Exhausted            │
│ ├─ Type Comms: Escalation                                  │
│ └─ Incident Comms: Notified stakeholders                   │
│                                                             │
│ VERIFICATION & FOLLOW-UP                                    │
│ ├─ Verification: Connection pool increased to 100          │
│ ├─ Issue Comms: Root cause identified and fixed            │
│ └─ Additional Task: Monitor pool usage for 7 days          │
│                                                             │
│ [🖨️ Print]  [✏️ Edit]  [Close]                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Admin.html - Management Interface

### Authentication
```
┌─────────────────────────────────────────────────────────────┐
│              ADMIN AUTHENTICATION                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Admin PIN: [••••••••]                                      │
│                                                             │
│  [Login]  [Cancel]                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Admin Dashboard
```
┌─────────────────────────────────────────────────────────────┐
│ ADMIN PANEL - Logged in as: Admin User                 [🚪] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Search: [Search incidents...]  [🔍]                        │
│ Filter: [All Shifts ▼] [All Status ▼] [All Category ▼]   │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ ID │ Date   │ Category │ Status │ Alert │ Actions  │   │
│ ├────┼────────┼──────────┼────────┼───────┼──────────┤   │
│ │ 42 │ 5/15   │ P1       │ Compl. │ DB... │ [✏️ Edit]│   │
│ │ 41 │ 5/14   │ P2       │ In Pr. │ API.. │ [✏️ Edit]│   │
│ │ 40 │ 5/14   │ P3       │ Pend.  │ Batch │ [✏️ Edit]│   │
│ │ 39 │ 5/13   │ P1       │ Compl. │ Time. │ [✏️ Edit]│   │
│ │    │        │          │        │       │          │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ [Audit Log]  [Logout]                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Edit Form
```
┌─────────────────────────────────────────────────────────────┐
│ Edit Incident #42                                      [X] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ BASIC INFORMATION                                           │
│ Date: [2024-05-15]                                         │
│ Shift: [S2 ▼]                                              │
│ Shift Lead: [Vikram Joshi ▼]                               │
│ Category: [P1 ▼]                                           │
│ Time Slot: [2-3 PM ▼]                                      │
│                                                             │
│ INCIDENT DETAILS                                            │
│ Alert: [Database timeout on payment processing]            │
│ Assigned To: [Raj Kumar ▼]                                 │
│ Alert Time: [14:30]                                        │
│ Status: [Completed ▼]                                      │
│                                                             │
│ REFERENCE INFORMATION                                       │
│ RITM: [CHG0123456]                                         │
│ STIP Incident: [INC0789012]                                │
│ Incident Raised: [INC0789012]                              │
│                                                             │
│ ... (more fields)                                           │
│                                                             │
│ Last Modified: 2024-05-15 15:30 by Admin User              │
│                                                             │
│ [💾 Save]  [❌ Cancel]  [🗑️ Archive]                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Audit Log
```
┌─────────────────────────────────────────────────────────────┐
│ AUDIT LOG                                                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Timestamp          │ User      │ Action │ Incident │ Field │
├────────────────────┼───────────┼────────┼──────────┼───────┤
│ 2024-05-15 15:30   │ Admin     │ UPDATE │ #42      │ Status│
│ 2024-05-15 15:25   │ Admin     │ UPDATE │ #42      │ MTTR  │
│ 2024-05-15 14:35   │ Form User │ CREATE │ #42      │ --    │
│ 2024-05-14 18:45   │ Admin     │ UPDATE │ #41      │ Categ.│
│ 2024-05-14 18:40   │ Admin     │ DELETE │ #40      │ --    │
│                                                             │
│ [< Previous]  Page 1 of 5  [Next >]                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTIONS                        │
└─────────────────────────────────────────────────────────────┘

Form User:
  1. Enter PIN → Authenticate
  2. Fill incident form → Validate
  3. Submit → API POST /api/incidents
  4. Excel updated immediately
  5. Dashboard shows within 10 seconds

Dashboard User:
  1. Load dashboard
  2. Apply filters (Year, Month, Date, Person, Category, etc.)
  3. View KPIs, Charts, Table
  4. Click incident → Open modal
  5. Auto-refresh every 10 seconds

Admin User:
  1. Enter admin PIN → Authenticate
  2. Search/filter incidents
  3. Click Edit → Open edit form
  4. Modify fields → Validate
  5. Save → Excel updated immediately
  6. Dashboard/Form updated within 10 seconds
  7. Audit log records action
  8. MTTR recalculated if status changed
```

---

## Excel File Structure (27 Columns)

```
Column │ Name                      │ Type      │ Status
───────┼───────────────────────────┼───────────┼─────────────
A      │ Date                      │ Date      │ Existing
B      │ Incident Category         │ Dropdown  │ NEW
C      │ Shift                     │ Text      │ Existing
D      │ Shift Lead                │ Text      │ NEW
E      │ Time Slot                 │ Text      │ Existing
F      │ Alert Report Time         │ Time      │ Existing
G      │ Alert                     │ Text      │ Existing
H      │ Assigned To               │ Text      │ Existing
I      │ RITM                      │ Text      │ Existing
J      │ STIP Incident             │ Text      │ Existing
K      │ Incident Raised           │ Text      │ Existing
L      │ Email                     │ Text      │ Existing
M      │ DB Giant                  │ Text      │ Existing
N      │ Type Comms                │ Text      │ Existing
O      │ Incident Comms            │ Text      │ Existing
P      │ Batch Reportable          │ Yes/No    │ Existing
Q      │ Final Comms               │ Text      │ Existing
R      │ CR                        │ Yes/No    │ Existing
S      │ Implementation            │ Yes/No    │ Existing
T      │ Verification              │ Text      │ Existing
U      │ Issue Communication       │ Text      │ Existing
V      │ Additional Task/Improve.  │ Text      │ Existing (Modified)
W      │ Status                    │ Dropdown  │ Existing
X      │ Created At                │ Timestamp │ NEW
Y      │ Completed At              │ Timestamp │ NEW
Z      │ MTTR (minutes)            │ Number    │ NEW
AA     │ Last Modified By          │ Text      │ NEW
AB     │ Last Modified At          │ Timestamp │ NEW
```

---

## Key Metrics & KPIs

### Dashboard KPIs
- **Total Incidents** - Count of all incidents
- **By Category** - P1, P2, P3, P4 breakdown
- **By Status** - In Progress, Pending, Completed
- **SLA Breaches** - Count and percentage
- **Average MTTR** - Mean time to resolution
- **MTTR by Category** - P1, P2, P3, P4 breakdown

### Charts
- **Incidents by Category** - Bar chart
- **Incident Trends** - Line chart (last 30 days)
- **Status Distribution** - Pie chart
- **MTTR Trend** - Line chart (last 30 days)

---

## Security & Compliance

- **Form PIN** - Shift-based access control
- **Admin PIN** - Separate admin authentication
- **Audit Log** - Complete action history
- **Data Validation** - Input validation on all forms
- **File Locking** - Prevent concurrent write conflicts
- **Archive** - Soft delete instead of permanent removal
- **Session Management** - Automatic logout on inactivity

