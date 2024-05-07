class children:
    def set_children(self, children):
        self.children=children
    def getchildren(self):
        return self.children
    
children=children()
children.set_children(int(input("Enter the number of children you have: ")))
print(children.getchildren())
