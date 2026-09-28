import secrets
import string

print("""__________________________
RANDOM PASSWORD GENERATOR
__________________________""")

try:
    length=int(input("Enter Password Lenght : "))

    if length <= 0:


        print(f'Error : Number must be greater than 0')

    else:
        character=string.ascii_letters+string.punctuation+string.digits

        password="".join(secrets.choice(character)for i in range(length))

        print(f"\nPassword Generated Successfully : {password}")

except Exception as e:
    print(e)

