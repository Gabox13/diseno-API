from datetime import datetime
class Message:
    def __init__(self,idM,sender, content, status,time,asunto):
        self.idM = idM
        self.sender = sender
        self.timestamp = time
        self.content = content
        self.status = status
        self.asunto = asunto

    def to_JSON(self):
        return {
            'idMessage': self.idM,
            'sender': self.sender,
            'timestamp': self.timestamp.isoformat(),
            'content': self.content,
            'status': self.status,
            'asunto':self.asunto
        }
