import requests
from pprint import pprint


token = ''
url = 'https://cloud-api.yandex.net/v1/disk/resources/'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_files_list(self):
        files_url = f'{url}files'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(files_url, headers=headers, timeout=5)
        return response.json()

    def get_upload_link(self, disc_file_path):
        upload_url = f'{url}upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': disc_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disc(self, disc_file_path, filename):
        link_dict = self.get_upload_link(disc_file_path=disc_file_path)
        href = link_dict.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    ya = YaUploader(token=token)
    pprint(ya.upload_file_to_disc('test.txt', 'test.txt'))
