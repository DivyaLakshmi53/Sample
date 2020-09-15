from ecommerce_common.common_helpers.dbhelpers import DbHelpers

class Products_Dao(object):
    
    def __init__(self):
       
       self.prodao = DbHelpers()
       
    def get_all_products_from_db(self):
        
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product';"
        db_response = self.prodao.execute_select(sql)
        return db_response
        
   

        
        
    