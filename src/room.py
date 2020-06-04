
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


item_list= {'sword': Item("get "),
'gun':Item('drop'),
'knife': Item('take')
`lamp`: Item('on_drop')
`LightSource: Item('')}




























