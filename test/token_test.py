from requests import post
from main.services.auth import token_encode

base_url = 'http://server:port/token/'

payload_encode = '' #user json

token_s = token_encode(payload=payload_encode)


def test_token_encode():
    r = post(url = base_url + 'encode', json = payload_encode)
    assert token_s == r.json()

def test_token_decode():
    r = post(url = base_url + 'decode', json = token_s)
    assert payload_encode == r.json()

def test_user_with_token_header():
    assert 1 == 1