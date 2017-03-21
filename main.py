import webapp2
import string

#rot 13 helper function from Unit 1, Ch. 12, Ex. 10.
def rot13(mess):

    idx=0
    codedText=""

    while idx < len(mess):
        if mess[idx] in string.ascii_lowercase:
            cipheredLetter = string.ascii_lowercase[(string.ascii_lowercase.find(mess[idx]) + 13) % 26]
            codedText += cipheredLetter
            idx += 1

        elif mess[idx] in string.ascii_uppercase:
            cipheredLetter = string.ascii_uppercase[(string.ascii_uppercase.find(mess[idx]) + 13) % 26]
            codedText += cipheredLetter
            idx += 1

        else:
            codedText += mess[idx]
            idx += 1

    return codedText

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
