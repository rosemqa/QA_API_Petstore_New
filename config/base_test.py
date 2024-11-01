from services.pet.pet_api import PetApi


class BaseTest:
    def setup_method(self):
        self.pet_api = PetApi()
