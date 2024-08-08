"""This is a function that accepts two arguments and returns a value of True or
False depending on the arrangement."""

"""The parameter weekday is True if it is a weekday, and the parameter vacation
is True if we are on vacation. We sleep in if it is not a weekday or we're on
vacation. Return True if we sleep in."""

def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  elif weekday == True and vacation == True:
    return True
  else:
    return None

 
 
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
