from config.config import BASE_URL


class UserEndpoints:
    create_user = f'{BASE_URL}/user'
    create_user_list = f'{BASE_URL}/user/createWithList'
    get_user_by_username = lambda self, username: f'{BASE_URL}/user/{username}'
    update_user = lambda self, username: f'{BASE_URL}/user/{username}'
    delete_user = lambda self, username: f'{BASE_URL}/user/{username}'
    login_user = f'{BASE_URL}/user/login'
    logout_user = f'{BASE_URL}/user/logout'
