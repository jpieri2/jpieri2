"""Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. Return a
new string which is 3 copies of the front."""


def front3(str):
    x = str
    count = 0
    nl2 = ""


    for n in x:
   
      nl2 += n
      count +=1
    
      if len(nl2) == 3:
        break
    
    return nl2*3  

  
