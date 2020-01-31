import requests
from resources.api_links import ApiLinks
from resources.login_resources import LoginCredentials


def get_login_response():
    url = ApiLinks.BASE_URI + ApiLinks.OAUTH
    client_id = LoginCredentials.CLIENT_ID
    username = LoginCredentials.USERNAME
    password = LoginCredentials.PASSWORD
    grant_type = LoginCredentials.GRANT_TYPE

    params = {'client_id': client_id,
              'username': username,
              'password': password,
              'grant_type': grant_type}

    response = requests.post(url, params=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(response.content)

get_login_response()


def auth_header(method):
    token = LoginCredentials.TOKEN
    if method == 'patch' or method == 'post':
        header = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    elif method == 'get' or method == 'delete':
        header = {'Authorization': f'Bearer {token}'}
    else:
        "Unknown method"
    return header
