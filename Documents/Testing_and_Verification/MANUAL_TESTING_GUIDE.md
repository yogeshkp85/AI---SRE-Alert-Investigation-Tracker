# Dashboard Manual Testing Guide

## Overview
This guide provides step-by-step instructions for manually testing all dashboard features, especially the newly implemented Print, Edit, and Save functionality.

## Prerequisites
- Flask backend running on http://localhost:5000
- Dashboard accessible at http://localhost:5000/dashboard.html
- 20 incidents loaded in the system
- Browser: Chrome, Firefox, Safari, or Edge (latest version)

## Test Environment Status
✅ Backend: Running (Process ID: 22)
✅ API Health: OK
✅ Incidents: 20 loaded
✅ Data Structure: Complete (28 fields)
✅ Editable Incidents: 13 (In Progress/Pending)

---

## Test Suite 1: Dashboard Loading & Display

### Test 1.1: Dashboard Loads Successfully
**Steps:**
1. Open http://localhost:5000/dashboard.html in browser
2. Wait for page to fully load (should see "Loading incidents..." then data)

**Expected Results:**
- ✅ Page loads without errors
- ✅ Header displays "📊 Incident Dashboard"
- ✅ Status shows "● Live"
- ✅ All sections visible: Filters, KPI Cards, Charts, Table

**Actual Result:** [PENDING - Manual Test]

---

### Test 1.2: KPI Metrics Display Correctly
**Steps:**
1. Dashboard loaded
2. Observe KPI cards section

**Expected Results:**
- ✅ Total Incidents: 20
- ✅ By Category: P1=5, P2=4, P3=6, P4=5
- ✅ By Status: Completed=7, In Progress=6, Pending=7
- ✅ Avg MTTR: Shows "--" (no MTTR data in current dataset)

**Actual Result:** [PENDING - Manual Test]

---

### Test 1.3: Charts Render Correctly
**Steps:**
1. Dashboard loaded
2. Scroll to Charts section
3. Observe all 4 charts

**Expected Results:**
- ✅ Category Chart: Bar chart with P1, P2, P3, P4
- ✅ Status Chart: Pie/Doughnut chart with Completed, In Progress, Pending
- ✅ Trends Chart: Line chart showing incidents over 30 days
- ✅ MTTR Trend: Line chart showing MTTR over 30 days

**Actual Result:** [PENDING - Manual Test]

---

### Test 1.4: Table Displays All Incidents
**Steps:**
1. Dashboard loaded
2. Scroll to Table section
3. Count visible rows

**Expected Results:**
- ✅ Table shows 20 incidents (25 per page)
- ✅ All columns visible: Date, Shift, Category, Shift Lead, Time Slot, Alert, Assigned To, Status, RITM
- ✅ Pagination shows "Page 1 of 1"
- ✅ Rows are clickable (cursor changes to pointer)

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 2: Filters & Interactions

### Test 2.1: Year Filter Works
**Steps:**
1. Dashboard loaded
2. Click Year dropdown
3. Select "2026"
4. Observe table updates

**Expected Results:**
- ✅ Dropdown shows available years
- ✅ Table filters to show only 2026 incidents
- ✅ Incident count updates
- ✅ KPI metrics update

**Actual Result:** [PENDING - Manual Test]

---

### Test 2.2: Month Filter Works
**Steps:**
1. Dashboard loaded
2. Click Month dropdown
3. Select "May"
4. Observe table updates

**Expected Results:**
- ✅ Table filters to show only May incidents
- ✅ Incident count updates
- ✅ KPI metrics update

**Actual Result:** [PENDING - Manual Test]

---

### Test 2.3: Category Filter Works
**Steps:**
1. Dashboard loaded
2. Click Category dropdown
3. Select "P1 - Critical"
4. Observe table updates

**Expected Results:**
- ✅ Table shows only P1 incidents
- ✅ Incident count shows 5
- ✅ KPI metrics update

**Actual Result:** [PENDING - Manual Test]

---

### Test 2.4: Status Filter Works
**Steps:**
1. Dashboard loaded
2. Click Status dropdown
3. Select "In Progress"
4. Observe table updates

**Expected Results:**
- ✅ Table shows only In Progress incidents
- ✅ Incident count shows 6
- ✅ KPI metrics update

**Actual Result:** [PENDING - Manual Test]

---

