from famProject.constants import GET, POST
import requests


def network_call(url, method, params, headers):
    try:
        data, response = {}, {}
        if method == GET:
            response = requests.get(url, params=params, headers=headers)
        if method == POST:
            pass
        if response.status_code == 200:
            data = response.json()
        return data
    except Exception as e:
        pass
