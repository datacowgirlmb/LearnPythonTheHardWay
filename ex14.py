from sys import argv

script, user_name = argv
x = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(x)

print(f"Where do you live {user_name}?")
lives = input(x)

print("What kind of computer do you have?")
computer = input(x)

print(f"""
Alright, so you've said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")