class Sheet(object):
    def __init__(self):
        self.content = ""

    def read(self):
        print(self.content)

    def write(self, content):
        self.content += content

    def erase(self):
        self.content = ""
