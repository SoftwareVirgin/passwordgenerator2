import random
import string

def randomString(stringLength=8):
 #Generates a string with  digits and syymbols

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Generating Random String password with letters, digits and special characters ")
print ("First Random String ", randomString() )
print ("Second Random String", randomString(8) )
print ("Third Random String", randomString(8) )