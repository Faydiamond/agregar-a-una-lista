Flag=False

List=[]

def Add_Fruit():
    nombre = input("¿Digite su nombre? ")
    List.append(nombre)
    print(List)
    exit_fruit()

def exit_fruit():
  ex = input("¿termino de ingresar frutas? ")
  if ex=='si':
    print(List)
  elif ex=='no':
    Add_Fruit()



if List:
  print ('Lista No esta vacia!')
else:
  print ('Lista Vacia')
  Add_Fruit()