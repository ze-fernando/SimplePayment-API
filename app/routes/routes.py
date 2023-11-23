from flask import Blueprint, request, jsonify
from app import db, Users

database = db.session

route = Blueprint('main', __name__)

@route.post('/user')
def newUser():
    data = request.json
    
    user = Users(
        name = data['name'],
        cpf = data['cpf'],
        email = data['email'],
        balance  = data['balance'],
        typ = data['type'],
        password = data['pass']
    )
    database.add(user)
    database.commit()
    
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201
    


"""@app.post('/transfer')
def transfer():
    data = request.json
    sender_id
    reciever_id
    """
    