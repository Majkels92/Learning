import characters


class MarhabaDesert:
    @staticmethod
    def entrance_description():
        print("""You enter area where You can only see sand and sand dunes, the sky is clear but it's terribly hot,
        you are sweating and thinking 'why would I ever come to this sandy hell'...""")


class Forest:
    @staticmethod
    def entrance_description():
        print("""Pleasant wind is blowing, You hear birds singing and trees cracking while moving from left to right,
        unfortunately despite of friendly atmosphere you can feel it in the air, that something is wrong with
        this forest...""")


class DarkCave:
    @staticmethod
    def entrance_description():
        print("""The cave with barely visible entrance, looks very interesting. Probably long time nobody seen what is
        inside. It's solid location to start searching some undiscovered treasures...but is it safe? You can sense 
        there is for sure a reason why nobody wants to explore this place. """)


class Camp:
    @staticmethod
    def entrance_description():
        print("""You have returned to safe camp where u can finally rest from everyday struggle of adventurer! """)


class LocationPaths:
    @staticmethod
    def easy_encounter():
        enemy = characters.EasyMonster()
        print(f"You enforced {enemy._name} let's KILL HIM!")
        return enemy

    @staticmethod
    def medium_encounter():
        enemy = characters.MediumMonster()
        print(f"You enforced {enemy._name} let's KILL HIM!")
        return enemy

    @staticmethod
    def hard_encounter():
        enemy = characters.HardMonster()
        print(f"You enforced {enemy._name} let's KILL HIM!")
        return enemy
