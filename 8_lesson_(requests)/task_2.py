# from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file, name_file):
        get_upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(url=get_upload_url, headers=headers, params=params).json()
        # pprint(response)
        href = response.get('href')
        upload_file = requests.put(href, data=open(name_file, 'rb'))
        upload_file.raise_for_status()
        if upload_file.status_code == 201:
            print('upload successful')


if __name__ == '__main__':
    name_file = 'test_task_2.txt'
    path_to_file = f'netology/{name_file}'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, name_file)
