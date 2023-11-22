from dataclasses import dataclass
from enums import Type

@dataclass
class User:
    name: str
    cpf: str
    email: str
    passwd: str
    balance: float
    typ: Type
    
