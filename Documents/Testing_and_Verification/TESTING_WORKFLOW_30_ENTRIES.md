# 📋 Testing Workflow: 30 Real Entries

## Overview
This document provides step-by-step instructions for adding 30 real entries through Form.html and verifying the complete workflow.

---

## Pre-Testing Checklist

- [ ] Backend running: http://localhost:5000/api/health
- [ ] Excel file exists: `incident-tracker.xlsx`
- [ ] All three HTML files updated (Dashboard, Form, Admin)
- [ ] Browser cache cleared
- [ ] Multiple browsers available for testing

---

## Part 1: Adding 30 Entries via Form.html

### Access Form
1. Open browser
2. Navigate to: **http://localhost:5000/form.html**
3. You should see the form with PIN authentication

### PIN Authentication
- **Early Shift (S1)**: PIN 1111
- **Main Shift (S2)**: PIN 2222
- **Night Shift (On Call)**: PIN 3333

### Entry Template

Each entry requires:
- Date (YYYY-MM-DD)
- Shift (S1, S2, On Call)
- Incident Category (P1, P2, P3, P4)
- Shift Lead (Team member name)
- Time Slot (Dropdown based on shift)
- Alert Report Time (HH:MM)
- Alert Description (Text)
- Assigned To (Team member)
- Status (Pending, In Progress, Completed)

### 30 Test Entries

#### Batch 1: April 17, 2026 (Shift S1 - PIN 1111)

**Entry 1**
- Date: 2026-04-17
- Shift: S1
- Category: P1
- Shift Lead: Raj Kumar
- Time Slot: 7-8 AM
- Alert Time: 07:15
- Alert: Payment gateway timeout - customers unable to complete transactions
- Assigned To: Raj Kumar
- Status: Completed

**Entry 2**
- Date: 2026-04-17
- Shift: S1
- Category: P2
- Shift Lead: Priya Singh
- Time Slot: 8-9 AM
- Alert Time: 08:30
- Alert: Database connection pool exhausted - slow query performance
- Assigned To: Priya Singh
- Status: In Progress

**Entry 3**
- Date: 2026-04-17
- Shift: S1
- Category: P3
- Shift Lead: Amit Patel
- Time Slot: 9-10 AM
- Alert Time: 09:45
- Alert: API response time exceeding SLA - 5 second delay
- Assigned To: Amit Patel
- Status: Pending

**Entry 4**
- Date: 2026-04-17
- Shift: S1
- Category: P4
- Shift Lead: Vikram Joshi
- Time Slot: 10-11 AM
- Alert Time: 10:20
- Alert: Minor UI glitch in dashboard - button styling issue
- Assigned To: Vikram Joshi
- Status: Completed

#### Batch 2: April 17, 2026 (Shift S2 - PIN 2222)

**Entry 5**
- Date: 2026-04-17
- Shift: S2
- Category: P1
- Shift Lead: Neha Sharma
- Time Slot: 11-12 PM
- Alert Time: 11:30
- Alert: Transaction processing failed - batch job error
- Assigned To: Neha Sharma
- Status: In Progress

**Entry 6**
- Date: 2026-04-17
- Shift: S2
- Category: P2
- Shift Lead: Rohan Verma
- Time Slot: 12-1 PM
- Alert Time: 12:45
- Alert: Email notification service not responding
- Assigned To: Rohan Verma
- Status: Pending

**Entry 7**
- Date: 2026-04-17
- Shift: S2
- Category: P3
- Shift Lead: Anjali Menon
- Time Slot: 1-2 PM
- Alert Time: 13:15
- Alert: Cache invalidation issue - stale data served
- Assigned To: Anjali Menon
- Status: Completed

**Entry 8**
- Date: 2026-04-17
- Shift: S2
- Category: P4
- Shift Lead: Arjun Gupta
- Time Slot: 2-3 PM
- Alert Time: 14:00
- Alert: Log file size exceeded - disk space warning
- Assigned To: Arjun Gupta
- Status: In Progress

#### Batch 3: April 17, 2026 (Shift On Call - PIN 3333)

**Entry 9**
- Date: 2026-04-17
- Shift: On Call
- Category: P1
- Shift Lead: Deepak Kumar
- Time Slot: 10 PM-7 AM
- Alert Time: 22:30
- Alert: Critical system outage - all services down
- Assigned To: Deepak Kumar
- Status: Completed

