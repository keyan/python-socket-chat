from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass
    
@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next = '/')
    print url_for('profile', username = 'John Doe')
    
if __name__ == '__main__':
    app.debug = True
    app.run()