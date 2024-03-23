# WattTime API Generation


# To register, use the code below. Please note that for these code examples we are using filler values for username
# (freddo), password (the_frog), email (freddo@frog.org), org (freds world) and you should replace each if you are
# copying and pasting this code.

username = 'freddo'
email = 'freddo@frog.org'
password = 'the_frog'
org = 'freds world'

# import requests
# register_url = 'https://api.watttime.org/register'
# params = {'username': username,
#          'password': password,
#          'email': email,
#          'org': org}
# rsp = requests.post(register_url, json=params)
# print(rsp.text)


# To login and obtain an access token, use this code:

# import requests
# from requests.auth import HTTPBasicAuth
# login_url = 'https://api.watttime.org/login'
# rsp = requests.get(login_url, auth=HTTPBasicAuth(username, password))
# TOKEN = rsp.json()['token']
# print(rsp.json())


# To reset your password, use this code:

# import requests
# password_url = f'https://api.watttime.org/password/?username={username}'
# rsp = requests.get(password_url)
# print(rsp.json())