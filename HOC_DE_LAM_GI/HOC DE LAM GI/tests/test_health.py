import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'backend'))
from fastapi.testclient import TestClient
from main import app
client=TestClient(app)
def test_health():
    r=client.get('/api/health')
    assert r.status_code==200
    assert r.json()['status']=='ok'
