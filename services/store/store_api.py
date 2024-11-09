import allure
from models.store_model import OrderModel, ApiResponseModel
from services.store.store_endpoints import StoreEndpoints
from services.store.store_payloads import StorePayloads
from utils.helper import Helper
from utils.my_requests import MyRequests


class StoreApi(Helper):
    def __init__(self):
        self.endpoints = StoreEndpoints()
        self.payloads = StorePayloads()

    @allure.step('Place order')
    def place_order(self):
        response = MyRequests.post(
            url=self.endpoints.place_order,
            json=self.payloads.place_order
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = OrderModel(**response.json())
        return model

    @allure.step('Find order by ID')
    def get_order_by_id(self, order_id):
        response = MyRequests.get(
            url=self.endpoints.find_order_by_id(order_id)
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = OrderModel(**response.json())
        return model

    @allure.step('Find order by not existent ID')
    def get_not_existent_order(self, order_id):
        response = MyRequests.get(
            url=self.endpoints.find_order_by_id(order_id)
        )
        assert response.status_code == 404, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model

    @allure.step('Delete order by ID')
    def delete_order_by_id(self, order_id):
        response = MyRequests.delete(
            url=self.endpoints.delete_order_by_id(order_id)
        )
        assert response.status_code == 200, f'{response.status_code} {response.text}'
        self.attach_response(response.json())
        model = ApiResponseModel(**response.json())
        return model
