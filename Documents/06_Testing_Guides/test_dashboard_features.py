#!/usr/bin/env python3
"""
Dashboard Features Test Script
Tests all dashboard functionality including Print, Edit, and Save
"""

import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

def test_api_health():
    """Test API health check"""
    print("\n" + "="*60)
    print("TEST 1: API Health Check")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Health: {data['status']}")
            print(f"   Timestamp: {data['timestamp']}")
            return True
        else:
            print(f"❌ API Health Check Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_incidents_api():
    """Test incidents API"""
    print("\n" + "="*60)
    print("TEST 2: Incidents API")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        if response.status_code == 200:
            data = response.json()
            incidents = data.get('incidents', [])
            print(f"✅ Incidents API: {len(incidents)} incidents loaded")
            
            if incidents:
                inc = incidents[0]
                print(f"\n   First Incident Details:")
                print(f"   - Date: {inc.get('Date')}")
                print(f"   - Category: {inc.get('Incident Category')}")
                print(f"   - Status: {inc.get('Status')}")
                print(f"   - Assigned To: {inc.get('Assigned To')}")
                print(f"   - RITM: {inc.get('RITM')}")
                print(f"   - MTTR: {inc.get('MTTR (minutes)')}")
                print(f"   - Created At: {inc.get('Created At')}")
                print(f"   - Completed At: {inc.get('Completed At')}")
                print(f"   - Last Modified By: {inc.get('Last Modified By')}")
                print(f"   - Last Modified At: {inc.get('Last Modified At')}")
            
            return True
        else:
            print(f"❌ Incidents API Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_data_structure():
    """Test data structure completeness"""
    print("\n" + "="*60)
    print("TEST 3: Data Structure Validation")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        data = response.json()
        incidents = data.get('incidents', [])
        
        if not incidents:
            print("❌ No incidents found")
            return False
        
        required_fields = [
            'Date', 'Incident Category', 'Shift', 'Shift Lead', 'Time Slot',
            'Alert Report Time', 'Alert', 'Assigned To', 'RITM', 'STIP Incident',
            'Incident Raised', 'Email', 'DB Giant', 'Type Comms', 'Incident Comms',
            'Batch Reportable', 'Final Comms', 'CR', 'Implementation', 'Verification',
            'Issue Communication', 'Additional Task/Improvement', 'Status',
            'Created At', 'Completed At', 'MTTR (minutes)', 'Last Modified By', 'Last Modified At'
        ]
        
        inc = incidents[0]
        missing_fields = []
        for field in required_fields:
            if field not in inc:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing fields: {missing_fields}")
            return False
        else:
            print(f"✅ All {len(required_fields)} required fields present")
            return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_status_distribution():
    """Test status distribution"""
    print("\n" + "="*60)
    print("TEST 4: Status Distribution")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        data = response.json()
        incidents = data.get('incidents', [])
        
        statuses = {}
        for inc in incidents:
            status = inc.get('Status', 'Unknown')
            statuses[status] = statuses.get(status, 0) + 1
        
        print(f"✅ Status Distribution:")
        for status, count in sorted(statuses.items()):
            print(f"   - {status}: {count}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_category_distribution():
    """Test category distribution"""
    print("\n" + "="*60)
    print("TEST 5: Category Distribution")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        data = response.json()
        incidents = data.get('incidents', [])
        
        categories = {}
        for inc in incidents:
            cat = inc.get('Incident Category', 'Unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        print(f"✅ Category Distribution:")
        for cat, count in sorted(categories.items()):
            print(f"   - {cat}: {count}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_editable_incidents():
    """Test incidents that can be edited"""
    print("\n" + "="*60)
    print("TEST 6: Editable Incidents (In Progress/Pending)")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        data = response.json()
        incidents = data.get('incidents', [])
        
        editable = [inc for inc in incidents if inc.get('Status') in ['In Progress', 'Pending']]
        
        print(f"✅ Editable Incidents: {len(editable)} out of {len(incidents)}")
        
        if editable:
            print(f"\n   Sample Editable Incidents:")
            for inc in editable[:3]:
                print(f"   - {inc.get('RITM')}: {inc.get('Status')} ({inc.get('Incident Category')})")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_mttr_calculation():
    """Test MTTR calculation logic"""
    print("\n" + "="*60)
    print("TEST 7: MTTR Calculation Logic")
    print("="*60)
    try:
        response = requests.get(f"{BASE_URL}/api/incidents")
        data = response.json()
        incidents = data.get('incidents', [])
        
        # Find incidents with MTTR values
        with_mttr = [inc for inc in incidents if inc.get('MTTR (minutes)')]
        
        print(f"✅ Incidents with MTTR: {len(with_mttr)} out of {len(incidents)}")
        
        if with_mttr:
            mttr_values = [int(inc.get('MTTR (minutes)', 0)) for inc in with_mttr]
            avg_mttr = sum(mttr_values) / len(mttr_values)
            print(f"   - Average MTTR: {int(avg_mttr)} minutes ({int(avg_mttr/60)}h {int(avg_mttr%60)}m)")
            print(f"   - Min MTTR: {min(mttr_values)} minutes")
            print(f"   - Max MTTR: {max(mttr_values)} minutes")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_print_functionality():
    """Test print functionality (simulated)"""
    print("\n" + "="*60)
    print("TEST 8: Print Functionality (Code Review)")
    print("="*60)
    
    # Read dashboard.html and check for printIncident function
    try:
        with open('templates/dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if 'function printIncident()' in content:
            print("✅ printIncident() function found")
            
            # Check for key print elements
            checks = [
                ('Print window creation', 'window.open'),
                ('Print styling', 'style'),
                ('Print content', 'Incident Report'),
                ('Print trigger', 'printWindow.print()')
            ]
            
            all_good = True
            for check_name, check_str in checks:
                if check_str in content[content.find('function printIncident()'):content.find('function printIncident()') + 2000]:
                    print(f"   ✅ {check_name}: Present")
                else:
                    print(f"   ⚠️  {check_name}: May be missing")
                    all_good = False
            
            return all_good
        else:
            print("❌ printIncident() function not found")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_edit_functionality():
    """Test edit functionality (code review)"""
    print("\n" + "="*60)
    print("TEST 9: Edit Functionality (Code Review)")
    print("="*60)
    
    try:
        with open('templates/dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        functions = ['editIncident()', 'saveIncidentEdit()']
        all_found = True
        
        for func in functions:
            if f'function {func}' in content:
                print(f"✅ {func} function found")
            else:
                print(f"❌ {func} function not found")
                all_found = False
        
        # Check for edit form elements
        if 'editStatus' in content and 'editCompletedDate' in content and 'editLastBy' in content:
            print("✅ Edit form fields present (Status, Completed Date, Last Edited By)")
        else:
            print("❌ Edit form fields missing")
            all_found = False
        
        # Check for edit button visibility logic
        if "inc['Status'] === 'In Progress' || inc['Status'] === 'Pending'" in content:
            print("✅ Edit button visibility logic correct (In Progress/Pending only)")
        else:
            print("⚠️  Edit button visibility logic may need verification")
        
        return all_found
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_save_functionality():
    """Test save functionality (code review)"""
    print("\n" + "="*60)
    print("TEST 10: Save Functionality (Code Review)")
    print("="*60)
    
    try:
        with open('templates/dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check for save logic
        checks = [
            ('Status update', "inc['Status'] = newStatus"),
            ('Completed At update', "inc['Completed At']"),
            ('MTTR calculation', "mttrMinutes"),
            ('Last Modified By', "inc['Last Modified By']"),
            ('Last Modified At', "inc['Last Modified At']"),
            ('Dashboard refresh', 'applyFilters()')
        ]
        
        all_good = True
        for check_name, check_str in checks:
            if check_str in content:
                print(f"✅ {check_name}: Present")
            else:
                print(f"❌ {check_name}: Missing")
                all_good = False
        
        return all_good
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("DASHBOARD FEATURES TEST SUITE")
    print("="*60)
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: {BASE_URL}")
    
    results = []
    
    # Run tests
    results.append(("API Health Check", test_api_health()))
    results.append(("Incidents API", test_incidents_api()))
    results.append(("Data Structure", test_data_structure()))
    results.append(("Status Distribution", test_status_distribution()))
    results.append(("Category Distribution", test_category_distribution()))
    results.append(("Editable Incidents", test_editable_incidents()))
    results.append(("MTTR Calculation", test_mttr_calculation()))
    results.append(("Print Functionality", test_print_functionality()))
    results.append(("Edit Functionality", test_edit_functionality()))
    results.append(("Save Functionality", test_save_functionality()))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Dashboard is ready for manual testing.")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
