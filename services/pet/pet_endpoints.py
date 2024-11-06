from config.config import BASE_URL


class PetEndpoints:
    add_new_pet = f'{BASE_URL}/pet'
    upload_image = lambda self, pet_id: f'{BASE_URL}/pet/{pet_id}/uploadImage'
    update_existing_pet = f'{BASE_URL}/pet'
    find_pet_by_id = lambda self, pet_id: f'{BASE_URL}/pet/{pet_id}'
    find_pets_by_status = f'{BASE_URL}/pet/findByStatus'
    update_pet_with_form_data = lambda self, pet_id: f'{BASE_URL}/pet/{pet_id}'
    delete_pet = lambda self, pet_id: f'{BASE_URL}/pet/{pet_id}'
