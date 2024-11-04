from faker import Faker

fake = Faker()


class PetPayloads:
    add_new_pet = {
        "id": 1020, #fake.random_number(digits=19),
        "category": {
            "id": fake.random_number(3),
            "name": fake.word()
        },
        "name": fake.first_name(),
        "photoUrls": [
            "https://storage-api.petstory.ru/resize/1000x1000x80/cb/48/7f/cb487f4677a640329e92ac0076004607.jpeg"
        ],
        "tags": [
            {
                "id": fake.random_number(3),
                "name": fake.word()
            }
        ],
        "status": "available"
    }
