#Question:
'''
The code produces an error. Please understand the error and try to fix it

print(type("Hey".replace("ey","i")[-1])

Hint: An open bracket always needs a closing bracket.
'''
#Answer:
'''
print(type("Hey".replace("ey","i")[-1]))

Explanation:

This code produces a SyntaxError: unexpected EOF while parsing which means
that Python found an unexpected End Of File while parsing. The reason of an
unexpected end of file is there's a missing closing bracket at the end of the
script. So, adding a closing bracket at the end of the file fixes the code.
'''
