from behave import step, given, when, then
from ecommerce_common.common_api_calls import products_rest_api
from ecommerce_common.common_dao.products_dao import Products_Dao

@given("I execute get all products rest api")
def i_execute_get_all_products_rest_api(context):
    
    products_api = products_rest_api.list_all_products()
    context.pc_api = len(products_api)
    
@when("I get all products from db")
def i_get_all_products_from_db(context):
    
    products_db = Products_Dao().get_all_products_from_db()
    context.pc_db = len(products_db)
    
@then("Total no of products in get call matches products count from db")
def total_no_of_products_in_get_call_matches_products_count_from_db(context):
    
    assert context.pc_db == context.pc_api, "Total no. of products {} in db, doesn't match total no.of products{} in api" \
           .format(context.pc_db, context.pc_api) 
    
          
        
    