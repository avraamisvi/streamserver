
import tornado.ioloop
import tornado.web
import tornado.gen
import os
import redis
import uuid
import datetime

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from livia.model.account import Account
from livia.model.base import Base

class SecurityService:

	def connect(self):
		self.redisService = SecurityRedisService().connect()
		self.rdbmsService = SecurityRDBMSService().connect()
		return self
	
	#O email sera usado como chave para achar o user
	def login(self, email, password):
		if self.rdbmsService.check_auth(email, password):
			code = self.rdbmsService.get_code(email)
			return True, code, self.redisService.create_token(code)

		return False, None, None

	def check_token(self, code, token):
		return self.redisService.check_token(code, token)

#Token service 
class SecurityRedisService:

	def connect(self):#TODO configurado
		self.connection = redis.StrictRedis(host='localhost', port=6379, db=0)#todo rever essa porta se nao deveria ficar em configuracao
		return self

	def check_token(self, code, token):
		local_token = self.connection.get(code).decode("utf-8")
		return  local_token == token

	#O email sera usado como chave para achar o user
	def create_token(self, codigo):
		uuidstr = str(uuid.uuid4())
		print(uuidstr)
		expire_at = datetime.timedelta(milliseconds=30*60000)
		self.connection.set(codigo, uuidstr, px=expire_at)
		return uuidstr

#Responsavel pela conexao com o banco de dados
class SecurityRDBMSService:

	def connect(self):
		self.engine = create_engine("mysql://root:123456@localhost/livia")#TODO configurado
		Base.metadata.bind = self.engine
		Session = sessionmaker(bind=self.engine)
		self.session = Session()
		return self
	
	#O email sera usado como chave para achar o user
	def check_auth(self, email, password):
		account = self.session.query(Account).filter(Account.Email == email).one()
		return account.Password == password

	def get_code(self, email):
		account = self.session.query(Account).filter(Account.Email == email).one()
		return account.Id