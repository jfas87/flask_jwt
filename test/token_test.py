from requests import post

base_url = 'http://server:port/token'
#must be tested with the flask api running

payload_encode = '' #user json data

token = '' #token string valye

payload_decode = '' #token value in json format

def test_answer():
    response = post(url = base_url + "/encode", data = payload_encode)
    api_encoded_token = response.json()
    assert token != api_encoded_token

def test_answer_2():
    response = post(url = base_url + "/encode", data = payload_decode)
    api_decoded_token = response.json()
    assert payload_decode != api_decoded_token