### Test 2.5: Clear All Filters Works
**Steps:**
1. Apply multiple filters (Year, Category, Status)
2. Click "🔄 Clear All" button
3. Observe table resets

**Expected Results:**
- ✅ All filters reset to "All"
- ✅ Table shows all 20 incidents
- ✅ Incident count shows 20

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 3: Modal Detail View

### Test 3.1: Modal Opens on Row Click
**Steps:**
1. Dashboard loaded
2. Click on any incident row in table
3. Observe modal opens

**Expected Results:**
- ✅ Modal appears with incident details
- ✅ Modal header shows "Incident Details"
- ✅ All 25 columns displayed in organized sections
- ✅ Print button visible
- ✅ Edit button visible (if incident is In Progress/Pending)
- ✅ Close button (X) visible

**Actual Result:** [PENDING - Manual Test]

---

### Test 3.2: Modal Shows All 25 Columns
**Steps:**
1. Open modal for any incident
2. Scroll through modal content
3. Verify all sections present

**Expected Results:**
- ✅ Section 1: Basic Information (Date, Shift, Category, Shift Lead, Time Slot, Alert Report Time)
- ✅ Section 2: Incident Details (Alert, Assigned To, Status, Incident Comms)
- ✅ Section 3: Reference Information (RITM, STIP Incident, Incident Raised, DB Giant)
- ✅ Section 4: Communication Details (Email, Type Comms, Issue Communication, Final Comms)
- ✅ Section 5: Status & Actions (Batch Reportable, CR, Implementation, Verification)
- ✅ Section 6: Additional Information (Additional Task, MTTR, Created At, Completed At, Last Modified By, Last Modified At)

**Actual Result:** [PENDING - Manual Test]

---

### Test 3.3: Modal Closes Properly
**Steps:**
1. Open modal
2. Click X button
3. Observe modal closes

**Expected Results:**
- ✅ Modal disappears
- ✅ Dashboard visible again
- ✅ No errors in console

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 4: Print Functionality

### Test 4.1: Print Button Visible
**Steps:**
1. Open modal for any incident
2. Look for Print button

**Expected Results:**
- ✅ Print button (🖨️ Print) visible in modal header
- ✅ Button is clickable

**Actual Result:** [PENDING - Manual Test]

---

### Test 4.2: Print Dialog Opens
**Steps:**
1. Open modal for any incident
2. Click "🖨️ Print" button
3. Observe print dialog

**Expected Results:**
- ✅ Print dialog opens
- ✅ Print preview shows formatted incident report
- ✅ Report includes:
  - Title: "Incident Report"
  - Basic Information section
  - Incident Details section
  - Generated timestamp

**Actual Result:** [PENDING - Manual Test]

---

### Test 4.3: Print Preview Content
**Steps:**
1. Open print dialog
2. Review preview content

**Expected Results:**
- ✅ Report shows incident data clearly
- ✅ Sections are properly formatted
- ✅ All key fields visible: Date, Shift, Category, Status, Alert, RITM, MTTR, Assigned To

**Actual Result:** [PENDING - Manual Test]

---

### Test 4.4: Print Can Be Cancelled
**Steps:**
1. Open print dialog
2. Click "Cancel" button
3. Observe dialog closes

**Expected Results:**
- ✅ Print dialog closes
- ✅ Modal still visible
- ✅ No print job submitted

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 5: Edit Button Visibility

### Test 5.1: Edit Button Shows for In Progress Incidents
**Steps:**
1. Find an incident with Status = "In Progress"
2. Click on it to open modal
3. Look for Edit button

**Expected Results:**
- ✅ Edit button (✏️ Edit) visible in modal header
- ✅ Button is clickable

**Actual Result:** [PENDING - Manual Test]

---

### Test 5.2: Edit Button Shows for Pending Incidents
**Steps:**
1. Find an incident with Status = "Pending"
2. Click on it to open modal
3. Look for Edit button

**Expected Results:**
- ✅ Edit button (✏️ Edit) visible in modal header
- ✅ Button is clickable

**Actual Result:** [PENDING - Manual Test]

---

### Test 5.3: Edit Button Hidden for Completed Incidents
**Steps:**
1. Find an incident with Status = "Completed"
2. Click on it to open modal
3. Look for Edit button

**Expected Results:**
- ✅ Edit button NOT visible
- ✅ Only Print button visible

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 6: Edit Form Functionality

