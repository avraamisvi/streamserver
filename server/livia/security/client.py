
from tornado.httpclient import *
import os
import json

from urllib.parse import urlencode
from livia.config.serversconfig import UrlConfig

class SecurityClient(object):

	def __init__(self):
		self.http = HTTPClient()

	def decode(self, data):
		if data:
			return data.decode("utf-8")
		return None

	def check_token(self, code, token):
		response_data = None
		try:
			url = UrlConfig().get_security_token_url()
			headers = {'Content-Type': 'application/x-www-form-urlencoded'}
			
			post_data = { 'c': code, 't': token } #A dictionary of your post data
			body = urlencode(post_data) #Make it into a post request

			response = self.http.fetch(
			   HTTPRequest(url, 'POST', headers, body=body)
			   )
			response_data = self.decode(response.body)
		except HTTPError as e:
		    # HTTPError is raised for non-200 responses; the response
		    # can be found in e.response.
		    print("Error: " + str(e))
		except Exception as e:
		    # Other errors are possible, such as IOError.
		    print("Error: " + str(e))

		#self.http.close()
		return json.loads(response_data)
		
	def login(self, email, password):
		response_data = None
		try:
			url = UrlConfig().get_security_auth_url()
			headers = {'Content-Type': 'application/x-www-form-urlencoded'}
			
			post_data = { 'e': email, 'p': password } #A dictionary of your post data
			body = urlencode(post_data) #Make it into a post request

			response = self.http.fetch(
			   HTTPRequest(url, 'POST', headers, body=body)
			   )
			
			response_data = self.decode(response.body)
			
		except HTTPError as e:
		    # HTTPError is raised for non-200 responses; the response
		    # can be found in e.response.
		    print("Error: " + str(e))
		except Exception as e:
		    # Other errors are possible, such as IOError.
		    print("Error: " + str(e))

		#self.http.close()
		return json.loads(response_data)