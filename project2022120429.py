# write by number int dari 0 - 719
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(719):
	value = randint(0,719)
	print(value)