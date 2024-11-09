from config.config import BASE_URL


class StoreEndpoints:
    returns_pet_inventories_by_status = f'{BASE_URL}/store/inventory'
    place_order = f'{BASE_URL}/store/order'
    find_order_by_id = lambda self, order_id: f'{BASE_URL}/store/order/{order_id}'
    delete_order_by_id = lambda self, order_id: f'{BASE_URL}/store/order/{order_id}'
