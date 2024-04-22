class Message:
    content = ""
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def get_sender(self):
        return self.sender
    def get_recipient(self):
        return self.recipient
    def append(self, content):
        self.content += "\n"+content
    def toString(self):
        return f"From: {self.sender}\nTo: {self.recipient}\n{self.content}"


message1 = Message("Harry Morgan", "Rudolf Reindeer")
message1.append("Merry Christmas")
message1.append("and a Happy New Year")
print(message1.toString())
