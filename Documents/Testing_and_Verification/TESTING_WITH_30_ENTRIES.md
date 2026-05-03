# Testing Dashboard with 30 Real Entries

## Overview
This guide will help you add 30 real entries through the Form.html, verify they flow to Excel, and then display correctly in Dashboard and Admin.html.

---

## Step 1: Verify Backend is Running

```bash
# Check if Flask is running
curl http://localhost:5000/api/health
# Should return: {"status":"ok","timestamp":"..."}
```

---

## Step 2: Open Form.html

```
http://localhost:5000/form.html
```

### Form PIN Codes
- **Shift 1 (S1)**: PIN 1111
- **Shift 2 (S2)**: PIN 2222
- **On Call**: PIN 3333

---

## Step 3: Add 30 Real Entries

### Entry Template (Fill these fields for each entry)

**Basic Information:**
- Date: [Select date]
- Shift: [S1, S2, or On Call]
- Shift Lead: [Select from dropdown]
- Time Slot: [Select from dropdown]
- Incident Category: [P1, P2, P3, or P4]

**Incident Details:**
- Alert Report Time: [HH:MM format]
- Alert: [Describe the alert/issue]
- Assigned To: [Select person]
- Status: [In Progress, Pending, or Completed]

**Reference Information:**
- RITM: [Change Request ID]
- STIP Incident: [STIP ID]
- Incident Raised: [Incident ID]

**Communication:**
- Email: [Email subject]
- DB Giant: [Database alert]
- Type Comms: [Communication type]
- Incident Comms: [Communication details]

**Actions:**
- Batch Reportable: [Yes/No]
- Final Comms: [Final communication]
- CR: [Yes/No]
- Implementation: [Yes/No]
- Verification: [Verification details]
- Issue Communication: [Issue details]
- Additional Task/Improvement: [Additional notes]

### Suggested 30 Entries

**Entries 1-10: P1 Critical Issues**
1. Database Connection Pool Exhausted (S1, In Progress)
2. API Gateway Timeout (S2, Pending)
3. Payment Processing Failed (S1, Completed)
4. Authentication Service Down (S2, In Progress)
5. Cache Layer Failure (On Call, Pending)
6. Load Balancer Error (S1, Completed)
7. SSL Certificate Expiration (S2, In Progress)
8. Database Replication Lag (S1, Pending)
9. Memory Leak Detected (S2, Completed)
10. Network Connectivity Issue (On Call, In Progress)

**Entries 11-20: P2 High Priority Issues**
11. Slow Query Performance (S1, Pending)
12. Disk Space Warning (S2, Completed)
13. CPU Usage High (S1, In Progress)
14. Memory Usage Alert (S2, Pending)
15. Backup Job Failed (On Call, Completed)
16. Log File Size Exceeded (S1, In Progress)
17. Service Restart Required (S2, Pending)
18. Configuration Mismatch (S1, Completed)
19. Dependency Update Available (S2, In Progress)
20. Security Patch Needed (On Call, Pending)

**Entries 21-30: P3/P4 Medium/Low Priority Issues**
21. Documentation Update Needed (S1, Completed)
22. Code Review Pending (S2, In Progress)
23. Test Coverage Low (S1, Pending)
24. Performance Optimization (S2, Completed)
25. Refactoring Required (On Call, In Progress)
26. Technical Debt Reduction (S1, Pending)
27. Monitoring Alert Tuning (S2, Completed)
28. Logging Enhancement (S1, In Progress)
29. Metrics Collection (S2, Pending)
30. Infrastructure Upgrade (On Call, Completed)

---

## Step 4: Verify Data in Excel

After adding entries through Form.html:

1. **Check Excel File**: `incident-tracker.xlsx`
2. **Verify Columns**: All 28 columns should be populated
3. **Verify Rows**: Should have 20 (original) + 30 (new) = 50 total rows
4. **Check Data**: Verify all fields are correctly populated

```bash
# Check Excel file exists
ls -la incident-tracker.xlsx
```

---

## Step 5: Refresh Dashboard

1. **Open Dashboard**: http://localhost:5000/dashboard.html
2. **Verify Data Loads**: Should show 50 total incidents
3. **Check KPI Metrics**:
   - Total Incidents: 50
   - By Category: Should show distribution of P1, P2, P3, P4
   - By Status: Should show distribution of Completed, In Progress, Pending
   - Avg MTTR: Should calculate correctly for completed incidents

---

## Step 6: Test Dashboard Features with New Data

### Test 1: Filters Work with New Data
- [ ] Apply Year filter → Shows correct incidents
- [ ] Apply Month filter → Shows correct incidents
- [ ] Apply Category filter → Shows correct incidents
- [ ] Apply Status filter → Shows correct incidents
- [ ] Combine multiple filters → Shows correct results

### Test 2: Charts Update with New Data
- [ ] Category chart shows updated distribution
- [ ] Status chart shows updated distribution
- [ ] Trends chart shows new data points
- [ ] MTTR Trend chart shows new data

### Test 3: Table Shows All 50 Incidents
- [ ] Pagination shows correct number of pages
- [ ] All 50 incidents visible when scrolling
- [ ] Sorting works on all columns
- [ ] Color-coded badges display correctly

