import allure
import pytest
from config.base_test import BaseTest
from services.pet.pet_payloads import PetPayloads


@allure.epic('Pet cases')
class TestPet(BaseTest):
    @allure.description('Filtering by status returns the pets with the given status')
    @pytest.mark.parametrize('status', ['available', 'sold', 'pending'])
    def test_find_pets_by_status(self, status):
        pets = self.pet_api.find_pets_by_status(status)
        for pet in pets:
            assert pet.status == status, 'Status value in the response does not match the given status'

    @allure.description('Can add a new pet to the store')
    def test_add_new_pet_to_the_store(self):
        # ADD A NEW PET
        pet = self.pet_api.add_new_pet_to_the_store()
        assert pet.model_dump() == PetPayloads.add_new_pet, 'The response json does not match the request json'

        # VALIDATE THAT A NEW PET WAS ADDED AND EXISTS IN THE PET LIST
        pet_status = PetPayloads.add_new_pet['status']
        pet_list = self.pet_api.find_pets_by_status(pet_status)
        assert pet in pet_list, "Pet not found in the pet list"

        # GET PET INFO BY PET ID (Find pet by ID)
        assert pet == self.pet_api.get_pet_by_id(pet.id), 'Check pet info by ID'

    @allure.description('Can upload image and additional image data')
    def test_upload_image(self):
        pet_id = 102030  # can accept non existent ID
        pet = self.pet_api.upload_image(pet_id)
        data_text = PetPayloads.upload_image['additionalMetadata']
        image = PetPayloads.image.split('/')[1]
        assert data_text and image in pet.message, 'Image name or additional data is missing in response message'

    @allure.description('Can update the name and status of an existed pet using form data')
    def test_update_name_and_status(self, check):
        # ADD A NEW PET
        pet = self.pet_api.add_new_pet_to_the_store()
        pet_id = pet.id

        # EDIT THE PET NAME AND STATUS
        edit_pet = self.pet_api.update_name_and_status(pet_id)
        assert edit_pet.message == f'{pet_id}', "Check pet ID in the response message when editing"

        # GET PET INFO
        updated_pet = self.pet_api.get_pet_by_id(pet_id)
        with check:
            assert updated_pet.name == PetPayloads.update_name_and_status['name'], 'Name not updated'
        with check:
            assert updated_pet.status == PetPayloads.update_name_and_status['status'], 'Status not updated'

    @allure.description('Can update an existing pet via json')
    def test_update_all_pet_data(self):
        # ADD A NEW PET
        pet = self.pet_api.add_new_pet_to_the_store()
        pet_id = pet.id

        # UPDATE PET DATA
        edit_pet = self.pet_api.update_all_pet_data()
        assert edit_pet.model_dump() == PetPayloads.update_existing_pet, 'Check response for PUT request'

        # GET PET INFO
        updated_pet = self.pet_api.get_pet_by_id(pet_id)
        assert updated_pet == edit_pet, 'Pet data not updated'

    @allure.description('Can delete the pet from the store')
    def test_delete_pet_from_the_store(self):
        # ADD A NEW PET
        pet = self.pet_api.add_new_pet_to_the_store()
        pet_id = pet.id
        pet_status = PetPayloads.add_new_pet['status']

        # DELETE PET
        delete_pet = self.pet_api.delete_pet_from_the_store(pet_id)
        assert delete_pet.message == f'{pet_id}', "Check pet ID in the response message when deleting"

        # Validate that the pet was deleted from the pet list
        pet_list = self.pet_api.find_pets_by_status(pet_status)
        assert pet not in pet_list, "Pet was not deleted from the pet list"

        # Verify that pet information doesn't return
        deleted_pet = self.pet_api.get_not_existent_pet(pet_id)
        assert deleted_pet.message == 'Pet not found', 'Check error message when get pet info by ID'
