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
    


@route.post('/transfer')
def transfer():
    data = request.json
    sender_id = data['sender']
    reciever_id = data['recieve']
    amount = data['amount']
    desc = data['description'] if 'description' in data and data['description'] is not None else None

    
    sender = Users.query.get(sender_id)
    reciever = Users.query.get(reciever_id)
    
    
    if sender and reciever: return TranferService.transfer(sender, reciever, amount, desc)
    
    