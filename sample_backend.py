from flask import Flask
from flask import request
from flask import jsonify



app = Flask(__name__)

#@app.route('/users', methods=['GET', 'POST'])

@app.route('/')
def hello_world():
	return 'Hello, world!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      },
      {
        "id": "qwe123",
        "job": "Zookeeper",
        "name": "Cindy"
      }
   ]
}


@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users

@app.route('/users/<id>',methods=['DELETE'])
def delete_user(id):
   userToDelete = request.get_json()
   users['users_list'].remove(userToDelete)
   resp = jsonify(success=True)
   return resp


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')  # accessing the value of parameter 'name'
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #fetch("http://127.0.0.1:5000/users")
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp


@app.route('/users/<name>/<job>')
def match_name_job(name, job):
    if name:
      for user in users['users_list']:
        if ((user['name']==name) and (user['job'] == job)): 
          resp = jsonify(success=True)
        else:
          resp = jsonify(success=False)
    return resp