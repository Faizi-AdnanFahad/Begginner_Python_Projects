class Instructor:

    def __init__(self, name, ext, email):
        self.name = name
        self.ext = ext
        self.email = email

    def getName(self):
        return self.name

    def getPhoneExtension(self):
        return self.ext

    def getEmail(self):
        return self.email

    def getInformation(self):
        return f"{self.name} has campus phone extension {self.ext} and contact email {self.email}"

    def setName(self, newName):
        self.name = newName

    def setPhoneExtension(self, nexExt):
        self.ext = nexExt

    def setEmail(self, newEmail):
        self.email = newEmail
