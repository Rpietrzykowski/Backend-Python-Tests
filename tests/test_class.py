from utils.utils import create_folder, delete_folder, upload_file, get_group_folder_permissions, set_group_folder_permissions, get_user_id_by_name
from dataextractor.extract_json_data import find_json_key
import pytest


@pytest.mark.regression
def test_create_valid_folder_delete_folder():
    folder = 'Shared/test'
    response = create_folder(folder)
    assert response.status_code == 201, f'Error: {response.json()["errorMessage"]}'
    print(f'Folder created, ID: {find_json_key(response, "folder_id")}')
    response = delete_folder(folder)
    assert response.status_code == 200, f'Error: {response.json()["errorMessage"]}'
    print('Folder deleted!')


@pytest.mark.regression
def test_create_multiple_folders():
    for number in range(1, 6):
        folder = 'Shared/test' + str(number)
        response = create_folder(folder)
        assert response.status_code == 201, f'Error: {response.json()["errorMessage"]}'
        print(f'Folder created, ID: {find_json_key(response, "folder_id")}')


@pytest.mark.regression
def test_create_folder_forbidden_character():
    folder = 'Shared/*'
    response = create_folder(folder)
    assert response.status_code == 409
    print(f'Error: {find_json_key(response, "errorMessage")}')


@pytest.mark.regression
def test_upload_txt_file_and_verify_path():
    file_name = 'text.txt'
    file_path = 'Shared/Documents/text.txt'
    response = upload_file(file_path, file_name)
    assert response.status_code == 200, f'Wrong Status Code: Expected 200, Actual {response.status_code} ' \
                                        f'Error: {response.content} '
    path = find_json_key(response, 'path')
    assert path == '/Shared/Documents/text.txt', f'Wrong file path.'


@pytest.mark.regression
def test_upload_file_forbidden_character():
    file_name = '<.txt'
    file_path = 'Shared/Documents/<.txt'
    response = upload_file(file_path, file_name)
    print(f'Error: {find_json_key(response, "message")}')


@pytest.mark.regression
def test_change_user_permission():
    user_id = get_user_id_by_name('rpietrzy')



test_change_user_permission()









