
import tornado.ioloop
import tornado.web
import tornado.gen
import os
import json

from livia.services.securityservice import SecurityService

#Usado por todos os handles
security_service = SecurityService().connect() #TODO colocar isso no run e passar por parametro?

class AuthorizationService(tornado.web.RequestHandler):
	EMAIL_PAR = "e"
	PASS_PAR = "p"
	
	def get(self):
		self.post()

	def post(self):
		email_par = self.get_argument(self.EMAIL_PAR)
		pass_par  = self.get_argument(self.PASS_PAR)

		ok, code, token = security_service.login(email_par, pass_par)

		self.set_header("Content-Type", "text/json")            
		self.write(json.dumps({"status": ok, "code": str(code), "token": token}))
            

class TokenCheckerService(tornado.web.RequestHandler):

	TOKEN_PAR = "t"
	CODE_PAR =  "c"

	def get(self):
		self.post()

	def post(self):
		token_par = self.get_argument(self.TOKEN_PAR)
		code_par  = self.get_argument(self.CODE_PAR)

		ok = security_service.check_token(code_par, token_par)

		self.set_header("Content-Type", "text/json")
		self.write(json.dumps({"status": ok, "code": code_par, "token": token_par}))

class SecurityServer(object):

	def run(self):
		app = tornado.web.Application([
			(r"/security/token", TokenCheckerService),
			(r"/security/auth",  AuthorizationService)
		])
		app.listen(8100)#TODO Each server in its port 
		tornado.ioloop.IOLoop.current().start()