# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name= name
        self.current_room= current_room

    def __str__(self):
        return f"{self.name}, you are at {self.room.name} now. \n{self.room.description}"


players={'captain': Room['floyer'],
'monster':Room['treasure']}


class monster:
    def __init__(self):
       pass
    def on_attack(self):
        return 