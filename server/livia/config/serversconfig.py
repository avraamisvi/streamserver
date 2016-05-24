#TODO criar um singelton
class UrlConfig(object):

	def get_security_token_url(self):
		return self.get_security_server_context() + self.get_security_token_path()

	def get_security_auth_url(self):
		return self.get_security_server_context() + self.get_security_auth_path()

	def get_stream_media_url(self):
		return self.get_stream_server_context() + self.get_security_media_path()

	def get_security_server_context(self):
		return "http://localhost:8100"
	
	def get_stream_server_context(self):
		return "http://localhost:8200"

	def get_security_token_path(self):
		return "/security/token"

	def get_security_auth_path(self):
		return "/security/auth"	

	def get_security_media_path(self):
		return "/stream/media"