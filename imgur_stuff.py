import requests
import os


class Imgur():
    client_id = None
    remCredits = None

    def __init__(self, clientID):
        self.client_id = clientID

    def uploadImage(self, file, title, description):
        file.save(file.filename)
        with open(file.filename, 'rb') as f:
            data = f.read()
        url = "https://api.imgur.com/3/image"
        payload = {'image': data, 'title': title, 'description': description}
        headers = {
            "authorization": f"Client-ID {self.client_id}"
        }
        res = requests.request("POST", url, headers=headers, data=payload)
        os.remove(file.filename)
        response = res.json()
        if response['success']:
            return response['data']['link']
        else:
            return None
