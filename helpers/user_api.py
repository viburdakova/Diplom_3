from typing import Optional, Dict, List

import requests

import data
from data import DELETE_USER_URL


class UserApi:

    @staticmethod
    def get_headers(token: Optional[str] = None) -> Dict:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = token
        return headers

    @staticmethod
    def create_user(payload):
        url = data.CREATE_USER_URL
        response = requests.post(url, data=payload)
        return response.json(), response.status_code

    @staticmethod
    def delete_user(token: str) -> requests.Response:
        headers = UserApi.get_headers()
        headers["Authorization"] = token

        response = requests.delete(
            DELETE_USER_URL,
            headers=headers
        )
        return response
