# things.py 

# Let's get this party started!
import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class VideosResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.stream = open('/home/abraaoisvi/Videos/repository/01/01/01/01.mp4', 'rb')
        print('teste')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
videos = VideosResource()

# things will handle all requests to the '/things' URL path
app.add_route('/videos', videos)