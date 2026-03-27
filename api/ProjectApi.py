import requests


class ProjectApi:

    def __init__(self) -> None:
        self.base_url = 'https://ru.yougile.com/api-v2'
        self.token = None
        self.headers = {}

    def get_auth_token(self, login: str, password: str, companyId: str) -> str:
        url = '{yougile}/auth/keys'.format(yougile=self.base_url)
        payload = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        response = requests.post(url, json=payload)
        self.token = response.json()['key']
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        return self.token

    def get_token(self) -> str:
        return self.token

    def get_headers(self) -> dict:
        return self.headers

    def get_all_projects(self) -> dict:
        url = '{yougile}/projects'.format(yougile=self.base_url)
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def create_project(self, title: str) -> dict:
        url = '{yougile}/projects'.format(yougile=self.base_url)
        response = requests.post(url, headers=self.get_headers(),
                                 json={"title": title})
        return response.json()

    def delete_project_by_id(self, id: str):
        url = '{yougile}/projects/{project_id}'.format(yougile=self.base_url,
                                                       project_id=id)
        response = requests.put(url, headers=self.get_headers(),
                                json={"deleted": True})
        return response.json()
