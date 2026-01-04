class Zoo:
    def animal(self):
        print("Zoo has different animals")


class Lion(Zoo):
    def animal(self):
        super().animal()   
        print("Lion is the king of the jungle")


li = Lion()
li.animal()