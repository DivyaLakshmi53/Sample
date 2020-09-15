from ecommerce_common.common_helpers.woo_request_helpers import WooRequestHelpers


        
def list_all_products():
        
    params = {'per_page' : '100'}
    response = WooRequestHelpers().get('products', params=params)
    return response
