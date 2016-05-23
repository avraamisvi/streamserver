# things.py /home/abraaoisvi/Videos/repository/01/01/01/01.mp4

import tornado.ioloop
import tornado.web
import tornado.gen
import os

class VideoStreamerHandler(tornado.web.RequestHandler):

    CHUNK_SIZE = 512000         # 0.5 MB isso tem que ser calculado e tem q ter um limite
    authorized = False
    VIDEO_ID_PAR = "v"
    USER_TOKEN_PAR = "tk"

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.authorize()
        self.send_stream()

    def authorize(self):
        #TODO pesquisar no REDIS se o TOKEN eh valido tk=123456
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

def make_app():
    return tornado.web.Application([
        (r"/stream", VideoStreamerHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()