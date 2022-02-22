from requests import get

base_url = 'http://server:port/user'

def test_user():
    r = get(base_url)
    assert r.status_code == 200

def test_user_by_id():
    r = get(base_url, params = {'id':0}) #test_data
    user = r.json()
    assert user['email'] == 'useremail@email' #test_data