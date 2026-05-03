#!/usr/bin/env python3
"""
Comprehensive test of Admin panel features
Tests: Login, Incidents (Add/Edit/Delete), Team Members (Add/Edit/Delete), Audit Log
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"
SESSION = requests.Session()

def print_test(test_name, status, details=""):
    """Print test result"""
    symbol = "✓" if status else "✗"
    color = "\033[92m" if status else "\033[91m"
    reset = "\033[0m"
    print(f"{color}{symbol}{reset} {test_name}")
    if details:
        print(f"  → {details}")

def test_admin_login():
    """Test 1: Admin Login"""
    print("\n" + "="*60)
    print("TEST 1: ADMIN LOGIN")
    print("="*60)
    
    try:
        response = SESSION.post(
            f"{BASE_URL}/api/admin/login",
            json={"pin": "9999"}
        )
        success = response.status_code == 200
        data = response.json()
        print_test("Admin Login", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Admin Login", False, f"Error: {str(e)}")
        return False

def test_get_incidents():
    """Test 2: Get All Incidents"""
    print("\n" + "="*60)
    print("TEST 2: GET ALL INCIDENTS")
    print("="*60)
    
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        success = response.status_code == 200
        data = response.json()
        count = data.get('count', 0)
        print_test("Get Incidents", success, f"Status: {response.status_code}, Count: {count}")
        return success, data.get('incidents', [])
    except Exception as e:
        print_test("Get Incidents", False, f"Error: {str(e)}")
        return False, []

def test_add_incident():
    """Test 3: Add New Incident"""
    print("\n" + "="*60)
    print("TEST 3: ADD NEW INCIDENT")
    print("="*60)
    
    try:
        new_incident = {
            "Date": "2026-05-02",
            "Shift": "S1",
            "Incident Category": "P1",
            "Status": "In Progress",
            "Alert": "Test Alert - New Incident",
            "Assigned To": "Amit Patel",
            "Shift Lead": "Raj Kumar",
            "Time Slot": "7-8 AM",
            "Alert Report Time": "09:00"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/incidents",
            json=new_incident
        )
        success = response.status_code == 201
        data = response.json()
        print_test("Add Incident", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success, data.get('row_number')
    except Exception as e:
        print_test("Add Incident", False, f"Error: {str(e)}")
        return False, None

def test_edit_incident(row_number):
    """Test 4: Edit Incident"""
    print("\n" + "="*60)
    print("TEST 4: EDIT INCIDENT")
    print("="*60)
    
    try:
        updated_incident = {
            "Date": "2026-05-02",
            "Shift": "S2",
            "Incident Category": "P2",
            "Status": "Pending",
            "Alert": "Test Alert - Updated Incident",
            "Assigned To": "Vikram Joshi",
            "Shift Lead": "Neha Sharma"
        }
        
        response = SESSION.post(
            f"{BASE_URL}/api/admin/incidents/{row_number}",
            json=updated_incident
        )
        success = response.status_code == 200
        data = response.json()
        print_test("Edit Incident", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Edit Incident", False, f"Error: {str(e)}")
        return False

def test_delete_incident(row_number):
    """Test 5: Delete Incident"""
    print("\n" + "="*60)
    print("TEST 5: DELETE INCIDENT")
    print("="*60)
    
    try:
        response = SESSION.delete(
            f"{BASE_URL}/api/admin/incidents/{row_number}"
        )
        success = response.status_code == 200
        data = response.json()
        print_test("Delete Incident", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Delete Incident", False, f"Error: {str(e)}")
        return False

def test_get_team_members():
    """Test 6: Get All Team Members"""
    print("\n" + "="*60)
    print("TEST 6: GET ALL TEAM MEMBERS")
    print("="*60)
    
    try:
        response = SESSION.get(
            f"{BASE_URL}/api/admin/teams"
        )
        success = response.status_code == 200
        data = response.json()
        count = len(data.get('members', []))
        print_test("Get Team Members", success, f"Status: {response.status_code}, Count: {count}")
        return success, data.get('members', [])
    except Exception as e:
        print_test("Get Team Members", False, f"Error: {str(e)}")
        return False, []

def test_add_team_member():
    """Test 7: Add Team Member"""
    print("\n" + "="*60)
    print("TEST 7: ADD TEAM MEMBER")
    print("="*60)
    
    try:
        new_member = {
            "name": "Test Member",
            "shift": "S1",
            "email": "test@example.com",
            "phone": "555-1234"
        }
        
        response = SESSION.post(
            f"{BASE_URL}/api/admin/teams",
            json=new_member
        )
        success = response.status_code == 201
        data = response.json()
        print_test("Add Team Member", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Add Team Member", False, f"Error: {str(e)}")
        return False

def test_update_team_member():
    """Test 8: Update Team Member"""
    print("\n" + "="*60)
    print("TEST 8: UPDATE TEAM MEMBER")
    print("="*60)
    
    try:
        updated_member = {
            "name": "Test Member Updated",
            "shift": "S2",
            "email": "updated@example.com",
            "phone": "555-5678"
        }
        
        response = SESSION.put(
            f"{BASE_URL}/api/admin/teams/Test%20Member",
            json=updated_member
        )
        success = response.status_code == 200
        data = response.json()
        print_test("Update Team Member", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Update Team Member", False, f"Error: {str(e)}")
        return False

def test_delete_team_member():
    """Test 9: Delete Team Member"""
    print("\n" + "="*60)
    print("TEST 9: DELETE TEAM MEMBER")
    print("="*60)
    
    try:
        response = SESSION.delete(
            f"{BASE_URL}/api/admin/teams/Test%20Member%20Updated"
        )
        success = response.status_code == 200
        data = response.json()
        print_test("Delete Team Member", success, f"Status: {response.status_code}, Message: {data.get('message', 'N/A')}")
        return success
    except Exception as e:
        print_test("Delete Team Member", False, f"Error: {str(e)}")
        return False

def test_get_audit_log():
    """Test 10: Get Audit Log"""
    print("\n" + "="*60)
    print("TEST 10: GET AUDIT LOG")
    print("="*60)
    
    try:
        response = SESSION.get(
            f"{BASE_URL}/api/admin/audit-log"
        )
        success = response.status_code == 200
        data = response.json()
        count = data.get('count', 0)
        print_test("Get Audit Log", success, f"Status: {response.status_code}, Count: {count}")
        return success
    except Exception as e:
        print_test("Get Audit Log", False, f"Error: {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("ADMIN PANEL COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    results = {}
    
    # Test 1: Login
    results['login'] = test_admin_login()
    
    if not results['login']:
        print("\n❌ Login failed - cannot proceed with other tests")
        return
    
    # Test 2: Get Incidents
    results['get_incidents'], incidents = test_get_incidents()
    
    # Test 3: Add Incident
    results['add_incident'], new_row = test_add_incident()
    
    # Test 4: Edit Incident
    if new_row:
        results['edit_incident'] = test_edit_incident(new_row)
    else:
        results['edit_incident'] = False
        print("⚠️  Skipping edit test - no incident to edit")
    
    # Test 5: Delete Incident
    if new_row:
        results['delete_incident'] = test_delete_incident(new_row)
    else:
        results['delete_incident'] = False
        print("⚠️  Skipping delete test - no incident to delete")
    
    # Test 6: Get Team Members
    results['get_team_members'], members = test_get_team_members()
    
    # Test 7: Add Team Member
    results['add_team_member'] = test_add_team_member()
    
    # Test 8: Update Team Member
    results['update_team_member'] = test_update_team_member()
    
    # Test 9: Delete Team Member
    results['delete_team_member'] = test_delete_team_member()
    
    # Test 10: Get Audit Log
    results['get_audit_log'] = test_get_audit_log()
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")

if __name__ == '__main__':
    main()
