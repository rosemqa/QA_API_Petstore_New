from services.pet.pet_api import PetApi
from services.store.store_api import StoreApi


class BaseTest:
    def setup_method(self):
        self.pet_api = PetApi()
        self.store_api = StoreApi()
