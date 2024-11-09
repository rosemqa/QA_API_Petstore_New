import datetime
import random
from faker import Faker

fake = Faker()


class StorePayloads:
    place_order = {
        "id": 0,
        "petId": fake.random_number(digits=19),
        "quantity": random.randint(1, 3),
        "shipDate": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        "status": random.choice(['placed', 'approved', 'delivered']),
        "complete": True
    }
