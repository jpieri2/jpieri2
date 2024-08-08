"""Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index of a char in the
original string (i.e. n will be in the range 0..len(str)-1 inclusive)."""

def missing_char(str, n):
    wrd = ""
    for letter in range(len(str)):
        if letter == int(n):
            continue
        else:
            wrd+= str[letter]
    return wrd
    
