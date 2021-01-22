from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # <--- add this line
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



def id_gen():
   new_id = random.range(22,500,6)
   return new_id

@app.route('/users/', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')  # accessing the value of parameter 'name'
      search_job = request.args.get('job')
      if search_username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_job and search_username :
         subdict = {'users_list' : []}
         subd = {'users_list' : []}
         #search by name
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         #search by job
         for u2 in users['users_list']:
            if u2['job'] == search_username:
               subd['users_list'].append(u2)
         return subd
      return users
      
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = str(id_gen())
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True, user=userToAdd)
      resp.status_code = 201
      #fetch("http://127.0.0.1:5000/users")
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToDelete = request.args.get('id')
      if userToDelete: 
         uFound = {'users_list' : []}
         for user in users['users_list']:
            if user['id'] == userToDelete:
               users['users_list'].remove(user)
         return users
      return users

'''
@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_del_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
            if user['id'] == id:
               return user
            return ({})
         return users
      elif request.method == 'DELETE':
        for user in users['users_list']:
            if user['id'] == id:
               users['users_list'].remove(user)
        resp = jsonify(success=True)
        resp.status_code = 201
        return users
''' 

@app.route('/users/<name>/<job>')
def match_name_job(name, job):
    if name:
      for user in users['users_list']:
        if ((user['name']==name) and (user['job'] == job)): 
          resp = jsonify(success=True)
        else:
          resp = jsonify(success=False)
    return resp