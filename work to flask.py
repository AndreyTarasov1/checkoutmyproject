from flask import Flask, request

app = Flask(__name__)

@app.route("/get")
def get():
   framework1 = request.args.get('framework')

   return "Framework {}".format(framework1)

@app.route('/authorization', methods=['GET', 'POST'])
def authorization():

   if request.method == 'POST':
       Login = request.form.get('Login')
       Password = request.form.get('Password')

       if Login=="admin" and Password=="admin":
           return '<div>Ты прошел</div>'
       else:
           return "Ты не прошел"

   return '''
             <form method="POST">
                 <div><label>Login: <input type="text" name="Login"></label></div>
                 <div><label>Password: <input type="text" name="Password"></label></div>
                 <div><label><input type="text"></label></div>
                 <input type="submit" value="Enter">
             </form>'''

if __name__ == "__main__":
  app.run()


