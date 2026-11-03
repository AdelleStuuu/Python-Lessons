# prompt user to enter a string
string = input("Enter a string: ")
# add an empty dictionary
joinedString = []
# add the string value and the constant hello
joinedString.append(string)
joinedString.append("Hello")
# use the joio keyword to combing the string and "Hello"
# "" indicated the separtor (eg. StringHello) 
print(f"Concatenated string:","".join(joinedString))