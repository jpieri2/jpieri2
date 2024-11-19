'''The following are functions for finding a day of the week if (Mon - Sun == 1
-7) and is added to and/or has a number subtracted from the given day. But the
final function can do either or if given a positive or negative number.'''



def add_days(d,n):
    m = d + n
    m%= 7
    while m < 1:
        m = m + 7
    
    return m

def subtract_days(d,n):
    m = d - n
    while m < 1:
        m = m + 7
    
    return m


def daysondays(d,n):
    m = d + n
    m%= 7
    while m < 1:
        m = m + 7
    
    return m
