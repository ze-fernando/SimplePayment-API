from flask import Blueprint, request

route = Blueprint('main', __name__)

@route.post('/user')
def newUser():
    data = request.json
    return data

    


"""@app.post('/transfer')
def transfer():
    data = request.json
    sender_id
    reciever_id
    """
    