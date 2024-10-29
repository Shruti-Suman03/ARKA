from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Function to generate the password
def generate_password(length):
    if length < 4:  # Ensure a minimum length for better security
        return "Password length should be at least 4 characters."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Generate password with at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to make it unpredictable
    random.shuffle(password)

    return ''.join(password)

# Route to display the form
@app.route('/')
def index():
    return render_template('password.html')

# Route to handle the form submission and display the generated password
@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        if length < 1:
            result = "Please enter a valid positive integer."
        else:
            result = generate_password(length)
    except ValueError:
        result = "Invalid input! Please enter a number."
    
    return render_template('password.html', password=result)

if __name__ == "__main__":
    app.run(debug=True)
