import random
from faker import Faker

fake = Faker()

list_range = list(range(1, 21))

l = [(lambda: fake.color_name())() for _ in range(5)]

random_val = random.choice(l)
random_int = random.randrange(0, 100, 10) # [0, 100]

random_decimal = random.random() # (0, 1)

random_vals = random.choices(l, weights=[99, 0, 0, 0, 1], k=2)

just_unique_val = list(range(1,51))
hand = random.sample(list(range(1,11)), k=3)

print(hand)
# print(l)
# print(random_vals)