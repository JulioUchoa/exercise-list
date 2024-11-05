import cs50

# define loop for accpeting only inputs between 1 and 8:
# if user types any other number, program should reprompt
height = 0
while height > 8 or height < 1:
    height = cs50.get_int("what height you want your piramid to be? ")


#define loop for priting a piramid of height height
x=1
for i in range(height):
    print(" " * (height-x), end="")
    print("#" * x, "", "#" * x)
    x+=1

