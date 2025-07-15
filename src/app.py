
### OPEN SERVER ###
# pipenv run python src/app.py

### PARA PROBAR EN API Request Builder ###
# Pasar el puerto abierto (3245) de "private" a "public"

#########################################################



from flask import Flask, jsonify, request
app = Flask(__name__)

# Variable global con to-do's
todos = [ { "label": "My first task", "done": False } ]



#############################
######### ENDPOINTS #########
#############################

######## GET /todos ########
@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

######## POST /todos ########
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

######## DELETE /todos ########
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is te position to be deleted:', position)
    todos.pop(position)
    # return "DELETE request accepted."
    return jsonify(todos)



#########################################
# endpoint de prueba con texto
@app.route('/myroute', methods=['GET'])
def my_route():
    return 'Hello World!'

# endpoint de prueba con HTML
@app.route('/hello', methods=['GET'])
def hello():
    return "<h1>Hello!</h1>"
#########################################



# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
