import random
from faker import Faker

fake = Faker()


class PetPayloads:
    add_new_pet = {
        "id": fake.random_number(digits=19),
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
        "status": random.choice(['available', 'sold', 'pending'])
    }

    update_existing_pet = {
        "id": add_new_pet['id'],
        "category": {
            "id": fake.random_number(3),
            "name": fake.word()
        },
        "name": fake.first_name(),
        "photoUrls": [
            fake.image_url()
        ],
        "tags": [
            {
                "id": fake.random_number(3),
                "name": fake.word()
            }
        ],
        "status": random.choice(['available', 'sold', 'pending'])
    }

    image = 'files/dog.jpg'

    upload_image = {
        'file': open(image, 'rb'),
        'additionalMetadata': fake.word()
    }

    update_name_and_status = {
            'name': fake.first_name(),
            'status': random.choice(['available', 'sold', 'pending'])
        }
