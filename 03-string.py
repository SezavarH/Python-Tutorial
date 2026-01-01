# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)


# Multiline String (''' ... ''' is also possible)

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people."""
print(multiline_string)

# join
first_name = "Lionel"
last_name  = "Messi"
print(first_name + " " + last_name)

## way 2: " " → the separator (a single space)
print(" ".join([first_name, last_name]))


# Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon


# count
print(language.count("n"))
print("apple".count("p"))


# split():Splits String from Left

challenge = 'Hi there this is a test'
print(challenge.split())  