class BankAccount:
    def __init__(self, balance):        
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount #incrementa el balance con el monto depositado
            print(f"Depósito: {amount} New Balance: {self.balance}")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount #decrementa el balance con el monto retirado
            print(f"Retiro: {amount} New Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                print(f"Retiro: {amount} New Balance: {self.balance}")  
            else:
                raise ValueError(
                    "Retiro no permitido. El balance no puede estar por debajo del mínimo requerido."                    
                )
        else:
            raise ValueError("Monto de retiro inválido o fondos insuficientes.")




account = BankAccount(1000) # Crea una cuenta bancaria con un saldo inicial de 1000
print("Balance actual Cuenta Bancaria:", account.balance)
savings = SavingsAccount(1500, 200) # Crea una cuenta de ahorro con un saldo inicial de 1500 y un mínimo de 200
print("Balance actual Cuenta de Ahorro:", savings.balance)

try:
    savings.withdraw(1400) # Intenta retirar 1400 de la cuenta de ahorro, lo que dejaría el balance en 100, que es menor que el mínimo requerido de 200, tambien se puede probar con un monto negativo y mostrar el mensaje de error correspondiente
except ValueError as error:
    print(error)

print("Balance actual Cuenta de Ahorro:", savings.balance)
