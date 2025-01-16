from components.__base__ import Base

class Attachment(Base):
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.attrs = kwargs.get("attrs")