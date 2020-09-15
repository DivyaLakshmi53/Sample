from woocommerce import API
import logging as logger
import json
from ecommerce_common.common_helpers.credentials_helper import CredentialsHelper
from ecommerce_common.common_helpers.dbhelpers import DbHelpers

class WooRequestHelpers(object):

    def __init__(self):

        cred_helper = CredentialsHelper()
        wc_cred = cred_helper.get_wc_credentials()
        db_cred = cred_helper.get_db_credentials()
        self.wcapi = API(
            url="http://mystore.local/", # Your store URL
            consumer_key=wc_cred['wc_key'], # Your consumer key
            consumer_secret=wc_cred['wc_secret'], # Your consumer secret
            wp_api=True, # Enable the WP REST API integration
            version="wc/v3" # WooCommerce WP REST API version
        )


    def assert_status_code(self):
        assert self.response.status_code == self.expected_status, "Bad status code " \
            "Endpoint: {}, Params: {}, Actual status code: {}. Expected status code: {}" \
            .format(self.endpoint, self.params, self.response.status_code, self.expected_status)
        print("Pass")

    def get(self, wc_endpoint, params=None, expected_status=200):

        self.response = self.wcapi.get(wc_endpoint, params=params)
        self.expected_status = expected_status
        self.endpoint = wc_endpoint
        self.params = params
        self.assert_status_code()
        return self.response.json()

    def post(self, wc_endpoint, data, expected_staus=201):

        self.response  = self.wcapi.post(wc_endpoint, data)
        self.expected_status = expected_staus
        self.endpoint = wc_endpoint
        #import pdb; pdb.set_trace() 
        self.assert_status_code()
        return self.response.json()
    
    def put(self, wc_endpoint, params, data, expected_status=200):

        self.response = self.wcapi.put(wc_endpoint, params, data)
        self.expected_status = expected_status
        self.endpoint = wc_endpoint
        self.assert_status_code()

if __name__ =='__main__':

    obj = WooRequestHelpers()
    #obj.get("products")
    #obj2 = DbHelper()
    #select_op = obj2.execute_select("select * from products")
    #print(select_op)
    
    data = {
        "name": "Ship Your Idea",
        "type": "variable",
        "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
        "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        "categories": [
            {
                "id": 9
            },
            {
                "id": 14
            }
        ],
        "images": [
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_4_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_4_back.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_3_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_3_back.jpg"
            }
        ],
        "attributes": [
            {
                "id": 6,
                "position": 0,
                "visible": False,
                "variation": True,
                "options": [
                    "Black",
                    "Green"
                ]
            },
            {
                "name": "Size",
                "position": 0,
                "visible": True,
                "variation": True,
                "options": [
                    "S",
                    "M"
                ]
            }
        ],
        "default_attributes": [
            {
                "id": 6,
                "option": "Black"
            },
            {
                "name": "Size",
                "option": "S"
            }
        ]
    }
    
    data1 = {
        "name": "Ship Your Idea",
        "type": "variable",
        "date_created": "2020-09-10T02:46:20",
        "date_created_gmt": "2020-09-10T02:46:20",
        "date_modified": "2020-09-10T02:46:20",
        "date_modified_gmt": "2020-09-10T02:46:20",
        "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
        "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        "categories": [
            {
                "id": 9
            },
            {
                "id": 14
            }
        ],
        "images": [
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_4_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_4_back.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_3_front.jpg"
            },
            {
                "src": "http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_3_back.jpg"
            }
        ],
        "attributes": [
            {
                "id": 6,
                "position": 0,
                "visible": False,
                "variation": True,
                "options": [
                    "Black",
                    "Green"
                ]
            },
            {
                "name": "Size",
                "position": 0,
                "visible": True,
                "variation": True,
                "options": [
                    "S",
                    "M"
                ]
            }
        ],
        "default_attributes": [
            {
                "id": 6,
                "option": "Black"
            },
            {
                "name": "Size",
                "option": "S"
            }
        ]
    }
    counter = 0
    data_json = dict(data)
    post_json1 = dict(data)
    print("")
    print(post_json1)
    for i, j in data_json.items():
        for x, value in post_json1.items():
            if i == j:
                if data_json[i] == post_json1[x]:
                    prink("looks good")
                else:
                    break
                    counter = counter+1
                    
    if counter != 0:
        print("")
        print("jsons don't match")
    else:
        print("json matches")    
                