import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):

        message = "Hello, World!"
        rot_value = 13

        self.response.write(caesar.encrypt(message, rot_value))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
