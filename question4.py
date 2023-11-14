""" Write a program to count the no. of vowels in a string. """

vowels = "aeiouAEIOU"
string = input("Enter a string")
vowel_count = 0
conso_count =0
for ch in string:
    if (ch in vowels):
        vowel_count += 1
    else:
        conso_count += 1
print("the length of the string is: ", len(string))
print("the no of vowels in string is: ", vowel_count)
print("the no of consonents in string is: ", conso_count)