class employee:
    language = "Python" #This is class attribute 
    salary = 10000

mudasir = employee()
mudasir.name = "Mudasir" #This is an instance attribute 
print(mudasir.name, mudasir.language, mudasir.salary)

mubashir = employee()
mubashir.name = "Mubashir"
mubashir.language = "Java"
mubashir.salary = 1500000
print(mubashir.name, mubashir.language, mubashir.salary)