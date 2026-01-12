class Vrchol:
    """vrchol binárního stromu"""

    def __init__(self, x=None):
        self.info = x  # uložená hodnota
        self.levy = None  # levý syn
        self.pravy = None  # pravý syn

    def preorder(self):
        """průchod stromem s kořenem v tomto vrcholu
        metodou preorder, vypisuje hodnoty všech
        vrcholů
        """
        print(self.info, end="")
        if self.levy is not None:
            self.levy.preorder()
        if self.pravy is not None:
            self.pravy.preorder()

    def inorder(self):
        """průchod stromem s kořenem v tomto vrcholu
        metodou inorder, vypisuje hodnoty všech
        vrcholů"""
        if self.levy is None: # je to list
            print(self.info, end='')
        else: # není to list
            print('(', end='')
            self.levy.inorder()
            print(self.info, end='')
            self.pravy.inorder()
            print(')', end='')

    def postorder(self):
        """průchod stromem s kořenem v tomto vrcholu
        metodou postorder, vypisuje hodnoty všech
        vrcholů"""
        if self.levy is not None:
            self.levy.postorder()
        if self.pravy is not None:
            self.pravy.postorder()
        print(self.info, end="")

    def vyraz(self):
        """vyhodnocení aritmetického výrazu reprezentovaného
        binárním stromem s kořenem v tomto vrcholu
        """
        if self.levy is None:  # list
            return self.info
        elif self.info == '+':
            return self.levy.vyraz() + self.pravy.vyraz()
        elif self.info == '-':
            return self.levy.vyraz() - self.pravy.vyraz()
        elif self.info == '*':
            return self.levy.vyraz() * self.pravy.vyraz()
        elif self.info == '/':
            return self.levy.vyraz() / self.pravy.vyraz()


v = Vrchol('*')
v.levy = Vrchol('+')
v.levy.levy = Vrchol(2)
v.levy.pravy = Vrchol(5)
v.pravy = Vrchol('-')
v.pravy.levy = Vrchol(13)
v.pravy.pravy = Vrchol(4)
print(v.vyraz())
v.preorder()
print()
v.inorder()
print()
v.postorder()
