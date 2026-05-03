#!/usr/bin/env python3
"""
Test Team Member Management from Excel Sheet2
Tests Add, Edit, Delete operations and verifies they persist in Excel
"""

import requests
import json
from datetime import datetime

BASE_URL = 'http://localhost:5000'
ADMIN_PIN = '9999'

# Session to maintain cookies
session = requests.Session()

print("\n" + "="*80)
print("🧪 TEAM MEMBER MANAGEMENT TESTING (EXCEL SHEET2)")
print("="*80)

# TEST 1: Admin Login
print("\n[TEST 1] Admin Login")
print("-" * 80)
try:
    response = session.post(f'{BASE_URL}/api/admin/login', 
        json={'pin': ADMIN_PIN},
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ PASS: Admin login successful")
    else:
        print("❌ FAIL: Admin login failed")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 2: Get Team Members
print("\n[TEST 2] Get Team Members (Admin)")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/admin/teams',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Team Members Count: {len(data.get('members', []))}")
    
    if response.status_code == 200 and data.get('members'):
        print("✅ PASS: Team members retrieved successfully")
        print(f"Sample members:")
        for member in data['members'][:3]:
            print(f"  - {member['name']} | {member['email']} | {member['phone']}")
    else:
        print("❌ FAIL: Could not retrieve team members")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 3: Add Team Member
print("\n[TEST 3] Add Team Member")
print("-" * 80)
try:
    new_member = {
        'name': 'Test Member 001',
        'email': 'test001@example.com',
        'phone': '9876543210'
    }
    
    response = session.post(f'{BASE_URL}/api/admin/teams',
        json=new_member,
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 201:
        print("✅ PASS: Team member added successfully")
        test_member_name = new_member['name']
    else:
        print("❌ FAIL: Could not add team member")
        test_member_name = None
except Exception as e:
    print(f"❌ ERROR: {e}")
    test_member_name = None

# TEST 4: Verify Member Added (Get Team Members Again)
print("\n[TEST 4] Verify Member Added")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/admin/teams',
        headers={'Content-Type': 'application/json'})
    
    data = response.json()
    members = data.get('members', [])
    
    # Check if new member is in the list
    found = any(m['name'] == test_member_name for m in members)
    
    print(f"Status Code: {response.status_code}")
    print(f"Total Members: {len(members)}")
    print(f"New Member Found: {found}")
    
    if found:
        print("✅ PASS: New member appears in team list")
    else:
        print("❌ FAIL: New member not found in team list")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 5: Update Team Member
print("\n[TEST 5] Update Team Member")
print("-" * 80)
if test_member_name:
    try:
        updated_member = {
            'name': 'Test Member 001 Updated',
            'email': 'test001-updated@example.com',
            'phone': '9876543211'
        }
        
        response = session.put(f'{BASE_URL}/api/admin/teams/{test_member_name}',
            json=updated_member,
            headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ PASS: Team member updated successfully")
            test_member_name = updated_member['name']  # Update for next test
        else:
            print("❌ FAIL: Could not update team member")
    except Exception as e:
        print(f"❌ ERROR: {e}")
else:
    print("⏭️  SKIPPED: No member to update (previous test failed)")

# TEST 6: Verify Member Updated
print("\n[TEST 6] Verify Member Updated")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/admin/teams',
        headers={'Content-Type': 'application/json'})
    
    data = response.json()
    members = data.get('members', [])
    
    # Find the updated member
    updated = next((m for m in members if m['name'] == test_member_name), None)
    
    print(f"Status Code: {response.status_code}")
    if updated:
        print(f"Updated Member: {updated['name']}")
        print(f"  Email: {updated['email']}")
        print(f"  Phone: {updated['phone']}")
        print("✅ PASS: Member update verified")
    else:
        print("❌ FAIL: Updated member not found")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 7: Delete Team Member
print("\n[TEST 7] Delete Team Member")
print("-" * 80)
if test_member_name:
    try:
        response = session.delete(f'{BASE_URL}/api/admin/teams/{test_member_name}',
            headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ PASS: Team member deleted successfully")
        else:
            print("❌ FAIL: Could not delete team member")
    except Exception as e:
        print(f"❌ ERROR: {e}")
else:
    print("⏭️  SKIPPED: No member to delete (previous test failed)")

# TEST 8: Verify Member Deleted
print("\n[TEST 8] Verify Member Deleted")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/admin/teams',
        headers={'Content-Type': 'application/json'})
    
    data = response.json()
    members = data.get('members', [])
    
    # Check if deleted member is gone
    found = any(m['name'] == test_member_name for m in members if m['name'])
    
    print(f"Status Code: {response.status_code}")
    print(f"Total Members: {len(members)}")
    print(f"Deleted Member Still Found: {found}")
    
    if not found:
        print("✅ PASS: Deleted member removed from team list")
    else:
        print("❌ FAIL: Deleted member still in team list")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 9: Get Team Members (Form/Dashboard)
print("\n[TEST 9] Get Team Members (Form/Dashboard)")
print("-" * 80)
try:
    response = requests.get(f'{BASE_URL}/api/teams',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    
    if response.status_code == 200:
        print(f"Team Members: {len(data.get('members', []))}")
        print("✅ PASS: Team members available for form/dashboard")
        print(f"Sample members: {data.get('members', [])[:3]}")
    else:
        print("❌ FAIL: Could not retrieve team members")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 10: Admin Logout
print("\n[TEST 10] Admin Logout")
print("-" * 80)
try:
    response = session.post(f'{BASE_URL}/api/admin/logout',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ PASS: Admin logout successful")
    else:
        print("❌ FAIL: Admin logout failed")
except Exception as e:
    print(f"❌ ERROR: {e}")

print("\n" + "="*80)
print("🧪 TESTING COMPLETE")
print("="*80 + "\n")
