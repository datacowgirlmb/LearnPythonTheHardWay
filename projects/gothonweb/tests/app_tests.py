# from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code  == 404

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code  == 200
    # assert_in(b"Fill Out This Form", rv.data)
    assert b"Fill Out This Form" in rv.data

    data = {'name': 'Maggie', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    # assert_in(b"Maggie", rv.data)
    # assert_in(b"Hola", rv.data)
    assert b"Maggie" in rv.data
    assert b"Hola" in rv.data
