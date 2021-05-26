"""
This file contains abstract classes of the army
"""

from abc import ABC, abstractmethod
from stack import ArrayStack
from my_queue import CircularQueue
from colours import Colours,BREAK_LINE

class Fighter(ABC):
    # LIFE=0
    # EXPERIENCE=0

    def __init__(self, life:int, experience:int)->None:
        if life >=0 and experience >=0 :
            self.LIFE = life
            self.EXPERIENCE = experience
        else:
            raise ValueError("life and experience must be greater than or equal to zero")

    def is_alive(self)->bool:
        return bool(self.LIFE > 0)

    def lose_life(self, lost_life:int):
        if lost_life >= 0:
            self.LIFE-=lost_life
        else:
            raise ValueError("lost_life must be greater than or equal to zero")

    def gain_experience(self, gained_experience:int)->None:
        if gained_experience >= 0:
            self.EXPERIENCE+=gained_experience
        else:
            raise ValueError("gained_experience must be greater than or equal to zero")

    def get_experience(self)->int:
        return self.EXPERIENCE

    @abstractmethod
    def get_speed(self)->int:
        pass

    @abstractmethod
    def get_speed(self)->int:
        pass

    @abstractmethod
    def get_cost(self)->int:
        pass

    @abstractmethod
    def attack_damage(self)->int:
        """
        :return: the amount of damage performed by the unit when it attacks
        """
        pass

    def defend(self, damage:int)->None:
        """
        decreases the life of the unit by the amount lost (if any) after defending from an attack that inflicted
        the amount of damage indicated by damage
        """
        if damage < 0:
            raise ValueError("damage must be greater than or equal to zero")

    def __str__(self)->str:
        return "{}'s {}life = {} {}and {}experience = {}{}".format(type(self).__name__, Colours.OKGREEN, self.LIFE,
                                                                     Colours.ENDC, Colours.FAIL, self.EXPERIENCE,
                                                                     Colours.ENDC)



class Soldier(Fighter):
    COST = 1
    def __init__(self)->None:
        Fighter.__init__(self,3,0)

    def get_speed(self) ->int:
        return 1+self.EXPERIENCE

    def get_cost(self) ->int:
        return self.COST

    def attack_damage(self) ->int:
        return 1+self.EXPERIENCE

    def defend(self, damage:int) ->None:
        Fighter.defend(self, damage)
        if damage> self.EXPERIENCE:
            self.lose_life(1)


class Archer(Fighter):
    COST = 2
    SPEED = 3

    def __init__(self)->None:
        Fighter.__init__(self,3,0)

    def get_speed(self) ->int:
        return self.SPEED

    def get_cost(self) ->int:
        return self.COST

    def attack_damage(self) ->int:
        return 1+self.EXPERIENCE

    def defend(self, damage:int) ->None:
        Fighter.defend(self, damage)
        self.lose_life(1)


class Cavalry(Fighter):
    COST = 3
    SPEED = 2

    def __init__(self):
        Fighter.__init__(self, 4,0)

    def get_cost(self) ->int:
        return self.COST

    def get_speed(self) ->int:
        return self.SPEED

    def attack_damage(self) ->int:
        return 2 * self.EXPERIENCE + 1

    def defend(self, damage:int) ->None:
        Fighter.defend(self, damage)
        if damage> (self.EXPERIENCE / 2):
            self.lose_life(1)



class Army:
    BUDGET = 30

    def __init__(self):
        self.name = None
        self.force = None

    def __correct_army_given(self, s, a, c):

        purchase_cost = s * Soldier.COST + a * Archer.COST + c * Cavalry.COST
        remaining_budget = (self.BUDGET - purchase_cost)
        # self.budget = remaining_budget
        return bool(remaining_budget >= 0)

    def __assign_army(self, name: str, s: int, a: int, c: int, formation: int):
        force_size = s + a + c
        self.name = name
        if formation == 0:
            self.force = ArrayStack(force_size)
            # push Cavalry into the force
            for i in range(c):
                self.force.push(Cavalry())
            # push Archers into the force
            for i in range(a):
                self.force.push(Archer())
            # push Soldiers into the force
            for i in range(s):
                self.force.push(Soldier())
        else:
            self.force = CircularQueue(force_size)
            # append Soldiers into the force
            for i in range(s):
                self.force.append(Soldier())
            # append Archers into the force
            for i in range(a):
                self.force.append(Archer())
            # append Cavalry into the force
            for i in range(c):
                self.force.append(Cavalry())



    def choose_army(self, name: str, formation: int) -> None:

        flag = True
        while flag:
            print("Player {} choose your army as S A C".format(name))
            print("where S is the number of Soldiers\n\t  A is the number of Archers\n\t  C is the number of Cavalry")
            given_army = input("Enter :")
            try:
                given_army = given_army.strip().split()
                n = len(given_army)
                if n == 3:
                    for i in range(n):
                        given_army[i] = int(given_army[i])
                else:
                    raise Exception("Invalid, input must consist of three integers")
                s, a, c = given_army
            except Exception as e:
                print(e)
                print(BREAK_LINE)
            else:
                if self.__correct_army_given(s, a, c):
                    self.__assign_army(name, s, a, c, formation)
                    flag = False
                else:
                    print("Army you chose is invalid")
                    print(BREAK_LINE)

    def __str__(self):
        return self.force
