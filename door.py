class Door(object):
    def __init__(self, state = "closed"):
        self.state = state

    def open(self):
        if self.state == "opened":
            print "Door already opened!"
        else:
            self.state = "opened"
            print "Door opened!"

    def close(self):
        if self.state == "closed":
            print "Door already closed!"
        else:
            self.state = "closed"
            print "Door closed!"
