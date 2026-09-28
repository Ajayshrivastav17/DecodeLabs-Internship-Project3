# 🔐 Random Password Generator

A simple  Random Password Generator built with Python.

The application asks the user for a desired password length and generates a random password containing **letters and numbers**.

This project was created to practice Python fundamentals such as **modules, string manipulation, loops, `.join()`, input validation, and exception handling**.

For security-sensitive password generation, this project uses Python's built-in `secrets` module instead of the ordinary `random` module. Python's documentation recommends `secrets` for generating cryptographically strong random values suitable for passwords and other security-sensitive data. [Python `secrets` documentation](https://docs.python.org/3/library/secrets.html?utm_source=chatgpt.com)

---

# 🎯 Project Objective

The main objective is to create a command-line tool that:

1. Asks the user for a password length.
2. Validates the entered length.
3. Creates a character pool containing letters and numbers.
4. Securely selects random characters.
5. Combines the characters into one password.
6. Displays the generated password.

---

# ✨ Features

* Accepts password length from the user
* Generates passwords of the requested length
* Uses uppercase and lowercase letters
* Uses numbers
* Uses `secrets.choice()` for secure random selection
* Uses `.join()` to combine characters
* Validates password length
* Rejects zero or negative lengths
* Handles non-numeric input
* Uses Python's built-in modules
* Requires no external libraries

---

# 🛠️ Technologies Used

* Python 3
* `secrets`
* `string`

No third-party packages or frameworks are required.

---

# 📁 Project Structure

```text
random_password_generator/
│
├── main.py
└── README.md
```

---

# 🧠 How the Program Works

The application follows this flow:

```text
User
  │
  ▼
Enter password length
  │
  ▼
Validate length
  │
  ├── Invalid → Display error
  │
  └── Valid
        │
        ▼
Create character pool
        │
        ▼
secrets.choice()
        │
        ▼
Select characters
        │
        ▼
"".join()
        │
        ▼
Generated Password
```

---

# 🔤 Character Pool

The application uses Python's built-in `string` module.

```python
import string
```

The character pool is created using:

```python
characters = string.ascii_letters + string.digits
```

### `string.ascii_letters`

Contains:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### `string.digits`

Contains:

```text
0123456789
```

Therefore:

```python
characters = string.ascii_letters + string.digits
```

creates a pool containing:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
```

---

# 🔐 Why `secrets.choice()`?

The application uses:

```python
secrets.choice(characters)
```

instead of:

```python
random.choice(characters)
```

The Python `secrets` module is specifically intended for generating cryptographically strong random numbers and values for security-sensitive applications such as passwords and tokens. [Python `secrets` documentation](https://docs.python.org/3/library/secrets.html?utm_source=chatgpt.com)

Example:

```python
import secrets

character = secrets.choice("ABC123")
```

The function securely selects one character from the provided sequence.

---

# 🔗 Using `.join()`

Instead of repeatedly adding characters like:

```python
password = password + character
```

the project uses:

```python
password = "".join(
    secrets.choice(characters)
    for _ in range(length)
)
```

The expression generates individual characters and `join()` combines them into one string.

For example:

```python
"".join(["A", "7", "k", "2"])
```

produces:

```text
A7k2
```

The empty string:

```python
""
```

means that no separator is placed between the characters.

---

# 🔢 Password Length

The user enters the desired length:

```python
length = int(input("Enter password length: "))
```

For example:

```text
Enter password length: 12
```

The program then generates exactly 12 characters.

---

# 🔄 Loop Logic

The generator uses:

```python
for _ in range(length):
```

If:

```text
length = 8
```

the operation runs eight times.

Conceptually:

```text
1 → Select character
2 → Select character
3 → Select character
4 → Select character
5 → Select character
6 → Select character
7 → Select character
8 → Select character
```

These characters are then combined using `.join()`.

---

# 🛡️ Input Validation

The program does not allow a password length of zero or a negative number.

```python
if length <= 0:
    raise ValueError(
        "Length must be greater than 0"
    )
```

For example:

```text
Enter password length: 0

Error: Length must be greater than 0
```

And:

```text
Enter password length: -5

Error: Length must be greater than 0
```

---

# ⚠️ Exception Handling

The application handles invalid user input using `try` and `except`.

```python
try:
    length = int(
        input("Enter password length: ")
    )

except ValueError as error:
    print(f"Error: {error}")
```

If the user enters:

```text
abc
```

Python cannot convert it into an integer.

Instead of crashing, the application displays:

```text
Error: invalid literal for int() with base 10
```

The program can also raise its own `ValueError` when the number is zero or negative.

Python's `ValueError` is appropriate when a value has the correct general type but is not an acceptable value for the operation. [Python Built-in Exceptions documentation](https://docs.python.org/3/library/exceptions.html?utm_source=chatgpt.com)

---

# 💻 Complete Code

```python
import secrets
import string


print("""
-----------------------------------
     RANDOM PASSWORD GENERATOR
-----------------------------------
""")


try:

    length = int(
        input("Enter password length: ")
    )

    if length <= 0:
        raise ValueError(
            "Length must be greater than 0"
        )

    characters = (
        string.ascii_letters +
        string.digits
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print(
        f"\nGenerated Password: {password}"
    )


except ValueError as error:

    print(f"Error: {error}")
```

---

# ▶️ How to Run

Make sure Python is installed:

```bash
python --version
```

Run the application:

```bash
python main.py
```

---

# 🖥️ Example

```text
-----------------------------------
     RANDOM PASSWORD GENERATOR
-----------------------------------

Enter password length: 10

Generated Password: aK7pQ92LmX
```

Every time the program runs, a different password can be generated.

Example:

```text
Enter password length: 10

Generated Password: 8xPq91LmZa
```

Another run:

```text
Enter password length: 10

Generated Password: Q7mK2aX91p
```

---

# ❌ Invalid Input Example

### Non-numeric input

```text
Enter password length: abc

Error: invalid literal for int() with base 10
```

### Zero

```text
Enter password length: 0

Error: Length must be greater than 0
```

### Negative number

```text
Enter password length: -10

Error: Length must be greater than 0
```

---

# 🧩 Python Concepts Practiced

## 1. Importing Modules

```python
import secrets
import string
```

---

## 2. User Input

```python
input()
```

---

## 3. Type Conversion

```python
int()
```

Converts the user's input from a string into an integer.

---

## 4. Conditional Statements

```python
if length <= 0:
```

Checks whether the requested length is valid.

---

## 5. Exception Handling

```python
try:
    ...
except ValueError:
    ...
```

Handles invalid input.

---

## 6. Raising Exceptions

```python
raise ValueError(
    "Length must be greater than 0"
)
```

Manually raises an error when the entered length is invalid.

---

## 7. String Manipulation

```python
string.ascii_letters
```

and:

```python
string.digits
```

are used to create the character pool.

---

## 8. Random Character Selection

```python
secrets.choice(characters)
```

Selects a character securely.

---

## 9. `range()`

```python
range(length)
```

controls how many characters are generated.

---

## 10. `.join()`

```python
"".join(...)
```

combines individual characters into a single password string.

---

# 📊 Core Logic

The complete password-generation logic can be summarized as:

```text
Password Length
       │
       ▼
Create Character Pool
       │
       ▼
Letters + Numbers
       │
       ▼
secrets.choice()
       │
       ▼
Repeat for requested length
       │
       ▼
"".join()
       │
       ▼
Final Password
```

---

# 🔒 Security Considerations

This project uses `secrets.choice()` rather than `random.choice()` because the purpose is password generation.

However, this basic implementation guarantees only that the password is made from the selected character pool. It does **not** guarantee that every generated password contains:

* At least one uppercase letter
* At least one lowercase letter
* At least one number

For example, a generated password could theoretically contain only letters.

A future version can enforce character requirements.

For real-world password management, users should also consider password length, uniqueness, and using a trusted password manager.

---

# 🚀 Future Improvements

Possible improvements include:

* Guarantee at least one uppercase letter
* Guarantee at least one lowercase letter
* Guarantee at least one number
* Add special characters
* Add password strength estimation
* Allow users to exclude confusing characters
* Generate multiple passwords
* Add a password history
* Add a graphical user interface
* Add command-line arguments
* Add automated tests

---

# 🎓 Learning Outcomes

By completing this project, you practice:

```text
Python
│
├── Modules
│   ├── secrets
│   └── string
│
├── User Input
│
├── Type Conversion
│
├── Conditions
│
├── Loops
│
├── Exception Handling
│
├── raise
│
├── String Manipulation
│
├── range()
│
└── join()
```

The project demonstrates how a small Python program can combine several fundamental concepts into a useful command-line tool.

---

# 👨‍💻 Author

**Ajay Deviprasad Shrivastav**

Learning Python Programming, AI Engineering, and AI Automation.
