from requests import post

base_url = 'http://url:port/user'

json_data = '' #user_json_data
r = post(url = base_url, json = json_data)

print(r)
print(r.json)
print(r.content)