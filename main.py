import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):

        message = "Hello, World!"
        rot_value = 13
        encrypted_message = caesar.encrypt(message, rot_value)

        text_area = "<textarea>" + encrypted_message + "</textarea>"
        submit_button = "<input type='submit' />"                            #creates a button that, when it is clicked,causes the form to submit
        form = "<form>" + text_area + "<br><br>" + submit_button + "</form>"

        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
