from flask import Blueprint, request, jsonify
from app import db, Users, TranferService

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
        type = data['type'],
        password = data['pass']
    )
    user.set_pass(user.password)
    
    database.add(user)
    database.commit()
    
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201
    


@app.post('/transfer')
def transfer():
    data = request.json
    sender_id = data['sender']
    reciever_id = data['recieve']
    amount = data['amount']
    TranferService.transfer(sender_id, reciever_id, amount)
    
    