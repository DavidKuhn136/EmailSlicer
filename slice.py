# use .partition to strip the username and domain
def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain is {domain}"

user_input = input("Enter your email: ")
print(email_slicer(user_input))
