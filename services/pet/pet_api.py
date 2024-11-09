import allure
import requests
from pydantic import TypeAdapter
from config.config import Headers
from models.pet_model import PetListModel, PetModel, ApiResponseModel
from services.pet.pet_endpoints import PetEndpoints
from services.pet.pet_payloads import PetPayloads
from utils.helper import Helper
from utils.my_requests import MyRequests


class PetApi(Helper):
    def __init__(self):
        self.endpoints = PetEndpoints()
        self.payloads = PetPayloads()
        self.headers = Headers()

    @allure.step('Find pet by status')
    def find_pets_by_status(self, status_value):
        response = MyRequests.get(
            url=self.endpoints.find_pets_by_status,
            params={'status': status_value}
        )
        assert response.status_code == 200, f'{response.status_code}'
        self.attach_response(response.json())
        # model = PetListModel(items=response.json())
        # model = [PetModel(**i) for i in response.json()]
        ta = TypeAdapter(list[PetModel])
        model = ta.validate_python(response.json())
        return model

    @allure.step('Find pet by ID')
    def get_pet_by_id(self, pet_id):
        response = MyRequests.get(
            url=self.endpoints.find_pet_by_id(pet_id),
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    @allure.step('Find pet by not existent ID')
    def get_not_existent_pet(self, pet_id):
        response = MyRequests.get(
            url=self.endpoints.find_pet_by_id(pet_id),
        )
        assert response.status_code == 404, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Add a new pet to the store')
    def add_new_pet_to_the_store(self):
        response = MyRequests.post(
            url=self.endpoints.add_new_pet,
            json=self.payloads.add_new_pet
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    @allure.step('Upload an image')
    def upload_image(self, pet_id):
        response = requests.post(
            url=self.endpoints.upload_image(pet_id),
            files=self.payloads.upload_image,
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Update the name and status of an existed pet using form data')
    def update_name_and_status(self, pet_id):
        response = MyRequests.post(
            url=self.endpoints.update_pet_with_form_data(pet_id),
            data=self.payloads.update_name_and_status
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Update all pet data')
    def update_all_pet_data(self):
        response = MyRequests.put(
            url=self.endpoints.update_existing_pet,
            json=self.payloads.update_existing_pet
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = PetModel(**response.json())
        return model

    @allure.step('Delete pet from the store')
    def delete_pet_from_the_store(self, pet_id):
        response = MyRequests.delete(
            url=self.endpoints.delete_pet(pet_id),
            headers=self.headers.api_key
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model
