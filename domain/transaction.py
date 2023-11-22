from flask import jsonify

class TranferService:
    @staticmethod
    def transfer(sender, recieve, amount):
        if sender.balance <= 0: return jsonify({'message': 'Saldo insuficiente para transação'}), 400
        
        else:
            sender.balance =- amount
            recieve.balance += amount
            return jsonify({'message': 'Transação feita com sucesso'}), 200
    