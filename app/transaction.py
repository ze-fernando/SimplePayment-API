from flask import jsonify
from . import db

class TranferService:
    @staticmethod
    def transfer(sender, recieve, amount, desc):
        if sender.balance < amount: return jsonify({'message': 'Saldo insuficiente para transação'}), 400
        
        elif sender.type.lower() == 'merchant': return jsonify({'message': 'Lojistas não podem realizar transações'}), 500
        
        else:
            sender.balance -= amount
            recieve.balance += amount
            
            db.session.commit()
            if desc is not None: return jsonify({
                    'message': 'Transação feita com sucesso',
                    'description': f'{desc}'
                    }), 200
                
            return jsonify({'message': 'Transação feita com sucesso'}), 200
    