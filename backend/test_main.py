import pytest
from datetime import date
from fastapi.testclient import TestClient
from main import *
from schemas import *

client = TestClient(app)
def test_calcweeks():
    d1 = date(2023, 12, 22)
    d2 = date(2024, 6, 13)
    res = client.post('/v1/calcweeks', json={'conceiving_date':str(d1), 'last_date':str(d2)})
    assert res.status_code == 200
    assert res.json()['response'] == {'conceiving_date':str(d1), 'last_date':str(d2), 'weeks': 24, 'days': 6}