**Entry 10**
- Date: 2026-04-17
- Shift: On Call
- Category: P2
- Shift Lead: Pooja Nair
- Time Slot: 10 PM-7 AM
- Alert Time: 23:15
- Alert: Memory leak detected in production - heap size growing
- Assigned To: Pooja Nair
- Status: Pending

#### Batch 4: April 18, 2026 (Shift S1 - PIN 1111)

**Entry 11**
- Date: 2026-04-18
- Shift: S1
- Category: P1
- Shift Lead: Sanjay Reddy
- Time Slot: 7-8 AM
- Alert Time: 07:00
- Alert: Payment reconciliation error - 500 transactions unmatched
- Assigned To: Sanjay Reddy
- Status: In Progress

**Entry 12**
- Date: 2026-04-18
- Shift: S1
- Category: P2
- Shift Lead: Tina Desai
- Time Slot: 8-9 AM
- Alert Time: 08:20
- Alert: SSL certificate expiring in 7 days - renewal required
- Assigned To: Tina Desai
- Status: Completed

**Entry 13**
- Date: 2026-04-18
- Shift: S1
- Category: P3
- Shift Lead: Varun Malhotra
- Time Slot: 9-10 AM
- Alert Time: 09:30
- Alert: Backup job failed - retry scheduled
- Assigned To: Varun Malhotra
- Status: Pending

**Entry 14**
- Date: 2026-04-18
- Shift: S1
- Category: P4
- Shift Lead: Yash Pandey
- Time Slot: 10-11 AM
- Alert Time: 10:45
- Alert: Documentation outdated - API version mismatch
- Assigned To: Yash Pandey
- Status: Completed

#### Batch 5: April 18, 2026 (Shift S2 - PIN 2222)

**Entry 15**
- Date: 2026-04-18
- Shift: S2
- Category: P1
- Shift Lead: Zara Khan
- Time Slot: 11-12 PM
- Alert Time: 11:00
- Alert: Database replication lag - 30 second delay
- Assigned To: Zara Khan
- Status: In Progress

**Entry 16**
- Date: 2026-04-18
- Shift: S2
- Category: P2
- Shift Lead: Aditya Rao
- Time Slot: 12-1 PM
- Alert Time: 12:30
- Alert: Load balancer misconfigured - uneven traffic distribution
- Assigned To: Aditya Rao
- Status: Pending

**Entry 17**
- Date: 2026-04-18
- Shift: S2
- Category: P3
- Shift Lead: Raj Kumar
- Time Slot: 1-2 PM
- Alert Time: 13:45
- Alert: Monitoring alert threshold exceeded - CPU at 85%
- Assigned To: Raj Kumar
- Status: Completed

**Entry 18**
- Date: 2026-04-18
- Shift: S2
- Category: P4
- Shift Lead: Priya Singh
- Time Slot: 2-3 PM
- Alert Time: 14:15
- Alert: Code review pending - 3 PRs awaiting approval
- Assigned To: Priya Singh
- Status: In Progress

#### Batch 6: April 18, 2026 (Shift On Call - PIN 3333)

**Entry 19**
- Date: 2026-04-18
- Shift: On Call
- Category: P1
- Shift Lead: Amit Patel
- Time Slot: 10 PM-7 AM
- Alert Time: 01:00
- Alert: Network connectivity issue - packet loss 15%
- Assigned To: Amit Patel
- Status: Completed

**Entry 20**
- Date: 2026-04-18
- Shift: On Call
- Category: P2
- Shift Lead: Vikram Joshi
- Time Slot: 10 PM-7 AM
- Alert Time: 02:30
- Alert: Firewall rule blocking traffic - port 443 blocked
- Assigned To: Vikram Joshi
- Status: Pending

#### Batch 7: April 19, 2026 (Shift S1 - PIN 1111)

**Entry 21**
- Date: 2026-04-19
- Shift: S1
- Category: P1
- Shift Lead: Neha Sharma
- Time Slot: 7-8 AM
- Alert Time: 07:30
- Alert: Transaction timeout - 2 minute processing delay
- Assigned To: Neha Sharma
- Status: In Progress

**Entry 22**
- Date: 2026-04-19
- Shift: S1
- Category: P2
- Shift Lead: Rohan Verma
- Time Slot: 8-9 AM
- Alert Time: 08:45
- Alert: API rate limit exceeded - 10000 requests/min threshold
- Assigned To: Rohan Verma
- Status: Completed

