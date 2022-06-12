import copy
import random
# Consider using the modules imported above.

class Hat:
  # at least 1 ball, el resto en la tupla args
  def __init__(self, **kwargs):    #forma un dic con todos los key(color):values(cant)      
    self.contents = []
    for key, value in kwargs.items():   #por cada color (str)
      for i in range(value):    # repetimos un color :value veces
        self.contents.append(key)  

    
  def draw(self, nroBalls):
    if len(self.contents) <= nroBalls:
      return self.contents
    else:
      list = []
      for i in range(nroBalls):
        indice = random.randrange(len(self.contents))
        elem_a_elim = self.contents[indice]
        list.append(elem_a_elim)
        self.contents.remove(elem_a_elim)
      return list   #retorna list de sti ej: ["red", "blue", "blue", "yellow"]

 
def list_a_dic(list):
  dic = {}
  for str in list:
    if str not in dic:
      dic[str] = 1
    else:
      dic[str] += 1
  return dic
    
def dic_in_dic(dic, bigger_diccionary):
  for key in dic:
    if key not in bigger_diccionary.keys():  # si el color q we need no está en la tanda
      return False
    if bigger_diccionary[key] < dic[key]:   # si tiene el color but no la cant necesaria
      return False
  return True  #estan todos los colors y cant necesarias


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0   #cant de veces q la tanda dió el resultado
  
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)  #balls in list[str's] (tanda)
    dic_balls = list_a_dic(balls)      #balls as dic (tanda)

    if dic_in_dic(expected_balls, dic_balls):
      success += 1

  probabilidad = success/num_experiments
  return probabilidad
