# method 1
# def checking(s1,s2):
#     if sorted(s1)==sorted(s2):
#         print('the given strings are anagram')
#     else:
#         print("the strings are not anagram")

# checking("cat","act")

# # method 2
# from collections import Counter
# def checking(s1,s2):
#     if Counter(s1)==Counter(s2):
#         print("the given strings are anagram")
#     else:
#         print("the strings arent anagram")

# checking("eleven plus two","tweleve plus one")

# method 3
def anagram(s1,s2):
    group_letters={}

    for i in s1:
        if i in group_letters:
            group_letters[i]+=1
        else:
            group_letters[i]=1
    
    for i in s2:
        if i in group_letters:
            group_letters[i]-=1
        else:
            group_letters[i]=1
            
    for j in group_letters:
        if group_letters[j]!=0:
            return False
    return True
    

s1=input("enter the first string:")
string1=s1.replace(" ","").lower()

s2=input("enter the second string:")
string2=s2.replace(" ","").lower()

me=anagram(string1,string2)

if me:
    print("its anagram")
else:
    print("it's not anagram")
