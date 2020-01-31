import requests
from resources.api_links import ApiLinks
from oauthmanager.authentication import auth_header
from dataextractor import extract_json_data
from requests import HTTPError


def create_folder(folder):
    url = ApiLinks.BASE_URI + ApiLinks.FILE_SYSTEM
    body = {'action': 'add_folder'}
    folder_url = url + folder
    body_json = extract_json_data.parse_body_to_json(body)
    response = requests.post(folder_url, body_json, headers=auth_header('post'))
    return response


def delete_folder(folder):
    url = ApiLinks.BASE_URI + ApiLinks.FILE_SYSTEM
    folder_url = url + folder
    response = requests.delete(folder_url, headers=auth_header('delete'))
    return response


def get_user_info():
    url = ApiLinks.BASE_URI + 'pubapi/v1/userinfo'
    response = requests.get(url, headers=auth_header('get'))
    return response


def api_connection(url):
    # Try to connect to API and check if it is alive
    try:
        # Get response from pointed URL
        response = requests.get(url)
        # Assign status code into value status
        status = response.status_code
        # Raise for status if unsuccessful
        response.raise_for_status()
    # If http error appears print HTTP error
    except HTTPError as http_err:
        return http_err
    # If different error appears then print error
    except Exception as err:
        return err
    else:
        return status


def check_api_connection(url):
    response = api_connection(url)
    if str(response)[0] == '2':
        print('Success!')
    else:
        print(response)


def upload_file(file_path, file_name):
    url = ApiLinks.BASE_URI + ApiLinks.UPLOAD_FILE + file_path
    files = {'upload_file': open('../resources/' + file_name, 'rb')}
    response = requests.post(url, files=files, headers=auth_header('post'))
    return response


def get_group_folder_permissions(folder, key):
    url = ApiLinks.BASE_URI + ApiLinks.PERMISSIONS + folder
    response = requests.get(url, headers=auth_header('get'))
    json_value = extract_json_data.find_json_key(response, key)
    return json_value


def set_group_folder_permissions(folder, body):
    url = ApiLinks.BASE_URI + ApiLinks.PERMISSIONS + folder
    body_json = extract_json_data.parse_body_to_json(body)
    response = requests.post(url, body_json, headers=auth_header('post'))
    return response


def get_users_list():
    url = ApiLinks.BASE_URI + ApiLinks.USERS
    response = requests.get(url, headers=auth_header('post'))
    return response


def get_user_id_by_name(user_name):
    response = get_users_list()
    response_json = response.json()
    user_list = response_json["resources"]
    for user in user_list:
        if user['userName'] == user_name:
            return user['id']
        else:
            print("User not found!")








get_user_id_by_name()







