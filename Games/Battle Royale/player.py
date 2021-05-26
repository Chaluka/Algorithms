# """
# Implementation of Player Class
# """
#
# from stack import ArrayStack
# from army import Soldier, Archer, Cavalry
# import enum
#
#
# BREAK_LINE = '-'*30
#
# # class Formation(enum.Enum):
# #     Stack = 0
# #     Queue = 1
#
# class Player:
#     budget=30
#     def __init__(self):
#         self.name = None
#         self.force = None
#
#     def __correct_army_given(self, s, a, c):
#
#         purchase_cost = s*Soldier.cost + a*Archer.cost + c*Cavalry.cost
#         remaining_budget = (self.budget-purchase_cost)
#         # self.budget = remaining_budget
#         return bool(remaining_budget>=0)
#
#     def __assign_army(self, name:str , s:int , a:int, c:int, formation:int):
#         force_size = s + a + c
#         self.name = name
#         if formation == 0:
#             self.force = ArrayStack(force_size)
#             #push Cavalry into the force
#             for i in range(c):
#                 self.force.push(Cavalry())
#             # push Archers into the force
#             for i in range(a):
#                 self.force.push(Archer())
#             # push Soldiers into the force
#             for i in range(s):
#                 self.force.push(Soldier())
#
#         print(self.force)
#
#
#     def choose_army(self, name: str, formation: int) -> None:
#
#         flag = True
#         while flag:
#             print("Player {} choose your army as S A C".format(name))
#             print("where S is the number of Soldiers\n\t  A is the number of Archers\n\t  C is the number of Cavalry")
#             given_army = input("Enter :")
#             try :
#                 given_army = given_army.strip().split()
#                 for i in range(len(given_army)):
#                     given_army[i] = int(given_army[i])
#                 s, a, c = given_army
#             except Exception as e:
#                 print(e)
#                 print(BREAK_LINE)
#             else:
#                 if self.__correct_army_given(s,a,c):
#                     self.__assign_army(name, s, a, c, formation)
#                     flag = False
#                 else:
#                     print("Army you chose is invalid")
#                     print(BREAK_LINE)