from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for contacts
contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_contact(index):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
        return redirect(url_for('index'))
    
    contact = contacts[index]
    return render_template('update.html', contact=contact, index=index)

@app.route('/search', methods=['POST'])
def search_contact():
    query = request.form['query']
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return render_template('index.html', contacts=results)

if __name__ == '__main__':
    app.run(debug=True)