**Entry 23**
- Date: 2026-04-19
- Shift: S1
- Category: P3
- Shift Lead: Anjali Menon
- Time Slot: 9-10 AM
- Alert Time: 09:15
- Alert: Disk space low - 85% utilization on /var
- Assigned To: Anjali Menon
- Status: Pending

**Entry 24**
- Date: 2026-04-19
- Shift: S1
- Category: P4
- Shift Lead: Arjun Gupta
- Time Slot: 10-11 AM
- Alert Time: 10:30
- Alert: Test environment down - deployment failed
- Assigned To: Arjun Gupta
- Status: Completed

#### Batch 8: April 19, 2026 (Shift S2 - PIN 2222)

**Entry 25**
- Date: 2026-04-19
- Shift: S2
- Category: P1
- Shift Lead: Deepak Kumar
- Time Slot: 11-12 PM
- Alert Time: 11:45
- Alert: Production deployment failed - rollback initiated
- Assigned To: Deepak Kumar
- Status: In Progress

**Entry 26**
- Date: 2026-04-19
- Shift: S2
- Category: P2
- Shift Lead: Pooja Nair
- Time Slot: 12-1 PM
- Alert Time: 12:15
- Alert: Rollback required - version mismatch detected
- Assigned To: Pooja Nair
- Status: Pending

**Entry 27**
- Date: 2026-04-19
- Shift: S2
- Category: P3
- Shift Lead: Sanjay Reddy
- Time Slot: 1-2 PM
- Alert Time: 13:30
- Alert: Performance degradation - response time 3x normal
- Assigned To: Sanjay Reddy
- Status: Completed

**Entry 28**
- Date: 2026-04-19
- Shift: S2
- Category: P4
- Shift Lead: Tina Desai
- Time Slot: 2-3 PM
- Alert Time: 14:45
- Alert: Security patch pending - CVE-2026-1234 critical
- Assigned To: Tina Desai
- Status: In Progress

#### Batch 9: April 19, 2026 (Shift On Call - PIN 3333)

**Entry 29**
- Date: 2026-04-19
- Shift: On Call
- Category: P1
- Shift Lead: Varun Malhotra
- Time Slot: 10 PM-7 AM
- Alert Time: 03:00
- Alert: Data corruption detected - database integrity check failed
- Assigned To: Varun Malhotra
- Status: Completed

**Entry 30**
- Date: 2026-04-19
- Shift: On Call
- Category: P2
- Shift Lead: Yash Pandey
- Time Slot: 10 PM-7 AM
- Alert Time: 04:15
- Alert: Compliance violation - PCI DSS audit failed
- Assigned To: Yash Pandey
- Status: Pending

---

## Part 2: Verify Data in Excel

### Steps
1. Open `incident-tracker.xlsx`
2. Check Sheet1 has 30 data rows (plus header)
3. Verify columns:
   - Date
   - Shift
   - Incident Category
   - Shift Lead
   - Time Slot
   - Alert Report Time
   - Alert
   - Assigned To
   - Status
   - And other columns

### Expected Results
- Total rows: 31 (1 header + 30 data)
- All data populated
- No truncation
- Proper formatting

---

## Part 3: Verify Dashboard

### Access Dashboard
1. Open: **http://localhost:5000/dashboard.html**
2. Wait for data to load (10 seconds max)

### Verify Metrics
- [ ] Total Incidents: 30
- [ ] P1 Count: 6
- [ ] P2 Count: 8
- [ ] P3 Count: 8
- [ ] P4 Count: 8
- [ ] Completed: 10
- [ ] In Progress: 10
- [ ] Pending: 10

### Verify Filters
- [ ] Year filter works
- [ ] Month filter works
- [ ] Date filter works
- [ ] Person filter works
- [ ] Shift Lead filter works
- [ ] Shift filter works
- [ ] Category filter works
- [ ] Status filter works
- [ ] Clear All button works

### Verify Charts
- [ ] Category chart displays (6, 8, 8, 8)
- [ ] Status chart displays (10, 10, 10)
- [ ] Trends chart displays
- [ ] MTTR chart displays

### Verify Table
- [ ] All 30 rows display
- [ ] Pagination shows 2 pages
- [ ] Sorting works on all columns
- [ ] Modal opens on row click
- [ ] Modal displays all fields

