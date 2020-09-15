import pymysql
from ecommerce_common.common_helpers.credentials_helper import CredentialsHelper

class DbHelpers(object):

    def __init__(self):

        cred = CredentialsHelper()
        db_cred = cred.get_db_credentials()
        self.db_user = db_cred['db_user']
        self.db_password = db_cred['db_password']
        self.port = 10005
        self.host = 'localhost'

    def create_connection(self):

        self.connection = pymysql.connect(host=self.host, user=self.db_user, password=self.db_password, db='local', port=self.port)

    def execute_select(self, sql):
        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            result_dict = cur.fetchall()
        except Exception as e:
            print("Failed to connect/execute SQl {}, Exception thrown is {}".format(sql, str(e)))
        finally:
            cur.close()
        return result_dict
