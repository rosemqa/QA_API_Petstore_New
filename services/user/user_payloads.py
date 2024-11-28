from faker import Faker

fake = Faker()


class UserPayloads:
    create_user = {
        "id": fake.random_number(digits=19),
        "username": fake.user_name(),
        "firstName": fake.first_name_male(),
        "lastName": fake.last_name_male(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": 0
    }

    update_user = {
        "id": create_user['id'],
        "username": create_user['username'],
        "firstName": fake.first_name_female(),
        "lastName": fake.first_name_female(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": 0
    }

    @staticmethod
    def create_user_list():
        user = {
            "id": fake.random_number(digits=19),
            "username": fake.user_name(),
            "firstName": fake.first_name_male(),
            "lastName": fake.last_name_male(),
            "email": fake.email(),
            "password": fake.password(),
            "phone": fake.phone_number(),
            "userStatus": 0
        }
        return user
