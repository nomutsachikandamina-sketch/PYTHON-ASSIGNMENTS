

Question 1
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)  
        result = classify_number(number)
        print(f"The number is {result}.")
      
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
Question 2
def calculate_average(args):
   
    Calculate the average of a variable number of numeric arguments.
    
    Parameters:
        *args (float or int): Any number of numeric values.
    
    Returns:
        float: The average of the provided numbers.
        None: If no arguments are provided.
    
    Example:
        >>> calculate_average(2, 4, 6)
        4.0
    
    if not args:
        return None  
    
    return sum(args) / len(args)
Question 3
while True:
    try:
        num = float(input("Enter a number: "))  
        print(f"You entered: {num}")
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")
Question 4
 Define a list of names to be written to the file
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
 Write the names to a file named 'names.txt'
 The 'with open(...)' statement automatically handles file closing.
 The 'w' mode opens the file for writing.
with open('names.txt', 'w') as file:
    Iterate over each name in the list
    for name in names:
        # Write each name followed by a newline character (\n)
        file.write(name + '\n')


 Read the names from the file and print them to the console
 The 'r' mode opens the file for reading.
print("Reading names from the file:")
with open('names.txt', 'r') as file:
     Iterate over each line in the file
    for line in file:
         The .strip() method removes leading/trailing whitespace, including the newline character
        print(line.strip())

Question 5
 A sample list of Celsius temperatures
celsius_temps = [0, 10, 20, 30, 40]
 The formula is F = C * 9/5 + 32
celsius_to_fahrenheit = lambda c: c * 9/5 + 32
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print("Original Celsius temperatures:", celsius_temps)
print("Converted Fahrenheit temperatures:", fahrenheit_temps)

Question 6
def divide_numbers(numerator, denominator):
    Divides two numbers and handles potential ZeroDivisionError and TypeError.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The result of the division if successful, or None if an error occurs.

        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError
        print("Error: Invalid input types. Please provide numbers.")
        return None



Question 7

class NegativeNumberError(Exception):
    Custom exception raised when a number is negative
    pass
def check_positive(number)
    Raises NegativeNumberError if the input number is negative.
       Args:
        number: The number to check.
     Raises:
        NegativeNumberError: If the number is less than 0.
    if number < 0:
        raise NegativeNumberError("The number provided is negative.")
    print(f"The number {number} is positive.")
print("--- Testing with a positive number ---")
try:
    check_positive(5)
except NegativeNumberError as e:
    print(f"Caught an exception: {e}")

print("\n--- Testing with a negative number ---")
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Caught an exception: {e}")

Question 8

import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Generated numbers: {random_numbers}")
total_sum = sum(random_numbers)
average = total_sum / len(random_numbers)
print(f"The average of the numbers is: {average:.2f}")

Question 9
I)import re
text = "Contact support@example.com or sales@company.org for more info. My email is user.name+tag@sub.domain.co."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"Emails found: {emails}\n")

II) def validate_date(date_string):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date_string):
        return True
    else:
        return False

date1 = "2023-11-20"
date2 = "2023-11-2"
print(f"Is '{date1}' a valid date format? {validate_date(date1)}")
print(f"Is '{date2}' a valid date format? {validate_date(date2)}\n")

 III)sentence = "The quick brown fox jumps over the lazy dog."
new_sentence = re.sub(r'quick', 'slow', sentence)
print(f"Original sentence: {sentence}")
print(f"Sentence with replacement: {new_sentence}\n")

IV)sentence_to_split = "Hello, world! How's it going?"
words = re.split(r'[^a-zA-Z0-9]', sentence_to_split)
words = [word for word in words if word]
print(f"Original string: {sentence_to_split}")
print(f"Split words: {words}")

Question 10
HOST = '127.0.0.1'  
PORT = 65432        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            message = "Hello from server!"
            conn.sendall(message.encode('utf-8'))
    except socket.error as e:
        print(f"Server error: {e}")
Client Program (client.py)
​The client needs to know the server's address and port to connect.
HOST = '127.0.0.1'  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connected to server.")
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
    except socket.error as e:
        print(f"Client error: {e}")

Question 11
An API (Application Programming Interface) refers to a  set of rules that allows two software applications to communicate with each other with the other sending data and the other receiving data.
Making a GET Request using `requests` Library in Python.

import requests

Define the API endpoint
url = "https://api.example.com/data"

Send a GET request
response = requests.get(url)

Check response status
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    print(data)
else:
    print("Request failed with status:", response.status_code)
 `requests.get(url)` sends the request.
 `response.json()` parses the data if it's JSON.
-status_code` helps check if the request was successful (200 = OK).

Connecting to a SQLite Database Using Python:

import sqlite3

Step 1: Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

Step 2: Create a cursor object
cursor = conn.cursor()

Step 3: Execute SQL commands (example: create table)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

Step 4: Commit changes



Firstly Connect to database by opening a connection to the SQLite database file. If the file doesn’t exist, it’s created.
Then create a cursor which is used  to execute SQL commands and fetch data.
Then execute SQL by creating  tables, insert data, query, etc.
Then commit changes like inserts 
Then close connection by freeing up resources and closes the link to the database.
print("Hello, World!")
