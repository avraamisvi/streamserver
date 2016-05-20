# things.py /home/abraaoisvi/Videos/repository/01/01/01/01.mp4

import tornado.ioloop
import tornado.web
import tornado.gen
import os

class FileStreamerHandler(tornado.web.RequestHandler):

    CHUNK_SIZE = 512000         # 0.5 MB isso tem que ser calculado e tem q ter um limite

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.set_header("Content-Type", "video/mp4")
        self.set_header("Content-Length", os.path.getsize("/home/abraaoisvi/Videos/repository/01/01/01/01.mp4"))
        self.flush()
        self.path = "/home/abraaoisvi/Videos/repository/01/01/01/01.mp4"

        fd = open(self.path, "rb")
        data = fd.read(self.CHUNK_SIZE)
        while data:
            self.write(data)
            yield tornado.gen.Task(self.flush)
            data = fd.read(self.CHUNK_SIZE)
        fd.close()
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/stream", FileStreamerHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()