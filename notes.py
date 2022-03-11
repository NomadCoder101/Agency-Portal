num = 'a'
if num != 0:
  try: 
   ans = num/5
   print("ans = ", ans)
  except:
   print("int required")
else:
   print("num must not be zero")

# dot notation in the case of class:
#package.module.class.method
#Or in the case of functions:
# package.module.function.attribute
# Table 5-1. Common regex symbols
# Symbol Matches
# . (dot) Any single character
# \d Any single digit
# [A-Z] Any character between A and Z (uppercase)
# [a-z] Any character between a and z (lowercase)
# [A-Za-z] Any character between a and z (case-insensitive)
# + One or more of the previous expression (e.g., \d+
# matches one or more digits)
# [^/]+ One or more characters until (and not including) a
# forward slash
# ? Zero or one of the previous expression (e.g., \d?
# matches zero or one digits)
# * Zero or more of the previous expression (e.g., \d*
# matches zero, one or more than one digit)
# {1,3} Between one and three (inclusive) of the previous
# expression (e.g., \d{1,3} matches one, two or three
# digits)
# (...) Matches whatever regular expression is inside the pa-
# rentheses and indicates the start and end of a group
# (?P<name>...) Matches whatever regular expression is inside the
# parentheses and turns matched data into a named
# parameter. E.g. (?P<pk>[0-9]+) would insert any
# captured digits into a parameter named pk .
# For more on regular expressions, see the Python regex documentation 12 .