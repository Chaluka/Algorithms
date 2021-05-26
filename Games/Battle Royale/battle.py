
from stack import ArrayStack
POP = ArrayStack.pop
PUSH = ArrayStack.push
from army import Fighter,Soldier, Archer, Cavalry, Army
from colours import Colours,BREAK_LINE


class Battle:

    def __init__(self):
        self.army1 = None
        self.army2 = None

    def __fare_fight(self,army1: Army, army2:Army, GET1, GET2, PUT1, PUT2)->None:
        """ Both players attacks at the same time as their speed is same"""
        U1 = GET1()
        U2 = GET2()

        damage_on_fighter2 = U1.attack_damage()
        damage_on_fighter1 = U2.attack_damage()
        print("{}{}{}: {} attacks".format(Colours.PLAYER1, army1.name, Colours.ENDC, U1))
        print("{}{}{}: {} attacks".format(Colours.PLAYER2, army2.name, Colours.ENDC, U2))

        U1.defend(damage_on_fighter1)
        U2.defend(damage_on_fighter2)
        print("Both defend them selves")
        # if both are alive then both lose a life
        if U1.is_alive() and U2.is_alive():
            print("{}{}{}: {} and {}{}{}: {} both are alive ".format(Colours.PLAYER1,army1.name,Colours.ENDC,U1,Colours.PLAYER2, army2.name, Colours.ENDC,U2))
            U1.lose_life(1)
            PUT1(U1)

            U2.lose_life(1)
            PUT2(U2)
            print("Both lost life, Added back to the force")
        # if fighter1 is alive
        elif U1.is_alive() and not U2.is_alive():
            U1.gain_experience(1)
            print("{}{}{}: {} killed {}{}{}: {} ".format(Colours.PLAYER1, army1.name, Colours.ENDC, U1, Colours.PLAYER2,
                                                         army2.name, Colours.ENDC, U2))
            print("Added back to the force")
            PUT1(U1)

        elif U2.is_alive() and not U1.is_alive():
            print("{}{}{}: {} killed {}{}{}: {} ".format(Colours.PLAYER2,army2.name,Colours.ENDC,U2, Colours.PLAYER1, army1.name, Colours.ENDC,U1))
            U2.gain_experience(1)
            print("Added back to the force")
            PUT2(U2)
        else:
            print("Both are dead.!")

    def __fight(self,army1: Army, army2:Army, GET1, GET2, PUT1, PUT2)->None:
        """ army1 has the fastest unit such that it attack first"""

        U1 = GET1()
        U2 = GET2()

        print("{}{}{}: {} attacks".format(Colours.PLAYER1,army1.name, Colours.ENDC, U1))
        damage_on_fighter2 = U1.attack_damage()
        U2.defend(damage_on_fighter2)
        # fighter2 can fight only if he is alive
        if U2.is_alive():
            print("{}{}{}: {} is alive".format(Colours.PLAYER2, army2.name,Colours.ENDC,U2))
            print("{}{}{}: {} attacks".format(Colours.PLAYER2, army2.name,Colours.ENDC,U2))
            damage_on_fighter1 = U2.attack_damage()
            U1.defend(damage_on_fighter1)
            #if U1 has servived, then both added back into forces back. No one gain experience
            if U1.is_alive():
                print("{}{}{}: {} is alive".format(Colours.PLAYER1,army1.name,Colours.ENDC,U1))
                PUT1(U1)
                PUT2(U2)
            #if U1 is dead, then only the U2 is added back. U2 gain experience
            else:
                print("{}{}{}: {} is dead".format(Colours.PLAYER1,army1.name,Colours.ENDC,U1))
                U2.gain_experience(1)
                PUT2(U2)
        # if U2 is dead, then U1 doesn't have to fight. U1 gain experience and
        # added back into the force
        else:
            print("{}{}{}: {} is dead".format(Colours.PLAYER2, army2.name,Colours.ENDC, U2))
            U1.gain_experience(1)
            PUT1(U1)


        # U1 = army1.force.peek()
        # U2 = army2.force.peek()
        #
        # if U1.is_alive() and not U2.is_alive():
        #     U1.gain_experience(1)
        # elif U2.is_alive() and not U1.is_alive():
        #     U2.gain_experience(1)

    def __conduct_combat(self, army1: Army, army2:Army, formation:int )->int:

        #if formation==1 then we access a queue, otherwise a stack. Thus, we change the fucntions been used
        if formation:
            GET1 = army1.force.serve
            GET2 = army2.force.serve
            PUT1 = army1.force.append
            PUT2 = army2.force.append
        else:
            GET1 = army1.force.pop
            GET2 = army2.force.pop
            PUT1 = army1.force.push
            PUT2 = army2.force.push

        while not army1.force.is_empty() and not army2.force.is_empty():

            U1 = army1.force.peek()
            U2 = army2.force.peek()
            print(BREAK_LINE)
            # if both have same speed then both attack at the same time
            if U1.get_speed() == U2.get_speed():
                print("{}{}{}: Army1 and {}{}{}: Army2 has same speed ".format(Colours.PLAYER1, army1.name, Colours.ENDC, Colours.PLAYER2,army2.name, Colours.ENDC))
                self.__fare_fight(army1, army2, GET1 , GET2, PUT1, PUT2)
            # if fighter two is fast then he attacks first
            elif U1.get_speed() > U2.get_speed():
                print("{}{}{}: Army1 attack first on {}{}{}: Army2".format(Colours.PLAYER1,army1.name,Colours.ENDC, Colours.PLAYER2,army2.name,Colours.ENDC))
                self.__fight(army1,army2, GET1, GET2, PUT1, PUT2)
            else:
                print("{}{}{}: Army2 attack first on {}{}{}: Army1".format(Colours.PLAYER2, army2.name, Colours.ENDC, Colours.PLAYER1, army1.name, Colours.ENDC))
                self.__fight(army2,army1,GET2,GET1,PUT2,PUT1)
        status = 0
        if not army1.force.is_empty() and army2.force.is_empty():
            status = 1
        elif not army2.force.is_empty() and army1.force.is_empty():
            status = 2

        return status


    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        army1 = Army()
        army2 = Army()

        #read and form an army for player1
        army1.choose_army(player_one,0)
        # read and form an army for player2
        army2.choose_army(player_two, 0)

        status = self.__conduct_combat(army1,army2,0)
        print("\n")
        print(BREAK_LINE)
        if status==0:
            print("\t\tBattle is drawn")
        elif status==1:
            print("\t\tPlayer 1: {}{}{} won the battle".format(Colours.PLAYER1, army1.name, Colours.ENDC))
        else:
            print("\t\tPlayer 2: {}{}{} won the battle".format(Colours.PLAYER2, army2.name, Colours.ENDC))

        print(BREAK_LINE)
        return status


    def fairer_combat(self, player_one: str, player_two: str) -> int:
        army1 = Army()
        army2 = Army()

        #read and form an army for player1
        army1.choose_army(player_one,1)
        # read and form an army for player2
        army2.choose_army(player_two, 1)

        status = self.__conduct_combat(army1,army2,1)
        print("\n")
        print(BREAK_LINE)
        if status==0:
            print("\t\tBattle is drawn")
        elif status==1:
            print("\t\tPlayer 1: {}{}{} won the battle".format(Colours.PLAYER1, army1.name, Colours.ENDC))
        else:
            print("\t\tPlayer 2: {}{}{} won the battle".format(Colours.PLAYER2, army2.name, Colours.ENDC))

        print(BREAK_LINE)
        return status



if __name__ == "__main__":

    b = Battle()
    # b.gladiatorial_combat("Peter", "John")
    b.fairer_combat(123, "John")
