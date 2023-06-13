from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username =='admin' and password == 'password':
         return app.run(home)
    else:
         return 'Invalid username or password'

if __name__ =='__main__':
    app.run(login)

@app.route('/')
def game():
     print("1,addition")
     print("2,subtraction")
     print("3,multiplication")
     print("4,division")
     choice=input("enter 1/2/3/4 ")
     if choice == 1:
          app.run(add)
     elif choice == 2:
          app.run(sub)
     elif choice == 3:
          app.run(mul)
     elif choice == 4:
          app.run(div)
     else:
          print("enter correctly!!!!!!!")

@app.route('/')
def add(x, y):
     return x + y
@app.route('/')
def sub(x, y):
     return x - y
@app.route('/')
def mul(x, y):
     return x * y
@app.route('/')
def div(x, y):
     return x / y

@app.route('/')
def home(name, choice):
     print("welcome")
     name = input("what is your name? ")
     print(f"welcome, {name}")
     choice=input("od you want to paly a game? yes or no ")
     if choice.startswith("yes"):
          return app.run(game)
     elif choice.startswith("no"):
          return app.run(exit)
     else:
          app.run(login)
