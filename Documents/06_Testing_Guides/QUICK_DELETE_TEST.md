# Quick Delete Functionality Test Guide

## Setup (2 minutes)
1. Start the Flask backend: `python app.py`
2. Open two browser tabs:
   - **Tab 1**: http://localhost:5000/admin.html (Admin Panel)
   - **Tab 2**: http://localhost:5000/dashboard.html (Dashboard)

## Test 1: Single Deletion (2 minutes)
**Objective**: Verify Dashboard updates immediately after deleting one incident

### Steps:
1. **Admin Tab (Tab 1)**:
   - Enter PIN: `9999`
   - Click "Login"
   - Look at the "Manage Incidents" table
   - Note the current incident count

2. **Dashboard Tab (Tab 2)**:
   - Wait for incidents to load
   - Note the "Total Incidents" KPI value
   - Note the incident count in the table

3. **Admin Tab (Tab 1)**:
   - Click "Delete" button on any incident
   - Confirm deletion when prompted
   - Wait 1 second for confirmation message

4. **Dashboard Tab (Tab 2)**:
   - **EXPECTED**: Incident count should decrease immediately
   - **EXPECTED**: "Total Incidents" KPI should decrease by 1
   - **EXPECTED**: Category counts (P1/P2/P3/P4) should update
   - **EXPECTED**: Status counts should update
   - **EXPECTED**: Table should refresh and show one fewer incident

### Result:
- ✅ **PASS** if Dashboard updates immediately
- ❌ **FAIL** if Dashboard waits for 10-second refresh

---

## Test 2: Multiple Sequential Deletions (3 minutes)
**Objective**: Verify Dashboard updates correctly after multiple deletions

### Steps:
1. **Admin Tab (Tab 1)**:
   - Delete 3 incidents one after another
   - Wait 1 second between each deletion

2. **Dashboard Tab (Tab 2)**:
   - Watch the "Total Incidents" KPI
   - **EXPECTED**: Should decrease by 1 after each deletion
   - **EXPECTED**: Should NOT wait for 10-second refresh

### Result:
- ✅ **PASS** if all 3 deletions update immediately
- ❌ **FAIL** if any deletion waits for auto-refresh

---

## Test 3: Category-Specific Deletion (2 minutes)
**Objective**: Verify category metrics update correctly

### Steps:
1. **Dashboard Tab (Tab 2)**:
   - Note the P1 count (e.g., 5)

2. **Admin Tab (Tab 1)**:
   - Find a P1 incident in the table
   - Delete it

3. **Dashboard Tab (Tab 2)**:
   - **EXPECTED**: P1 count should decrease by 1 (5 → 4)
   - **EXPECTED**: Total count should decrease by 1
   - **EXPECTED**: Category chart should update

### Result:
- ✅ **PASS** if P1 count decreases immediately
- ❌ **FAIL** if P1 count doesn't update

---

## Test 4: Status Update (2 minutes)
**Objective**: Verify status metrics update when editing

### Steps:
1. **Dashboard Tab (Tab 2)**:
   - Note the "In Progress" count

2. **Admin Tab (Tab 1)**:
   - Click "Edit" on an "In Progress" incident
   - Change status to "Completed"
   - Click "Save Changes"

3. **Dashboard Tab (Tab 2)**:
   - **EXPECTED**: "In Progress" count should decrease by 1
   - **EXPECTED**: "Completed" count should increase by 1
   - **EXPECTED**: Update should be immediate

### Result:
- ✅ **PASS** if status counts update immediately
- ❌ **FAIL** if status counts don't update

---

## Test 5: Cross-Tab Communication (2 minutes)
**Objective**: Verify localStorage communication works

### Steps:
1. Open browser Developer Tools (F12)
2. Go to **Application** → **Local Storage** → http://localhost:5000
3. **Admin Tab (Tab 1)**:
   - Delete an incident
   - Watch the Local Storage in Developer Tools
   - **EXPECTED**: `dashboardRefresh` key should appear with timestamp

4. **Dashboard Tab (Tab 2)**:
   - Open Developer Tools Console
   - **EXPECTED**: Should see message: "Dashboard refresh notification received from admin panel"
   - **EXPECTED**: Incident count should decrease

### Result:
- ✅ **PASS** if localStorage key appears and console message shows
- ❌ **FAIL** if no localStorage activity

---

## Troubleshooting

### Dashboard doesn't update after deletion:
1. Check browser console (F12) for errors
2. Verify Flask backend is running
3. Check if `dashboardRefresh` appears in Local Storage
4. Try refreshing Dashboard manually (F5)
5. Check if incident was actually deleted in Excel

### Deletion fails in Admin:
1. Verify Admin PIN is correct (9999)
2. Check Flask console for error messages
3. Verify Excel file is not locked by another program
4. Try deleting a different incident

### Charts don't update:
1. Wait 2 seconds for chart re-render
2. Try scrolling down to see updated charts
3. Check browser console for JavaScript errors

---

## Success Criteria

All tests should show:
- ✅ Immediate Dashboard updates (no 10-second wait)
- ✅ Correct incident count decreases
- ✅ Correct category/status metric updates
- ✅ Charts update immediately
- ✅ localStorage communication works
- ✅ No console errors

## Time Estimate
- Total test time: **~15 minutes**
- Per test: **2-3 minutes**

## Notes
- Tests can be run in any order
- Each test is independent
- No data cleanup needed between tests
- All changes are saved to Excel automatically
