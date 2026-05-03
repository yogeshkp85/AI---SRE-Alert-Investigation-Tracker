# Quick Dashboard Testing Instructions

## 🚀 Quick Start (5 minutes)

### Step 1: Verify Backend is Running
```bash
# Check if Flask is running
curl http://localhost:5000/api/health
# Should return: {"status":"ok","timestamp":"..."}
```

### Step 2: Open Dashboard
Open this URL in your browser:
```
http://localhost:5000/dashboard.html
```

### Step 3: Quick Smoke Test (5 minutes)

#### Test 1: Dashboard Loads ✅
- [ ] Page loads without errors
- [ ] See "📊 Incident Dashboard" header
- [ ] Status shows "● Live"
- [ ] All sections visible

#### Test 2: KPI Metrics Display ✅
- [ ] Total Incidents: 20
- [ ] By Category: P1=5, P2=4, P3=6, P4=5
- [ ] By Status: Completed=7, In Progress=6, Pending=7
- [ ] Avg MTTR: "--" (no data yet)

#### Test 3: Filters Work ✅
- [ ] Click Category dropdown → Select "P1"
- [ ] Table updates to show only P1 incidents (5 rows)
- [ ] Incident count shows "5 of 20"
- [ ] Click "🔄 Clear All" → Table shows all 20 incidents

#### Test 4: Modal Opens ✅
- [ ] Click any incident row
- [ ] Modal appears with "Incident Details"
- [ ] See all sections: Basic Info, Incident Details, Reference, Communication, Status, Additional
- [ ] Print button visible
- [ ] Close button (X) works

#### Test 5: Print Works ✅
- [ ] Modal open
- [ ] Click "🖨️ Print" button
- [ ] Print dialog opens
- [ ] Preview shows formatted incident report
- [ ] Click "Cancel" to close

#### Test 6: Edit Works (In Progress/Pending) ✅
- [ ] Find incident with Status = "In Progress" or "Pending"
- [ ] Click to open modal
- [ ] Click "✏️ Edit" button
- [ ] Edit form opens with fields:
  - Status (dropdown)
  - Completed Date (date input)
  - Completed Time (time input)
  - Last Edited By (text input)
- [ ] Click "❌ Cancel" to close

#### Test 7: Save Works ✅
- [ ] Open edit form for In Progress incident
- [ ] Change Status to "Pending"
- [ ] Enter your name in "Last Edited By"
- [ ] Click "💾 Save Changes"
- [ ] Alert shows: "✅ Incident updated successfully!"
- [ ] Modal closes
- [ ] Dashboard updates (status changed in table)

#### Test 8: Edit Hidden for Completed ✅
- [ ] Find incident with Status = "Completed"
- [ ] Click to open modal
- [ ] Edit button NOT visible
- [ ] Only Print button visible

#### Test 9: Charts Update ✅
- [ ] Apply filter (e.g., Category = P1)
- [ ] Charts update to show filtered data
- [ ] All 4 charts visible and rendering

#### Test 10: CSV Export ✅
- [ ] Click "📥 Export CSV" button
- [ ] File downloads: "incidents-YYYY-MM-DD.csv"
- [ ] Open file in Excel/spreadsheet
- [ ] Verify data is correct

---

## 📋 Detailed Test Scenarios

### Scenario 1: Complete an Incident
1. Find incident with Status = "In Progress"
2. Click to open modal
3. Click "✏️ Edit"
4. Change Status to "Completed"
5. Enter Completed Date: 2026-05-03
6. Enter Completed Time: 14:30
7. Enter Last Edited By: Your Name
8. Click "💾 Save Changes"
9. Verify:
   - Alert shows success
   - Modal closes
   - Table shows new status
   - KPI metrics update (In Progress -1, Completed +1)

### Scenario 2: Filter and Export
1. Apply Year = 2026
2. Apply Category = P1
3. Apply Status = Pending
4. Verify table shows filtered results
5. Click "📥 Export CSV"
6. Verify file contains only filtered incidents

### Scenario 3: Print Multiple Incidents
1. Click incident 1 → Print → Cancel
2. Click incident 2 → Print → Cancel
3. Click incident 3 → Print → Cancel
4. Verify all print dialogs work correctly

