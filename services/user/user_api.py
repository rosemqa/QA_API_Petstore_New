import random

import allure
from models.user_model import ApiResponseModel, UserModel, AuthHeadersModel
from services.user.user_endpoints import UserEndpoints
from services.user.user_payloads import UserPayloads
from utils.helper import Helper
from utils.my_requests import MyRequests


class UserAPI(Helper):
    def __init__(self):
        self.endpoints = UserEndpoints()
        self.payloads = UserPayloads()

    @allure.step('Create a new user')
    def create_user(self):
        response = MyRequests.post(
            url=UserEndpoints.create_user,
            json=UserPayloads.create_user
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        user_date = UserPayloads.create_user
        return model, user_date

    @allure.step('Get user by username')
    def get_user_by_username(self, username):
        response = MyRequests.get(
            url=self.endpoints.get_user_by_username(username)
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step('Get user by not existent username')
    def get_not_existent_user(self, username):
        response = MyRequests.get(
            url=self.endpoints.get_user_by_username(username)
        )
        assert response.status_code == 404, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Update all user data by username')
    def update_user_by_username(self, username):
        response = MyRequests.put(
            url=self.endpoints.update_user(username),
            json=self.payloads.update_user
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        user_new_data = UserPayloads.update_user
        return model, user_new_data

    @allure.step('Delete user by username')
    def delete_user_by_username(self, username):
        response = MyRequests.delete(
            url=self.endpoints.delete_user(username)
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Delete user by not existent username')
    def delete_not_existent_user(self):
        username = '1234567890'
        response = MyRequests.delete(
            url=self.endpoints.delete_user(username)
        )
        assert response.status_code == 404, f'{response.status_code} {response.text}'
        return response

    @allure.step('Login user with username and password')
    def login_user(self, username, password):
        response = MyRequests.get(
            url=self.endpoints.login_user,
            params={'username': username, 'password': password}
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        headers = AuthHeadersModel(**response.headers)
        return model, headers

    @allure.step('Logout user')
    def logout_user(self):
        response = MyRequests.get(
            url=self.endpoints.logout_user
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    def create_list_of_users(self):
        user_list = [self.payloads.create_user_list() for _ in range(random.randint(2, 5))]
        response = MyRequests.post(
            url=self.endpoints.create_user_list,
            json=user_list
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model
