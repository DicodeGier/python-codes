class Message:
    def __init__(self, _sender, _recipient):
        self.sender = _sender
        self.recipient = _recipient
        self.message = ""

    def append(self, text):
        self.message += str(text)

    def toString(self):
        return("From: {} To: {} {}".format(self.sender, self.recipient, self.message))

testmessage = Message('Dico', 'Anniek')
testmessage.append("kijk daar zit flapper")
print(testmessage.toString())

class Mailbox:
    def __init__(self):
        self.mailbox = []

    def addMessage(self):
        self.message = testmessage.toString()
        self.mail.box.append(self.message)

    def getMessage(self, index):
        return self.mailbox[index]

    def removeMessage(self, index):
        self.mailbox.pop(index)

testmessage = Message('Dico', 'Anniek')
testmessage.append("kijk daar zit flapper")
print(testmessage.toString())


    