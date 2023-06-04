import requests

TOKEN = '...'

class Yandex:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = TOKEN

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, folder_name):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': f'disk:/{folder_name}'}
        response = requests.put(url, headers=self.get_headers(), params=params)
        return response.status_code

if __name__== '__main__':
    ya = Yandex(TOKEN)
    ya.create_folder()

