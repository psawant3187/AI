# Returns the String in Uppercase.
course = "Python for Beginners"
print(course.upper())

#Returns the String in Lowercase.
course = "Python for Beginners"
print(course.lower())

# Returns the index number of Search letter in string.
course = "Python for Beginners"
print(course.find('f'))
# Also works for returning index number of Searching Word inside a string.
print(course.find('for'))
# To check if certain word is present in Strting .
print('for' in course)

# Replace word in string.
course = "Python for Beginners"
print(course.replace('for','4')) #it only works when replacement is string.