### Test 4: Modal Shows All Details
- [ ] Click incident → Modal opens
- [ ] All 25 columns display correctly
- [ ] Print button works
- [ ] Edit button shows for In Progress/Pending

### Test 5: Edit and Save Works
- [ ] Find In Progress incident
- [ ] Click Edit → Edit form opens
- [ ] Change status to Completed
- [ ] Enter completion date/time
- [ ] Enter your name
- [ ] Click Save → Dashboard updates
- [ ] Verify MTTR calculated correctly

---

## Step 7: Verify Data in Admin.html

1. **Open Admin**: http://localhost:5000/admin.html
2. **Enter PIN**: 9999
3. **Verify Data**:
   - [ ] All 50 incidents visible
   - [ ] Can search incidents
   - [ ] Can filter by status/category
   - [ ] Can edit incidents
   - [ ] Can view audit log
   - [ ] Changes reflected in dashboard

---

## Step 8: Test Data Flow

### Flow: Form.html → Excel → Dashboard → Admin.html

1. **Add Entry in Form.html**
   - Fill all fields
   - Click Submit
   - Verify success message

2. **Check Excel**
   - Open incident-tracker.xlsx
   - Verify new entry in last row
   - Check all fields populated

3. **Check Dashboard**
   - Refresh dashboard
   - Verify new entry in table
   - Verify KPI metrics updated
   - Verify charts updated

4. **Check Admin.html**
   - Refresh admin
   - Verify new entry visible
   - Verify can edit entry
   - Verify changes reflected in dashboard

---

## Step 9: Test MTTR Calculation

### Scenario 1: Complete an In Progress Incident
1. Find incident with Status = "In Progress"
2. Click to open modal
3. Click Edit
4. Change Status to "Completed"
5. Enter Completed Date: [Today's date]
6. Enter Completed Time: [Current time]
7. Enter Last Edited By: Your name
8. Click Save
9. **Verify**: MTTR calculated and displayed correctly

### Scenario 2: Check MTTR in Dashboard
1. Open Dashboard
2. Look at KPI card "Avg MTTR"
3. Should show calculated average in "Xh Ym" format
4. Click incident with MTTR → Modal shows MTTR value

---

## Step 10: Verify CSV Export

1. **Open Dashboard**: http://localhost:5000/dashboard.html
2. **Click "📥 Export CSV"**
3. **Verify File**:
   - [ ] File downloads: incidents-YYYY-MM-DD.csv
   - [ ] File contains all 50 incidents
   - [ ] All 28 columns included
   - [ ] Data is correct

---

## Troubleshooting

### Entries Not Appearing in Dashboard
1. Check backend is running: `curl http://localhost:5000/api/health`
2. Check Excel file exists: `ls incident-tracker.xlsx`
3. Refresh dashboard: F5 or Ctrl+R
4. Check browser console (F12) for errors

### MTTR Not Calculating
1. Verify Created At field is populated
2. Verify Completed At field is populated
3. Check browser console for errors
4. Try different date/time format

### Data Not Flowing to Excel
1. Check Flask backend logs
2. Verify Excel file is not locked
3. Check file permissions
4. Restart Flask backend

### Admin.html Not Showing Data
1. Verify admin PIN is correct (9999)
2. Refresh page (F5)
3. Check backend is running
4. Check browser console for errors

---

## Success Criteria

✅ All 30 entries added successfully
✅ Data flows from Form.html to Excel
✅ Data displays in Dashboard (50 total incidents)
✅ Data displays in Admin.html
✅ Filters work with new data
✅ Charts update with new data
✅ MTTR calculates correctly
✅ Edit and Save works
✅ CSV export includes all data
✅ No console errors

---

## Expected Results After Adding 30 Entries

### Dashboard Metrics
- Total Incidents: 50
- By Category: P1=15, P2=15, P3=10, P4=10 (approximately)
- By Status: Completed=15, In Progress=15, Pending=20 (approximately)
- Avg MTTR: Should calculate based on completed incidents

### Table
- Shows 50 incidents total
- Pagination: 2 pages (25 per page)
- All columns populated
- Color-coded badges display

### Charts
- Category chart shows 4 bars (P1, P2, P3, P4)
- Status chart shows 3 segments (Completed, In Progress, Pending)
- Trends chart shows data points for each date
- MTTR Trend shows average MTTR per date

---

## Next Steps

1. ✅ Add 30 real entries through Form.html
2. ✅ Verify data in Excel
3. ✅ Verify data in Dashboard
4. ✅ Verify data in Admin.html
5. ✅ Test all features with new data
6. ✅ Document any issues
7. ✅ Fix any issues found
8. ✅ Deploy to production

---

## Time Estimate

- Adding 30 entries: 30-45 minutes
- Verifying in Excel: 5 minutes
- Testing Dashboard: 10 minutes
- Testing Admin.html: 5 minutes
- Testing features: 15 minutes
- **Total**: 1-1.5 hours

---

## Support

If you encounter issues:
1. Check browser console (F12)
2. Check Flask backend logs
3. Verify backend is running
4. Check Excel file is not locked
5. Restart Flask backend if needed

---

**Ready to test?** Start adding entries to Form.html now! 🚀

