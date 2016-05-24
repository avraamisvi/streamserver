# things.py /home/abraaoisvi/Videos/repository/01/01/01/01.mp4

import tornado.ioloop
import tornado.web
import tornado.gen
import os

from livia.services.mediaservice import MediaService
from livia.services.mediaservice import FileService

from livia.security.client import SecurityClient

class VideoStreamerHandler(tornado.web.RequestHandler):

    CHUNK_SIZE = 512000         # 0.5 MB isso tem que ser calculado e tem q ter um limite
    authorized = False
    VIDEO_ID_PAR =   "v"
    USER_TOKEN_PAR = "t"
    USER_CODE_PAR =  "c"

    def __init__(self):
        self.security_client = SecurityClient()
        self.media_service = MediaService()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.authorize()
        self.send_stream()

    def authorize(self):
        #TODO pesquisar no REDIS se o TOKEN eh valido tk=123456
        self.token = self.get_argument(self.USER_TOKEN_PAR)
        self.user_code = self.get_argument(self.USER_TOKEN_PAR)

        self.security_client.check_token(self.user_code, self.token)

        self.authorized = True

    def get_media(self, media_id):
        #TODO obter essa informacao do servidor de media
        return "/home/abraaoisvi/streamer/repository/01/01/01/01.mp4"

    @tornado.web.asynchronous
    @tornado.gen.engine
    def send_stream(self):
        if self.authorized:
            media = self.get_media(self.get_argument(self.VIDEO_ID_PAR))
            self.set_header("Content-Type", "video/mp4")
            self.set_header("Content-Length", os.path.getsize(media))
            self.flush()

            fd = open(media, "rb")
            data = fd.read(self.CHUNK_SIZE)
            while data:
                self.write(data)
                yield tornado.gen.Task(self.flush)
                data = fd.read(self.CHUNK_SIZE)
            fd.close()
            self.finish()

class StreamServer(object):

    def run(self):
        app = tornado.web.Application([
            (r"/stream/media", VideoStreamerHandler)
        ])
        app.listen(8200)#TODO Each server in its port 
        tornado.ioloop.IOLoop.current().start()