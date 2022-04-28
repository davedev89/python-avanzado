def make_division_by(n):
     #This clousure returns a function that returns the division of an x number by n

     def division(x):
          assert n > 0, "Debes colocar un numero mayor a cero"
          return x/n
     
     return division


division_by_3 = make_division_by(3)
print(division_by_3(18))

division_by_5 = make_division_by(5)
print(division_by_5(100))

division_by_18 = make_division_by(18)
print(division_by_18(54))