class father:
    def eat(self):
        print("eating")
class son(father):
    pass
class grandfather:
    def skill(self):
        print("reading current affirs")
class father(grandfather):
    def fatherskill(self):
        print("makes money")
class son(father):
    def sonskill(self):
        print("1.tv watching\n2.sleepin\n3.reels\n3.studying")
#instance of son
son=son()
son.sonskill()
son.fatherskill()
son.skill()
