import requests
import json

print('Testing API endpoints...\n')

# Test health
try:
    r = requests.get('http://localhost:5000/api/health')
    print(f'✅ Health: {r.status_code}')
except Exception as e:
    print(f'❌ Health error: {e}')

# Test incidents
try:
    r = requests.get('http://localhost:5000/api/incidents')
    print(f'✅ Incidents: {r.status_code}')
    data = r.json()
    print(f'   Count: {data.get("count")}')
    if data.get('incidents'):
        inc = data['incidents'][0]
        print(f'   First incident keys: {list(inc.keys())[:8]}')
        print(f'   Date: {inc.get("Date")}')
        print(f'   Shift: {inc.get("Shift")}')
        print(f'   Incident Category: {inc.get("Incident Category")}')
        print(f'   Shift Lead: {inc.get("Shift Lead")}')
except Exception as e:
    print(f'❌ Incidents error: {e}')
    import traceback
    traceback.print_exc()