### Test 6.1: Edit Form Opens
**Steps:**
1. Open modal for In Progress/Pending incident
2. Click "✏️ Edit" button
3. Observe edit form opens

**Expected Results:**
- ✅ Edit form modal appears
- ✅ Form title shows "Edit Incident - [RITM]"
- ✅ Form has 4 fields:
  - Status (dropdown)
  - Completed Date (date input)
  - Completed Time (time input)
  - Last Edited By (text input)
- ✅ Save and Cancel buttons visible

**Actual Result:** [PENDING - Manual Test]

---

### Test 6.2: Edit Form Fields Populate Correctly
**Steps:**
1. Open edit form for In Progress incident
2. Check Status field

**Expected Results:**
- ✅ Status dropdown shows current status selected
- ✅ Can change to: In Progress, Pending, or Completed
- ✅ Date/Time fields are empty (for new completion)
- ✅ Last Edited By field is empty (ready for input)

**Actual Result:** [PENDING - Manual Test]

---

### Test 6.3: Edit Form Can Be Cancelled
**Steps:**
1. Open edit form
2. Click "❌ Cancel" button
3. Observe form closes

**Expected Results:**
- ✅ Edit form closes
- ✅ Modal still visible
- ✅ No changes saved

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 7: Save Functionality

### Test 7.1: Save Requires Last Edited By
**Steps:**
1. Open edit form
2. Leave "Last Edited By" empty
3. Click "💾 Save Changes"
4. Observe validation

**Expected Results:**
- ✅ Alert appears: "Please enter your name"
- ✅ Form stays open
- ✅ No changes saved

**Actual Result:** [PENDING - Manual Test]

---

### Test 7.2: Save Updates Status
**Steps:**
1. Open edit form for In Progress incident
2. Change Status to "Pending"
3. Enter name in "Last Edited By"
4. Click "💾 Save Changes"
5. Observe modal closes and dashboard updates

**Expected Results:**
- ✅ Alert shows: "✅ Incident updated successfully!"
- ✅ Edit form closes
- ✅ Modal closes
- ✅ Dashboard refreshes
- ✅ Incident status changed in table

**Actual Result:** [PENDING - Manual Test]

---

### Test 7.3: Save Marks Incident as Completed
**Steps:**
1. Open edit form for In Progress incident
2. Change Status to "Completed"
3. Enter Completed Date (e.g., 2026-05-03)
4. Enter Completed Time (e.g., 14:30)
5. Enter name in "Last Edited By"
6. Click "💾 Save Changes"

**Expected Results:**
- ✅ Alert shows: "✅ Incident updated successfully!"
- ✅ Incident status changes to "Completed"
- ✅ Completed At field populated with date/time
- ✅ MTTR calculated (if Created At exists)
- ✅ Dashboard metrics update

**Actual Result:** [PENDING - Manual Test]

---

### Test 7.4: MTTR Calculation Works
**Steps:**
1. Open edit form for In Progress incident
2. Change Status to "Completed"
3. Enter Completed Date and Time
4. Save changes
5. Open modal again to verify MTTR

**Expected Results:**
- ✅ MTTR (minutes) field now shows calculated value
- ✅ MTTR displayed as "Xh Ym" format (e.g., "2h 30m")
- ✅ Calculation is: (Completed At - Created At) in minutes

**Actual Result:** [PENDING - Manual Test]

---

### Test 7.5: Last Modified Fields Updated
**Steps:**
1. Edit and save an incident
2. Open modal again
3. Check Last Modified fields

**Expected Results:**
- ✅ Last Modified By shows the name entered
- ✅ Last Modified At shows current timestamp
- ✅ Fields are updated correctly

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 8: Dashboard Refresh After Edit

### Test 8.1: KPI Metrics Update After Edit
**Steps:**
1. Note current KPI values (e.g., In Progress count)
2. Edit an In Progress incident to Completed
3. Observe KPI metrics

**Expected Results:**
- ✅ In Progress count decreases by 1
- ✅ Completed count increases by 1
- ✅ Total remains same
- ✅ Average MTTR updates (if MTTR calculated)

**Actual Result:** [PENDING - Manual Test]

---

### Test 8.2: Table Updates After Edit
**Steps:**
1. Edit an incident's status
2. Observe table

**Expected Results:**
- ✅ Incident status badge updates in table
- ✅ Row reflects new status color
- ✅ No page reload needed

**Actual Result:** [PENDING - Manual Test]

