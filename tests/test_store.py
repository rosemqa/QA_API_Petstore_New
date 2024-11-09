import allure
from config.base_test import BaseTest


@allure.epic('Store cases')
class TestStore(BaseTest):
    @allure.description('Can place an order')
    def test_place_order(self):
        # PLACE ORDER
        place_order = self.store_api.place_order()
        order_id = place_order.id

        # GET ORDER BY ID
        order = self.store_api.get_order_by_id(order_id)
        assert order == place_order, 'Check order data'

    @allure.description('Can delete an order')
    def test_delete_order(self):
        # PLACE ORDER
        place_order = self.store_api.place_order()
        order_id = place_order.id

        # DELETE ORDER BY ID
        delete = self.store_api.delete_order_by_id(order_id)
        assert delete.message == str(order_id), "Check order ID in the response message when deleting"

        # VERIFY THAT ORDER INFORMATION DOESN'T RETURN
        order = self.store_api.get_not_existent_order(order_id)
        assert order.message == 'Order not found', 'Check error message when get order info by ID'
