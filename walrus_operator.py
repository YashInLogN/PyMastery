'''
:= , Walrus operator
'''


# happy = True
# print("Happy status: ", happy )

print("Happy status: ", happy := True)

foods = list()
# while True:
#     food = input("What food do u like: ")
#     if food.lower() == "quit": break
#     foods.append(food)

while food := input("What do u like to eat: ").lower() != "quit":
    foods.append(food)