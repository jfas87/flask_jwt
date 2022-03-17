from requests import post, get

base_url = 'http://server:port'

payload_encode = '' #user json


def test_success():

    r = post(f'{base_url}/auth/user', json = payload_encode)   
    header = { 'token' : r.json().encode('UTF-8')}
    r = get(f'{base_url}/user/list', headers=header)
    assert r.status_code == 200
    