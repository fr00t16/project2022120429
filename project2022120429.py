# write by number int dari 0 - 585
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(585):
	value = randint(0,585)
	print(value)