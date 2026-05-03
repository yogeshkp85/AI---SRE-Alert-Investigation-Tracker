# How to Test Team Member Management

## Quick Start

### 1. Verify Backend is Running
```
http://localhost:5000/api/health
```
Should return: `{"status": "ok", ...}`

### 2. Open Admin Panel
```
http://localhost:5000/admin.html
```

### 3. Login
- PIN: `9999`
- Click "Login"

---

## Test Scenarios

### Scenario 1: Add Team Member

**Steps:**
1. Click "Team Members" tab
2. Click "Add Team Member" button
3. Fill in:
   - Name: `Test User 001`
   - Email: `test001@example.com`
   - Phone: `9876543210`
4. Click "Add Member"

**Expected Result:**
- ✅ Green success message appears
- ✅ New member appears in table
- ✅ Modal closes automatically

**Verify Persistence:**
1. Refresh the page
2. Go to Team Members tab
3. New member should still be there

---

### Scenario 2: Edit Team Member

**Steps:**
1. Click "Team Members" tab
2. Find "Test User 001" in table
3. Click "Edit" button
4. Modify:
   - Name: `Test User 001 Updated`
   - Email: `test001-updated@example.com`
   - Phone: `9876543211`
5. Click "Update Member"

**Expected Result:**
- ✅ Green success message appears
- ✅ Changes appear in table immediately
- ✅ Modal closes automatically

**Verify Changes:**
1. Refresh the page
2. Go to Team Members tab
3. Updated member should show new values

---

### Scenario 3: Delete Team Member

**Steps:**
1. Click "Team Members" tab
2. Find "Test User 001 Updated" in table
3. Click "Delete" button
4. Confirm deletion

**Expected Result:**
- ✅ Green success message appears
- ✅ Member removed from table
- ✅ Modal closes automatically

**Verify Deletion:**
1. Refresh the page
2. Go to Team Members tab
3. Member should be gone

---

### Scenario 4: Verify Form Shows Team Members

**Steps:**
1. Open Form: `http://localhost:5000/form.html`
2. Look for "Assigned To" dropdown
3. Click dropdown

**Expected Result:**
- ✅ All 18 team members appear
- ✅ List is alphabetically sorted
- ✅ No duplicates

---

### Scenario 5: Verify Dashboard Shows Team Members

**Steps:**
1. Open Dashboard: `http://localhost:5000/dashboard.html`
2. Look for incident dropdowns
3. Click "Assigned To" dropdown

**Expected Result:**
- ✅ All 18 team members appear
- ✅ List is alphabetically sorted
- ✅ No duplicates

---

### Scenario 6: Add Member and Verify in Form

**Steps:**
1. Go to Admin Panel
2. Add new team member: `New Test Member`
3. Go to Form
4. Click "Assigned To" dropdown

**Expected Result:**
- ✅ New member appears in dropdown
- ✅ No need to refresh
- ✅ Changes are immediate

---

### Scenario 7: Add Member and Verify in Dashboard

**Steps:**
1. Go to Admin Panel
2. Add new team member: `Another Test Member`
3. Go to Dashboard
4. Click incident dropdown

**Expected Result:**
- ✅ New member appears in dropdown
- ✅ No need to refresh
- ✅ Changes are immediate

---

## Troubleshooting

### Issue: Team members not appearing in Form/Dashboard
**Solution:**
1. Check backend is running: `http://localhost:5000/api/health`
2. Check browser console (F12 → Console)
3. Look for error messages
4. Restart backend if needed

### Issue: Add/Edit/Delete not working
**Solution:**
1. Verify you're logged in (PIN: 9999)
2. Check browser console for errors
3. Check that Excel file is not locked
4. Try refreshing the page

### Issue: Changes not persisting after refresh
**Solution:**
1. Check Excel file is not locked
2. Check file permissions
3. Verify Sheet2 exists in Excel
4. Restart backend

### Issue: Modal not closing after operation
**Solution:**
1. Check browser console for errors
2. Try clicking X button to close manually
3. Refresh page
4. Try operation again

---

## Expected Team Members (18 Total)

1. Raj Kumar
2. Priya Singh
3. Amit Patel
4. Vikram Joshi
5. Neha Sharma
6. Rohan Verma
7. Anjali Menon
8. Arjun Gupta
9. Deepak Kumar
10. Pooja Nair
11. Sanjay Reddy
12. Tina Desai
13. Varun Malhotra
14. Yash Pandey
15. Zara Khan
16. Aditya Rao
17. Manager A
18. Manager B

---

## Success Criteria

✅ All team members appear in Form dropdown  
✅ All team members appear in Dashboard dropdown  
✅ Can add new team member in admin panel  
✅ New member appears in Form/Dashboard immediately  
✅ Can edit team member in admin panel  
✅ Changes appear in Form/Dashboard immediately  
✅ Can delete team member in admin panel  
✅ Deleted member removed from Form/Dashboard immediately  
✅ Changes persist after page refresh  
✅ Changes persist after app restart  

---

## Test Checklist

- [ ] Backend is running and responding to health check
- [ ] Admin panel loads and login works
- [ ] Team Members tab shows 18 members
- [ ] Can add new team member
- [ ] New member appears in table
- [ ] New member appears in Form dropdown
- [ ] New member appears in Dashboard dropdown
- [ ] Can edit team member
- [ ] Changes appear in table
- [ ] Changes appear in Form dropdown
- [ ] Changes appear in Dashboard dropdown
- [ ] Can delete team member
- [ ] Deleted member removed from table
- [ ] Deleted member removed from Form dropdown
- [ ] Deleted member removed from Dashboard dropdown
- [ ] Changes persist after page refresh
- [ ] Changes persist after app restart

---

## Admin Panel URLs

- **Admin Panel**: http://localhost:5000/admin.html
- **Form**: http://localhost:5000/form.html
- **Dashboard**: http://localhost:5000/dashboard.html
- **Health Check**: http://localhost:5000/api/health

---

## Admin Credentials

- **PIN**: `9999`

---

## Support

If you encounter any issues:
1. Check browser console (F12 → Console)
2. Check backend logs
3. Verify Excel file is not locked
4. Try restarting the backend
5. Check that Sheet2 exists in Excel file

---

**Status**: ✅ Ready for Testing

All functionality has been implemented and tested. Follow the scenarios above to verify everything works correctly.
