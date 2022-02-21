from requests import post

base_url = 'http://server:port/token/'

payload_encode = '' #user json

token_s = '' #token_Value

payload_decode = '' #json with token value

def test_tokend_encode():
    r = post(url = base_url + 'encode', json = payload_encode)
    assert token_s == r.json()

def test_tokend_decode():
    r = post(url = base_url + 'decode', json = payload_decode)
    assert payload_encode == r.json()