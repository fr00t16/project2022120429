# write by number int dari 0 - 108
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(108):
	value = randint(0,108)
	print(value)