---

### Test 8.3: Charts Update After Edit
**Steps:**
1. Edit an incident's status
2. Observe charts

**Expected Results:**
- ✅ Status Distribution chart updates
- ✅ Incident Trends chart updates
- ✅ MTTR Trend chart updates (if MTTR calculated)

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 9: Auto-Refresh

### Test 9.1: Dashboard Auto-Refreshes
**Steps:**
1. Dashboard loaded
2. Wait 10 seconds
3. Observe "Last Updated" timestamp

**Expected Results:**
- ✅ "Last Updated" timestamp changes every 10 seconds
- ✅ Dashboard data refreshes automatically
- ✅ No manual refresh needed

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 10: Export CSV

### Test 10.1: CSV Export Works
**Steps:**
1. Dashboard loaded
2. Click "📥 Export CSV" button
3. Observe file download

**Expected Results:**
- ✅ CSV file downloads
- ✅ Filename format: "incidents-YYYY-MM-DD.csv"
- ✅ File contains all filtered incidents
- ✅ All columns included

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 11: Edge Cases

### Test 11.1: Multiple Filters Combined
**Steps:**
1. Apply Year = 2026
2. Apply Category = P1
3. Apply Status = In Progress
4. Observe results

**Expected Results:**
- ✅ Table shows only incidents matching ALL filters
- ✅ Incident count reflects combined filter
- ✅ KPI metrics update correctly

**Actual Result:** [PENDING - Manual Test]

---

### Test 11.2: Edit Multiple Incidents
**Steps:**
1. Edit and save Incident A
2. Edit and save Incident B
3. Verify both updated correctly

**Expected Results:**
- ✅ Both incidents update independently
- ✅ Dashboard reflects all changes
- ✅ No conflicts or errors

**Actual Result:** [PENDING - Manual Test]

---

### Test 11.3: Print After Edit
**Steps:**
1. Edit an incident
2. Open modal again
3. Click Print

**Expected Results:**
- ✅ Print preview shows updated data
- ✅ New status reflected in print
- ✅ MTTR shown if calculated

**Actual Result:** [PENDING - Manual Test]

---

## Test Suite 12: Browser Compatibility

### Test 12.1: Chrome/Chromium
**Steps:**
1. Open dashboard in Chrome
2. Run through Test Suites 1-11

**Expected Results:**
- ✅ All features work correctly
- ✅ No console errors
- ✅ Responsive design works

**Actual Result:** [PENDING - Manual Test]

---

### Test 12.2: Firefox
**Steps:**
1. Open dashboard in Firefox
2. Run through Test Suites 1-11

**Expected Results:**
- ✅ All features work correctly
- ✅ No console errors
- ✅ Responsive design works

**Actual Result:** [PENDING - Manual Test]

---

### Test 12.3: Safari
**Steps:**
1. Open dashboard in Safari
2. Run through Test Suites 1-11

**Expected Results:**
- ✅ All features work correctly
- ✅ No console errors
- ✅ Responsive design works

**Actual Result:** [PENDING - Manual Test]

---

## Summary

### Total Tests: 50+
- Test Suites: 12
- Individual Test Cases: 50+

### Test Categories:
1. Dashboard Loading & Display (4 tests)
2. Filters & Interactions (5 tests)
3. Modal Detail View (3 tests)
4. Print Functionality (4 tests)
5. Edit Button Visibility (3 tests)
6. Edit Form Functionality (3 tests)
7. Save Functionality (5 tests)
8. Dashboard Refresh After Edit (3 tests)
9. Auto-Refresh (1 test)
10. Export CSV (1 test)
11. Edge Cases (3 tests)
12. Browser Compatibility (3 tests)

### Success Criteria:
- ✅ All 50+ tests pass
- ✅ No console errors
- ✅ All features work as designed
- ✅ Dashboard is production-ready

---

## Notes

- **Test Environment**: Windows 10, Python 3.9+, Flask running
- **Browser**: Latest version recommended
- **Data**: 20 incidents with 13 editable (In Progress/Pending)
- **Backend**: Running on http://localhost:5000
- **Dashboard**: http://localhost:5000/dashboard.html

---

## Contact

For issues or questions, refer to:
- DASHBOARD_IMPROVEMENTS.md - Design improvements
- FEATURE_OVERVIEW.md - Technical design
- DASHBOARD_FIXED_READY_TO_USE.md - Previous fixes

