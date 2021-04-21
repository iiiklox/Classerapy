import requests
import helpers
import json
import requests

device = helpers.Device()
headers = helpers.Headers()

class client:
    def __init__(self, proxies: dict = None, certificatePath = None):
            self.api = "https://lns-api.classera.com/v2/"
            self.apiOld = "https://lns-cns.classera.com/api/v1/"
            self.chatApi = "https://chat-az.classera.com/api/"
            self.proxies = proxies
            self.certificatePath = certificatePath
            self.json = None
            self.userAgent = device.userAgent
            self.token = device.token
            self.auth = None

    def login(self, username: str, password: str):
        """
        Login into a classera account and save AUTH_KEY.

        **Parameters**
            - **username** : username of the account.
            - **password** : Password of the account.
        """
        data = {
            "password": f"{password}",
            "username": f"{username}",
            "app_type": f"classera"
        }

        response = requests.post(f"{self.api}users/users_login?access_token={self.token}", headers=headers.headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        helpers.Auth(json.loads(response.text)["data"]["auth_token"])

    def get_materials_list(self):
        """
        Get course materials list.

        **Returns**
             - Courses JSON list.
        """

        response = requests.get(f"{self.api}courses/get_cours_list?access_token={self.token}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["data"]

    def get_material_info(self, courseId: any, teacherId: any):
        """
        Get course material info from courseId and teacherId.

        **Returns**
             - Teacher's course details.
        """

        response = requests.get(f"{self.api}courses/browse_content_v2?course_id={courseId}&teacher_user_id={teacherId}&access_token={self.token}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["data"]

    
    def get_user_info(self, userId: int):
        """
        Get user info from userId.

        **Parameters**
            - **userId** : The userId of desired account.
        """
        data = {
            "users_ids[]": f"{userId}"
        }

        response = requests.post(f"{self.api}users/get_users_baisc_details?access_token={self.token}", data=data, headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["data"]

    def check_client_block(self, userId: int):
        """
        Know if a user is blocking you or not.

        **Parameters**
            - **userId** : The userId of desired account.
        """

        response = requests.get(f"{self.api}ChatsUsers/check_blocked/?access_token={self.token}&block_user_id={userId}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["data"]["is_block_me"]


    def get_user_notifications(self, userId: int, page: int, limit: int, source: str = "web"):
        """
        Get a user's notifications.

        **Parameters**
            - **userId** : userId of an account.
            - **page** : Page of notifications list.
            - **limit** : size of pages loaded.
            - **source** : client type, a known type is "web".
        """

        response = requests.get(f"{self.apiOld}users/{userId}/notifications?page={page}&limit={limit}&source={source}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["notifications"]

    def get_user_dms_notifications(self, userId: int, page: int, limit: int, source: str = "web"):
        """
        Get a user's dms notifications.

        **Parameters**
            - **userId** : userId of an account.
            - **page** : Page of notifications list.
            - **limit** : size of pages loaded.
            - **source** : client type, a known type is "web".
        """

        response = requests.get(f"{self.apiOld}users/{userId}/notifications?page={page}&limit={limit}&source={source}&types%5B%5D=mail", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["notifications"]

    def get_threadId(self, userId: int, source: str = "me"):
        """
        Get a user's dms notifications.

        **Parameters**
            - **userId** : userId of an account.
        """

        response = requests.get(f"{self.chatApi}list-users/{userId}/{userId}?source={source}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["users"][0]["thread_id"]

    def get_messages(self, threadId: int, source: str = "me"):
        """
        Get a conversasion's messages.

        **Parameters**
            - **threadId** : userId of an account.
            - **source** : client type, a known type is "me".
        """

        response = requests.get(f"{self.chatApi}list-messages/{threadId}/0?source={source}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["result"]

    def get_chat_users(self, schoolId: any):
        """
        Get chatable users from schoolId.

        **Parameters**
            - **schoolId** : Id of desired school entity.
        """

        response = requests.get(f"{self.api}ChatsUsers/chat_user_list?access_token={self.token}&school_id={schoolId}", headers=helpers.Headers(auth=helpers.Auth().key).headersAuth, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)["data"]



