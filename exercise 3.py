#Exercise 3: Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.

word_input = input("Input Word ")
print("your word is ", word_input)
length_of_the_word = len(word_input)
for i in range(0, length_of_the_word, 2):
    print(word_input[i])