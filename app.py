from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # For ethical testing: just print to console
    print(f"[!] Captured - Email: {email}, Password: {password}")
    
    return "<h2>Thanks for testing our phishing demo!</h2><p>This is for awareness training only.</p>"

if __name__ == '__main__':
    app.run(debug=True)
  
