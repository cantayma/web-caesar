import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):

        text_area = "<textarea name='message'></textarea>"
        submit_button = "<input type='submit' />"                                               #creates a button that, when it is clicked,causes the form to submit
        form = "<form method='post' >" + text_area + "<br><br>" + submit_button + "</form>"     #ACTION attirbute tells us WHERE we submit the form to
                                #If there is no ACTION attirubte, the form sends an other http request to the same place it started
                                #The METHOD attirbute is used here with the value, POST.
                                #METHOD specifies which type of http request you want to send.
                                #The default method is GET request.
                                #Now that we have a POST REQUEST, we have set up a POST REQUEST HANDLER, other we get 405 error.

        self.response.write(form)

    def post(self):
        message = self.request.get("message")       #self.request.get is an attirbute of RequestHandler that allows us to access the GET request
                                                    #in the case, the GET request is the text the user typed in, or the MESSAGE WE WANT TO ENCRYPT
                                                    #self.request.get TAKES ONE ARGUMENT that is the KEYNAME
                                                    #In English, it says, "get me the value of this key"
                                                    #this made up key name corresponds to the VALUE the user inputs in the textarea
                                                    #the key-value pair needs to be associated both in the post and get methods using a name attribute in the textarea tag

        rot_value = 13
        encrypted_message = caesar.encrypt(message, rot_value)

        self.response.write("Secret Message: " + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
