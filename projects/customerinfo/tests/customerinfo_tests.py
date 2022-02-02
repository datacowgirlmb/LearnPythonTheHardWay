from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects = True)
    assert_equal(rv.status_code, 200)

    data = {'first_name': 'Maggie', 'last_name': 'Butler', 'dob': '9/13/1986'}
    rv = web.post('/', follow_redirects=True, data=data)
    assert_in(b"Maggie", rv.data)
    assert_in(b"Butler", rv.data)
