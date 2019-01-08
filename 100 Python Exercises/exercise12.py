#Question:
'''
Complete the script so that it produces the expected output. Please use
my_range as input data.

Expected output:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

my_range = range(1, 21)

Hint: One way to solve this is to use list comprehension.
'''
#Answer
'''
my_list = range(1, 21)

print([10 * x for x in my_list])
'''
