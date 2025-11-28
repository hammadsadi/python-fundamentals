# Example of using escape characters in a string
course_name = "Introduction to \"Programming"
# Example of Using New Line Escape Character in a String
new_course = "Introduction to \nProgramming"
# print(new_course) 

# Concatenating Strings
first ="Sayyid"
last ="Saadi"
full = first + " " + last
# print(full)


# Using Formatted Strings (f-strings)
full_name = f"{first} {last}"
# print(full_name)


# Calculating Length of Strings in a Variable using f-strings 
user_full_name_length = f"{len(first)} {len(last)}"
# print(user_full_name_length)  # print(user_full_name_length)

course = "introduction to programming"

# String Methods
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())
print(course.rstrip())
# String Finding Methods
print(course.find("ing"))

# String Replacement Method
print(course.replace("programming", "Python"))

# Checking Substring Presence
print("programming" in course)

print("sadi" not in course)