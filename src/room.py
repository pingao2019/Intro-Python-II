
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__ (self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to=n_to
        self.s_to= s_to
        self.e_to= e_to
        self.w_to= w_to

  
    def __str__(self):
        return f"This is {self.name}, and {self.description}"



item_list= {'sword': Item("get "),
'gun':Item('drop'),
'knife': Item('take')
`lamp`: Item('on_drop')
`LightSource: Item('')}




























