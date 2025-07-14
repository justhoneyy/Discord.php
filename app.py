from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print(f"[!] Captured - Email: {email}, Password: {password}")
    return "<h2>Login received (educational demo).</h2>"

if __name__ == '__main__':
    app.run(debug=True)
    
