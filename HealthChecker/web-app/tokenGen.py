import requests
import hmac
import base64
import config
import json


def getToken():
    username = config.username
    password = config.password
    authUrl = config.priaid_authservice_url

    rawHashString = hmac.new(bytes(password, encoding='utf-8'), authUrl.encode('utf-8')).digest()
    computedHashString = base64.b64encode(rawHashString).decode()

    bearer_credentials = username + ':' + computedHashString
    postHeaders = {
        'Authorization': 'Bearer {}'.format(bearer_credentials)
    }
    responsePost = requests.post(authUrl, headers=postHeaders)

    data = json.loads(responsePost.text)
    return data["Token"]
