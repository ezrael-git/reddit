from components.__base__ import Base

class Date(Base):
    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    def __init__(self, day: int, month: int, year: int):
        super().__init__()
        self.day = day
        self.month = month
        self.year = year
    def into_str(self):
        return f"{self.day} {Date.MONTHS[self.month]} {self.year}"