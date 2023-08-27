# defining a reverse function
def reverse(string):
    return string[::-1]



# defining a count_vowel  to count the number of vovel in string function
def count_vowel(string):
    vowels="aeiouAEIOU"
    count=0
    for letters in string:
        if letters in vowels:
            count+=1
    return count



# # defining a capitalize to capitalize a string 
def capitalize(string):
    return string.upper()


# defining a cfunction to chek if  a string is palindrome 
def is_palindrome(string):
    # Convert to lowercase and remove spaces/punctuation
    string = string.lower().replace(" ", "").replace(",", "").replace(".", "") 
    return string == string[::-1]


