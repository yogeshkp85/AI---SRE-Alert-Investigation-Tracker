#!/usr/bin/env python3
"""
Comprehensive Admin Panel Testing Script
Tests all admin features: Login, Team Member Add/Edit/Delete, Incident Add/Edit/Delete
"""

import requests
import json
from datetime import datetime

BASE_URL = 'http://localhost:5000'
ADMIN_PIN = '9999'

# Session to maintain cookies
session = requests.Session()

print("\n" + "="*80)
print("🧪 COMPREHENSIVE ADMIN PANEL TESTING")
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
        print(f"Sample members: {data['members'][:3]}")
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
        'shift': 'S1',
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
    else:
        print("❌ FAIL: Could not add team member")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 4: Update Team Member
print("\n[TEST 4] Update Team Member")
print("-" * 80)
try:
    updated_member = {
        'name': 'Test Member 001 Updated',
        'shift': 'S2',
        'email': 'test001-updated@example.com',
        'phone': '9876543211'
    }
    
    response = session.put(f'{BASE_URL}/api/admin/teams/Test%20Member%20001',
        json=updated_member,
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ PASS: Team member updated successfully")
    else:
        print("❌ FAIL: Could not update team member")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 5: Delete Team Member
print("\n[TEST 5] Delete Team Member")
print("-" * 80)
try:
    response = session.delete(f'{BASE_URL}/api/admin/teams/Test%20Member%20001%20Updated',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ PASS: Team member deleted successfully")
    else:
        print("❌ FAIL: Could not delete team member")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 6: Get All Incidents
print("\n[TEST 6] Get All Incidents")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/incidents',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Total Incidents: {data.get('count', 0)}")
    
    if response.status_code == 200 and data.get('incidents'):
        print("✅ PASS: Incidents retrieved successfully")
        print(f"Sample incident: {data['incidents'][0] if data['incidents'] else 'None'}")
    else:
        print("❌ FAIL: Could not retrieve incidents")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 7: Add Incident
print("\n[TEST 7] Add Incident")
print("-" * 80)
try:
    new_incident = {
        'Date': datetime.now().strftime('%Y-%m-%d'),
        'Shift': 'S1',
        'Incident Category': 'P1',
        'Status': 'In Progress',
        'Alert': 'Test incident for admin panel testing',
        'Assigned To': 'Raj Kumar',
        'Shift Lead': 'Raj Kumar',
        'Time Slot': '7-8 AM',
        'Alert Report Time': datetime.now().strftime('%H:%M')
    }
    
    response = session.post(f'{BASE_URL}/api/incidents',
        json=new_incident,
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 201:
        print("✅ PASS: Incident added successfully")
        test_incident_row = response.json().get('row_number')
    else:
        print("❌ FAIL: Could not add incident")
        test_incident_row = None
except Exception as e:
    print(f"❌ ERROR: {e}")
    test_incident_row = None

# TEST 8: Update Incident (Admin)
print("\n[TEST 8] Update Incident (Admin)")
print("-" * 80)
if test_incident_row:
    try:
        updated_incident = {
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Shift': 'S2',
            'Incident Category': 'P2',
            'Status': 'Completed',
            'Alert': 'Updated test incident',
            'Assigned To': 'Priya Singh',
            'Shift Lead': 'Priya Singh',
            'Created At': datetime.now().isoformat(),
            'Completed At': datetime.now().isoformat()
        }
        
        response = session.post(f'{BASE_URL}/api/admin/incidents/{test_incident_row}',
            json=updated_incident,
            headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ PASS: Incident updated successfully")
        else:
            print("❌ FAIL: Could not update incident")
    except Exception as e:
        print(f"❌ ERROR: {e}")
else:
    print("⏭️  SKIPPED: No incident to update (previous test failed)")

# TEST 9: Delete Incident (Admin)
print("\n[TEST 9] Delete Incident (Admin)")
print("-" * 80)
if test_incident_row:
    try:
        response = session.delete(f'{BASE_URL}/api/admin/incidents/{test_incident_row}',
            headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ PASS: Incident deleted successfully")
        else:
            print("❌ FAIL: Could not delete incident")
    except Exception as e:
        print(f"❌ ERROR: {e}")
else:
    print("⏭️  SKIPPED: No incident to delete (previous test failed)")

# TEST 10: Get Audit Log
print("\n[TEST 10] Get Audit Log")
print("-" * 80)
try:
    response = session.get(f'{BASE_URL}/api/admin/audit-log',
        headers={'Content-Type': 'application/json'})
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Audit Log Entries: {data.get('count', 0)}")
    
    if response.status_code == 200:
        print("✅ PASS: Audit log retrieved successfully")
        if data.get('entries'):
            print(f"Sample entries: {data['entries'][-3:]}")
    else:
        print("❌ FAIL: Could not retrieve audit log")
except Exception as e:
    print(f"❌ ERROR: {e}")

# TEST 11: Admin Logout
print("\n[TEST 11] Admin Logout")
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
