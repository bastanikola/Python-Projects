#Question:
'''
Please download the attached urls.txt file. The file contains some broken URLs.
Here's what the file contains:

https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com

Please use Python to remove the "s" from "https" and add another forward slash
next to the existing slash, so the content looks like in the expected output.

Hint 1: To remove the first occurence of a character in a string, you would use
"sample".replace("s", "", 1)

Hint 2: To add a character somewhere in a string you could do something like
"sample"[:2] + "x" + "sample"[2:].
'''
#Answer:
'''
with open("urls.txt", "r") as file:
    lines = file.readline()

print(lines)

with open("urls_corrected.txt", "w") as file:
    for line in lines:
        #removing only the first occurence of the "s" letter
        line_removes_s = line.replace("s", "", 1)
        line_removes_s_add_slash = line_removes_s[:6] + "/" + line_removes_s[6:]
        file.write(line_removes_s_add_slash)
'''
