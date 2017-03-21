import webapp2
import caesar

def build_page(textarea_content):
        #ACTION attirbute tells us WHERE we submit the form to
        #If there is no ACTION attirubte, the form sends an other http request to the same place it started
        #The METHOD attirbute is used here with the value, POST.
        #METHOD specifies which type of http request you want to send.
        #The default method is GET request.
        #Now that we have a POST REQUEST, we have set up a POST REQUEST HANDLER, other we get 405 error.

    message_label = "<label>Type a message: </label>"
    text_area = "<textarea name='message'>" + textarea_content + "</textarea>"

    rotation_label = "<label>Rotate by: </label>"
    rotation_input = "<input type='number' name='rotation' />"
    submit_button = "<input type='submit' />"

    form = ("<form method='post' >"
                + rotation_label + rotation_input
                + "<br><br>"
                + message_label + text_area
                + "<br><br>"
                + submit_button
                + "</form>")

    header = "<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)


    def post(self):
        #self.request.get is an attirbute of RequestHandler that allows us to access the GET request
        #in the case, the GET request is the text the user typed in, or the MESSAGE WE WANT TO ENCRYPT
        #self.request.get TAKES ONE ARGUMENT that is the KEYNAME
        #In English, it says, "get me the value of this key"
        #this made up key name corresponds to the VALUE the user inputs in the textarea
        #the key-value pair needs to be associated both in the post and get methods using a name attribute in the textarea tag

        rotation = int(self.request.get("rotation"))
        message = self.request.get("message")
        encrypted_message = caesar.encrypt(message, rotation)
        content = build_page(encrypted_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
