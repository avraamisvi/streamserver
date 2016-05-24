
import tornado.ioloop
import tornado.web
import tornado.gen
import os
import redis
import uuid
import datetime

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from livia.model.media import Media

#Usado pelo servidor de midia e stream basicamente

"""Servico de midia, acessa os dados no banco relativos a midia, como tipo, categoria, e midia
"""
class MediaService(object):

	def __init__(self, session):
		self.session = session

	def list_media(self, filter):
		return None
	
	def list_category(self, filter):
		return None

	def list_type(self, filter):
		return None

	def list_session(self, filter):
		return None

	def get_category(self, id):
		return None

	def get_type(self, id):
		return None

	def get_session(self, id):
		return None

	def get_media(self, id):
		return None

"""Servico de repositorio, acessa o aquivo pela media
"""
class FileService(object):

	def __init__(self):
		self.repository_path = '/home/abraaoisvi/streamer/repository'

	def get_file(self, media):
		return None