### Scenario 4: Edit Multiple Incidents
1. Edit incident 1 (change status)
2. Edit incident 2 (change status)
3. Verify both updated correctly
4. Verify dashboard reflects all changes

---

## 🎯 Success Criteria

### All Tests Pass If:
- ✅ Dashboard loads without errors
- ✅ All filters work correctly
- ✅ Modal displays all 25 columns
- ✅ Print button opens print dialog
- ✅ Edit button shows only for In Progress/Pending
- ✅ Save updates incident and refreshes dashboard
- ✅ Charts update on filter change
- ✅ CSV export works
- ✅ No console errors
- ✅ Responsive design works

---

## 🐛 Troubleshooting

### Dashboard Won't Load
```bash
# Check backend
curl http://localhost:5000/api/health

# If not running, start Flask
python app.py
```

### No Incidents Showing
```bash
# Check API
curl http://localhost:5000/api/incidents

# Should return 20 incidents
```

### Print Dialog Won't Open
- Check browser console (F12)
- Verify no JavaScript errors
- Try different browser

### Edit Button Not Showing
- Verify incident status is "In Progress" or "Pending"
- Check browser console for errors
- Try refreshing page

### Save Not Working
- Verify "Last Edited By" field is filled
- Check browser console for errors
- Verify backend is running

---

## 📊 Test Data

### Available Incidents
- Total: 20
- By Status:
  - Completed: 7 (not editable)
  - In Progress: 6 (editable)
  - Pending: 7 (editable)
- By Category:
  - P1: 5
  - P2: 4
  - P3: 6
  - P4: 5

### Editable Incidents
- Total editable: 13 (In Progress + Pending)
- Sample RITMs: INC1003, INC1004, INC1006, etc.

---

## 🔗 URLs

| Page | URL |
|------|-----|
| Dashboard | http://localhost:5000/dashboard.html |
| Form | http://localhost:5000/form.html |
| Admin | http://localhost:5000/admin.html |
| API Health | http://localhost:5000/api/health |
| API Incidents | http://localhost:5000/api/incidents |

---

## 📝 Test Checklist

### Basic Functionality
- [ ] Dashboard loads
- [ ] KPI metrics display
- [ ] Filters work
- [ ] Modal opens
- [ ] Print works
- [ ] Edit works
- [ ] Save works
- [ ] Dashboard updates

### Advanced Features
- [ ] Charts update on filter
- [ ] CSV export works
- [ ] Multiple filters combined
- [ ] Edit multiple incidents
- [ ] MTTR calculation works
- [ ] Last Modified fields update

### Edge Cases
- [ ] Edit button hidden for Completed
- [ ] Edit button shown for In Progress/Pending
- [ ] Save requires Last Edited By
- [ ] Print works after edit
- [ ] Dashboard auto-refreshes

### Browser Compatibility
- [ ] Chrome works
- [ ] Firefox works
- [ ] Safari works
- [ ] Edge works

---

## 🎉 Expected Results

### After Completing All Tests:
✅ All 10 quick tests pass
✅ All 4 detailed scenarios work
✅ All success criteria met
✅ No console errors
✅ Dashboard is production-ready

---

## 📞 Support

If you encounter issues:
1. Check browser console (F12)
2. Verify backend is running
3. Check API health: http://localhost:5000/api/health
4. Review MANUAL_TESTING_GUIDE.md for detailed tests
5. Check DASHBOARD_CURRENT_STATUS.md for implementation details

---

## ⏱️ Time Estimates

- Quick Smoke Test: 5 minutes
- Detailed Scenarios: 10 minutes
- Full Manual Testing: 30-45 minutes
- Browser Compatibility: 15 minutes per browser

**Total Time**: 1-2 hours for complete testing

---

## 🚀 Next Steps

1. ✅ Run Quick Smoke Test (5 min)
2. ✅ Run Detailed Scenarios (10 min)
3. ✅ Run Full Manual Testing (30-45 min)
4. ✅ Test Browser Compatibility (15 min per browser)
5. ✅ Document any issues
6. ✅ Fix issues if needed
7. ✅ Deploy to production

---

**Status**: ✅ **READY FOR TESTING**

Open http://localhost:5000/dashboard.html now and start testing!

