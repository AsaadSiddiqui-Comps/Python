email = []
phone = []
f = open("exp14.txt", "r")
for x in f:
   xf = x.split()
   for item in xf:
       if "@" in item:
           email.append(item)
       if "+91" in item:
              phone.append(item)
print("Data ExtRACTted Form The Given File")
print(f" Phone Numbers: {phone}")
print(f" Email Address's: {email}")

















email = []
phone = []

#By ai
# f = open("11.txt", "r")

# read = f.readlines()
# words = []
# for line in read:
#     words.extend(line.split())  # Split each line into words and add to the list

# #print(words)
# for i in words:
#     if "@" in i:
#          email.append(i)
#          print(i)

f = open("11.txt", "r")
for x in f:
   #print(x)
   xf = x.split()
   #print(xf)
   for item in xf:
       if "@" in item:
           email.append(item)
       if "+91" in item:
              phone.append(item)
print("Data ExtRACTted Form The Given File")
# print(f" Phone Numbers: {phone}")
# print(f" Email Address's: {email}")

for q in range(len(email)): #phone/email Be also used HEERE it is only for the where to end the loop
    print(f"Email : {email[q]}, Phone: {phone[q]}")
    
# for z in st:
#     if "@" in z:
#         # email.append(z)
#         print(z)
#print(email)

# read = f.readlines()
# word = read.split()
#print(word)





# for i in word:
#     if "@" in i:
#          email.append(i)
#          print(i)
#     if "-" in i:
#         phone.append(i)
#     if "/" in i:
#         dob.append(i)





# print("Emails:", emails)
# print("Phone Numbers:", phone_numbers)
# print("Dates:", dates)




# john.doe@example.com
# jane.smith@company.org
# 123-456-7890
# 987.654.3210
# 01/01/2023
# 12/31/2022

# File handling operations explained:

# 1. Opening a file:
# The `open()` function is used to open a file. It requires the file path and mode.
# Modes include:
# - "r": Read mode (default, opens the file for reading)
# - "w": Write mode (creates a new file or overwrites an existing file)
# - "a": Append mode (adds data to the end of the file without overwriting)
# - "rb", "wb", etc.: Binary modes for reading/writing binary files

# 2. Reading a file:
# - `read()`: Reads the entire content of the file as a single string.
# - `readline()`: Reads one line at a time from the file.
# - `readlines()`: Reads all lines from the file and returns them as a list of strings.

# 3. Writing to a file:
# - `write()`: Writes a string to the file.
# - `writelines()`: Writes a list of strings to the file.

# 4. Splitting strings:
# - `split()`: Splits a string into a list of words based on whitespace by default.
#   You can provide a delimiter to split based on specific characters.

# 5. Stripping strings:
# - `strip()`: Removes leading and trailing whitespace or specified characters from a string.
# - `lstrip()`: Removes leading whitespace or specified characters.
# - `rstrip()`: Removes trailing whitespace or specified characters.

# 6. Iterating through a file:
# You can iterate through a file object line by line using a `for` loop.

# 7. Closing a file:
# Always close the file after completing operations using `close()` to free system resources.
# Alternatively, use a `with` statement to handle files, which ensures the file is closed automatically.

# Example:
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Strips leading/trailing whitespace and prints each line