import math

class Category():
  def __init__(self, cat):
    self.category = cat
    self.ledger = []

  def get_balance(self):
    platita = 0
    for dic in self.ledger:
      platita += dic["amount"]
    return platita
    
  def check_funds(self, amount):
    if self.get_balance() < amount:
      return False
    else: return True
      
  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount, "description":description})
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description":description})
      return True
    else: return False

  def transfer(self, amount, cat):
    desc = f"Transfer to {cat.category}"
    #si hay los fondos necesario
    if self.check_funds(amount):
      self.withdraw(amount, desc)
      # y ahora tranferimos
      desc = f"Transfer from {self.category}"
      cat.deposit(amount, desc)
      return True
    else: return False

  def __str__(self): 
    #cabecera
    line = '*'*(15 - math.floor(len(self.category)/2)) + self.category + '*'*(15 - math.ceil(len(self.category)/2)) + '\n'
    # detalles y saldos
    for dic in self.ledger:
      if len(dic["description"]) <= 23:
        line = line + dic["description"] + ' '*(30 - len(dic["description"]) - len("{:.2f}".format(dic["amount"]))) + "{:.2f}".format(dic["amount"]) + '\n'
      else:
        line = line + dic["description"][:23] + ' '*(7 - len("{:.2f}".format(dic["amount"]))) + "{:.2f}".format(dic["amount"]) + '\n'

    line = line + "Total: " + str(self.get_balance())
    return line

        
    
        
      

def create_spend_chart(categories):
  line = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
  return line
    
  
  
  