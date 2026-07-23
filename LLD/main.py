from abc import ABC, abstractmethod

class Platform:
    def __init__(self, platform_name, rate_limiting):
        self.platform_name = platform_name
        self.rate_limiting = rate_limiting

class Brand:
    def __init__(self, brand_name, email, **kwargs):
        self.brand_name = brand_name
        self.email = email
        if "stores" in kwargs:
            self.stores = kwargs["stores"]
        if "platforms" in kwargs:
            self.platforms = kwargs["platforms"]

    def add_platform(self, platform):
        self.platforms.append(platform)
    def add_store(self, store):
        self.stores.append(store)

class Store:
    def __init__(self, store_name, brand_name, platform) -> None:
        self.store_name = store_name
        self.brand_name = brand_name
        self.platform = platform



class LoginUsername:
    def __init__(self, brand, platform, username, password) -> None:
        self.brand = brand
        self.platform = platform
        self.username = username
        self.password = password
        self.cookie = None

class CHARGEBACKTYPE:
    WRONG_ORDER = "wrong_order" 
    MISSING_ITEMS = "missing_items"
    CANCELLED = "cancelled"


order_details = [{}]
    
        



class AutomatedChargeBackDisputes:
    def process_order(self):
        disputed_orders = []
        for order in order_details:
            if order["has_error"]:
                disputed_orders.append(order)

        disputed_order = filter_by_brand_platform(order)

        for order in disputed_orders:
n




class DisputeStrategy(ABC):
    @abstractmethod
    def is_dispute(self, dispute_orders):
        pass


class FirstBatchStrategy(DisputeStrategy):
    def raise_dispute_orders(self, dispute_orders):
        return dispute_orders

registry_order_charged_back_per_store = {}

class ConfigForParsing:
    platform : string
    config_json = { {key : str, value: , operator: }}

class AmountBasedStrategy(DisputeStrategy):
    def raise_dispute_orders(self, dispute_orders):
        raise_dispute_orders_list = []
        for order in dispute_orders:
            store = order["store"]
            platform = store.platform
            config = ConfigForParsing.get(platform)

            is_valid = is_valid_for_raising_dispute(config, order)
            if is_valid:
                raise_dispute_orders_list.append(order)


            # for key, value in config.items():
            #     # check how we want to filer
            #     if order["key"] 

            # if order["amount"] > 50:
            #     raise_dispute_orders_list.append(dispute_orders)
        return raise_dispute_orders_list



# rest, http, email...
# 



class username_password_RestAPI()
Class login_username_lgin_passwordSwiggyRestAPI()


class LoginStratgeis(ABC)

class ZomatoRestAPILoginAdapter(LoginStratgeis):
    zomato_api_oject = ZomamtoRestAPI()
    def set_username(self):
        self.usenrame
    def set_password()
    def login()
        zomato_api_oject ("username" : username)


class HTTP


class ZomatoLogin:
    
        

adapter(username, password, )
 intetr()
def lo

