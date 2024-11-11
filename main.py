import random
import string

def main():
    try:
        len = password("Enter length > ")
        print(f"The password is {len}")
    except:
        print("Invalid type")

def password(length):
    userInp = int(input(length))
    if userInp < 6:
        print("Weak Password")
    elif userInp < 8:
        print("Medium Password")
    elif userInp < 12:
        print("Good Password")
    else:
        print("Excellent Password")
    return passGen(userInp)

def passGen(lenn):
    s1 = ""
    s1 += string.ascii_lowercase
    s1 += string.digits
    s1 += string.ascii_uppercase
    s1 += string.punctuation
    password = []
    for _ in range(lenn):
        randomchar = random.choice(s1)
        password.append(randomchar)
    passKey = "".join(password)
    return passKey

if __name__ == "__main__":
    main()