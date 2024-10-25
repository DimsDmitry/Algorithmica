from random import *

# СПОСОБ 1 - через randint
color_list = 'cyan red blue black orange green lightblue bisque purple yellow lime magenta'.split()
print(color_list)

rand_digit = randint(0, len(color_list)-1)
rand_color = color_list[rand_digit]
print(rand_color)

# СПОСОБ 2 - через shuffle
color_list = 'cyan red blue black orange green lightblue busquit purple yellow lime magenta'.split()
shuffle(color_list)
print(color_list[0])