# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(wrist, preast):
    # [assignment] Add your code here
    if (sorted(wrist) == sorted(preast)):
        answer = True
    else:
        answer = False
    print (answer)


str1 = input ("enter first word:") 
str2 = input ("enter second word:")
find_anagram(str1, str2)
    

