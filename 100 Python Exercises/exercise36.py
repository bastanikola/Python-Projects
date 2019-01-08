#Question:
'''
Please download the words1.txt file from the attachment and then create a
Python function that takes a text file as input and returns the number of
words contained in the text file.

Expected output:
10

Hint: Create a function that takes a file path as input, reads the file, splits
the content, and counts the items of the split output.
'''
#Answer:
'''
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_words("words1.txt"))

Note: For the above script to work, you should have a file named words1.txt in
the same directory with the Python script.

Explanation:

The function here takes as input a file path. If the file path is in the same
directory with your Python script, you can simply pass in the file name as in
the above script. If your text file is somewhere else, then you need to pass
the full path when calling the function.

Example:

print(count_words("C:/Home/words1.txt"))
The rest of the script consists of opening the file in read  mode, loading the
text into a string using read  and then splitting and counting the number of
words.
'''