### Verify Features
- [ ] Auto-refresh works (10 second countdown)
- [ ] CSV export works
- [ ] Responsive on mobile
- [ ] No console errors

---

## Part 4: Verify Admin Panel

### Access Admin
1. Open: **http://localhost:5000/admin.html**
2. Enter PIN: **9999**
3. Click Login

### Verify Incidents Tab
- [ ] All 30 incidents display
- [ ] Edit button works
- [ ] Delete button works
- [ ] Changes reflected in Dashboard

### Test Edit Functionality
1. Click Edit on first incident
2. Change Status to "Completed"
3. Click Save
4. Verify change in Dashboard

### Test Delete Functionality
1. Click Delete on last incident
2. Confirm deletion
3. Verify incident removed from Dashboard
4. Verify count decreased to 29

### Verify Team Members Tab
- [ ] Team members display
- [ ] Add member works
- [ ] Edit member works
- [ ] Delete member works

### Verify Audit Log Tab
- [ ] Audit entries display
- [ ] Shows timestamp, user, action
- [ ] Shows incident ID
- [ ] Shows field changed

---

## Part 5: Cross-Browser Testing

### Test on Each Browser

#### Chrome/Chromium
1. Open all three URLs
2. Verify layout correct
3. Verify colors correct (black background, white text)
4. Verify functionality works
5. Check console for errors

#### Microsoft Edge
1. Open all three URLs
2. Verify layout correct
3. Verify colors correct
4. Verify functionality works
5. Check console for errors

#### Firefox
1. Open all three URLs
2. Verify layout correct
3. Verify colors correct
4. Verify functionality works
5. Check console for errors

#### Safari
1. Open all three URLs
2. Verify layout correct
3. Verify colors correct
4. Verify functionality works
5. Check console for errors

#### Chrome Mobile (Android)
1. Open all three URLs
2. Verify responsive layout
3. Verify touch interactions work
4. Verify text readable
5. Verify no horizontal scroll

#### Safari Mobile (iOS)
1. Open all three URLs
2. Verify responsive layout
3. Verify touch interactions work
4. Verify text readable
5. Verify no horizontal scroll

---

## Part 6: Performance Testing

### Dashboard Performance
- [ ] Loads in < 2 seconds
- [ ] Filters apply in < 500ms
- [ ] Charts render in < 1 second
- [ ] Auto-refresh doesn't lag
- [ ] No memory leaks

### Form Performance
- [ ] Loads in < 1 second
- [ ] Submission completes in < 2 seconds
- [ ] No lag on input

### Admin Performance
- [ ] Loads in < 1 second
- [ ] Edit modal opens in < 500ms
- [ ] Save completes in < 2 seconds

---

## Expected Final Results

### Dashboard
```
Total Incidents: 30
Category: P1=6, P2=8, P3=8, P4=8
Status: Completed=10, In Progress=10, Pending=10
Average MTTR: ~2-3 hours
```

### Excel
```
Rows: 31 (1 header + 30 data)
Columns: 27 (all populated)
Data Integrity: 100%
```

### Admin
```
Incidents: 30 (or 29 if 1 deleted)
Team Members: 16
Audit Entries: Multiple (edit, delete actions)
```

---

## Troubleshooting

### Form not submitting
- Check backend running
- Verify PIN correct
- Check all required fields filled
- Check browser console

### Dashboard showing no data
- Refresh page (Ctrl+F5)
- Check Excel file exists
- Verify backend API responding
- Check browser console

### Admin edit not working
- Verify PIN correct (9999)
- Check backend running
- Verify incident exists
- Check browser console

### Mobile display issues
- Clear browser cache
- Disable zoom
- Rotate device
- Try different browser

---

## Sign-Off Checklist

- [ ] All 30 entries added successfully
- [ ] Excel file contains all 30 entries
- [ ] Dashboard displays correct metrics
- [ ] All filters working
- [ ] Charts rendering correctly
- [ ] Admin edit/delete working
- [ ] Cross-browser testing complete
- [ ] Performance acceptable
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Ready for Phase 2 review

---

## Next Steps

After completing all testing:
1. Document any issues found
2. Fix any bugs discovered
3. Optimize performance if needed
4. Prepare for Phase 2 review
5. Plan Phase 2 implementation

---

**Status**: READY FOR TESTING

