import allure
from config.base_test import BaseTest


@allure.epic('User cases')
class TestUser(BaseTest):
    @allure.description('Can create a new user')
    def test_create_user(self, check):
        # CREATE A NEW USER
        create_user, user_data = self.user_api.create_user()
        user_id = user_data['id']
        with check:
            assert create_user.message == str(user_id), \
                'Check user ID in the response message when creating a user'

        # GET USER INFO BY USERNAME
        username = user_data['username']
        user = self.user_api.get_user_by_username(username)
        with check:
            assert user.model_dump() == user_data, 'User data in the response JSON does not match the new user data'

    @allure.description('Can update user data by username and user ID')
    def test_update_user(self):
        # CREATE A NEW USER
        create_user, user_data = self.user_api.create_user()
        username = user_data['username']

        # UPDATE USER BY USERNAME
        updated_user, user_new_data = self.user_api.update_user_by_username(username)

        # GET USER INFO BY USERNAME
        user = self.user_api.get_user_by_username(username)
        assert user.model_dump() == user_new_data, 'User data not updated'

    @allure.description('Can delete user by username')
    def test_delete_user(self):
        # CREATE A NEW USER
        create_user, user_data = self.user_api.create_user()
        username = user_data['username']

        # DELETE USER BY USERNAME
        delete_user = self.user_api.delete_user_by_username(username)
        assert delete_user.message == username

        # GET USER BY USERNAME
        user = self.user_api.get_not_existent_user(username)
        assert user.message == "User not found", 'Check error message for GET request'

    @allure.description('Can login with username and password')
    def test_login_user(self):
        # CREATE A NEW USER
        create_user, user_data = self.user_api.create_user()
        username = user_data['username']
        password = user_data['password']

        # LOGIN
        rate_limit = 5000
        model, headers = self.user_api.login_user(username, password)
        assert 'logged in user session:' in model.message, 'Check message in response'
        assert headers.x_rate_limit == rate_limit, 'Check x_rate_limit value in response headers'

    @allure.description('Can logout')
    def test_logout_user(self):
        logout = self.user_api.logout_user()
        assert logout.message == 'ok', 'Check message in response'

    @allure.description('Can create a list of users with given input list')
    def test_create_user_list(self):
        users = self.user_api.create_list_of_users()
        assert users.message == 'ok', 'Check message in response'
