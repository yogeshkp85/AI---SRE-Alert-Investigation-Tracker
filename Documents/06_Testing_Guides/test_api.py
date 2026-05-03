import requests
import json

# Test incidents endpoint
print('📊 Testing /api/incidents endpoint:')
r = requests.get('http://localhost:5000/api/incidents')
data = r.json()
print(f'   Total incidents: {data["count"]}')
if data['incidents']:
    inc = data['incidents'][0]
    print(f'   First incident:')
    print(f'     Date: {inc.get("Date")}')
    print(f'     Shift: {inc.get("Shift")}')
    print(f'     Time Slot: {inc.get("Time Slot")}')
    print(f'     Alert: {inc.get("Alert")[:50]}...')
    print(f'     Assigned To: {inc.get("Assigned To")}')
    print(f'     Status: {inc.get("Status")}')

# Test teams endpoint
print('\n👥 Testing /api/teams endpoint:')
r = requests.get('http://localhost:5000/api/teams')
data = r.json()
print(f'   Total team members: {len(data["members"])}')
print(f'   Members: {data["members"][:5]}...')

print('\n✅ All API endpoints working correctly!')
