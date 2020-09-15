import os

class CredentialsHelper(object):

	def get_db_credentials(self):

		db_user = os.environ.get('DB_USER')
		db_password = os.environ.get('DB_PASSWORD')

		if not db_user or not db_password:
			raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be set as env variables")
		else:
			return {'db_user': db_user, 'db_password': db_password}

	def get_wc_credentials(self):
		consumer_key = os.environ.get('WC_KEY')
		print("consumer_key {}".format(consumer_key))
		consumer_secret = os.environ.get('WC_SECRET')
		print("consumer_secret {}".format(consumer_key))
		if not consumer_key or not consumer_secret:
			raise Exception("The Woocommerce 'WC_KEY' & 'WC_SECRET' must be set as env variables")
		else:
			return {'wc_key': consumer_key, 'wc_secret': consumer_secret}
			
if __name__ == '__main__':

	obj = CredentialsHelper()
	print(obj.get_db_credentials())