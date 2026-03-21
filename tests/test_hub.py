"""Unit tests for smart home hub data processing."""
import json, sqlite3, sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'hub'))

import pytest

def make_db():
    conn = sqlite3.connect(':memory:')
    conn.execute('''CREATE TABLE readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        node TEXT, temp REAL, humidity REAL,
        motion INTEGER, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    return conn


def test_db_insert():
    conn = make_db()
    conn.execute('INSERT INTO readings (node,temp,humidity,motion) VALUES (?,?,?,?)',
                 ('node-01', 23.5, 55.0, 0))
    conn.commit()
    row = conn.execute('SELECT * FROM readings').fetchone()
    assert row[1] == 'node-01'
    assert row[2] == 23.5


def test_valid_payload():
    payload = json.dumps({'node': 'node-01', 'temp': 22.0, 'humidity': 48.0, 'motion': 1})
    data = json.loads(payload)
    assert data['temp'] == 22.0


def test_invalid_payload_handled():
    try:
        data = json.loads('invalid json {{')
    except json.JSONDecodeError:
        pass
