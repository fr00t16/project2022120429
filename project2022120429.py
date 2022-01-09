# write by number int dari 0 - 984
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(984):
	value = randint(0,984)
	print(value)