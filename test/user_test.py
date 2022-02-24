from requests import get, post

base_url = 'http://server:port/user'

user_payload = '' #user_data

def test_user():
    assert get(base_url).status_code == 200

def test_user_by_id():
    r = get(base_url, params = {'id':1}) #test_data
    user = r.json()
    assert user['email'] == 'user@email.com' #test_data

def test_new_user():
    assert post(base_url, json = user_payload) .status_code == 200 #test_data