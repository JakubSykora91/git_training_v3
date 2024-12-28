
#def separate_letters(text):
text = "Hello! I am Jakub. This is my python script to find UPPPER Letter and lower letter in a text"
    
upper_case = []
lower_case = []


for char in text:
    if char.isupper():
        upper_case.append(char)
    elif char.islower():
        lower_case.append(char)
    
print( upper_case) 
print (lower_case)