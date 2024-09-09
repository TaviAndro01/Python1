# Laboratul 1
from operator import length_hint

# Exercitiul 1

# x = int(input("Baza = "))
# y = int(input("Inaltimea = "))
# z = (x*y)/2
# print(f"Tipul rezultatului {z} este {type(z)}")

# Exercitiul 2

# x = 7710
# y = int(input("Numărul tău este: "))
# if x<y:
#     print(f"{x} este mai mic decât parola")
# elif x>y:
#     print(f"{x} este mai mare decât parola")
# else:
#     print("Ai ghicit parola")

# Exercitiul 3

# x = int(input("Primul număr este:"))
# y = (input("Al doilea număr este:"))
# print(f"Media numerelor este:{(x*y)/2}")
# print(f"Impartirea numerelor este:{int(x/y)}")
# print(f"A la puterea b:{pow(x,y)}")

# Exercitiul 4

# x = int(input("Venit:"))
# print(f"Recomandarile noastre:")
# print(f"Cheltuieli uzuale:{x/2}")
# print(f"Recreere:{(x*30)/100}")
# print(f"Economii si datorii:{(x*20)/100}")

# Laboratul 2


# Exercitiul 1

# print("Astăzi mă duc la \"facultate\".")
# print("/*\\/*\\/*\\/*\\ \n Python \n\\./\\./\\./\\./")
# print("P\ty\tt\th\to\tn")
# print("/*\\"*5)

# Exercitiul 2

# x = (input("Numele utilizatorului:"))
# y = int(input("Varsta:"))
# print(f"Cum te numesti? {x}")
# print(f"Ce varsta ai? {y}")
# print(f"Ceau Ana! Deci te-ai nascut in {2024-y}. ")

# Exercitiul 3

# x = input("Introduceti un sir:")
# print("Lungimea șirului este: {lungime}".format(lungime=len(x)))
# print(f"Lungimea sirului este: {len(x)}")
# print("Lungimea sirului este: "+str(len(x)))
# print(f"Lungimea sirului este:",len(x))

# Exercitiul 4
# x = "/-\\".center(15)
# y = "//_\\\\".center(15)
# z = "--------".center(15)
# a = "\\\\_//".center(15)
# b = "\\-/".center(15)
# print(x,y,z,a,b, sep = "\n")

# x = "----".center(12)
# y = "/ \t \\".center(10)
# z = "/ ______ \\".center(12)
# print(x,y,z, sep = "\n")

# x = "*".center(7)
# y = "***".center(7)
# z = "*****".center(8)
# a = "*******".center(7)
# print(x,y,z,a, sep= "\n")

# Exercitiul 5

# x = input("Introduceti un cuvant:")
# y = x[::-1]
# if x==y:
#     print("Palindrom: True")
# else:
#     print("Palindrom: False")

# def replace(text,text2,text3,text4):
#     text = text.replace(" ", "_")
#     text2 = text2.replace(" ", "_")
#     text3 = text3.replace(" ", "_")
#     text4 = text4.replace(" ", "_")
#     print(text,text2,text3,text4)
# def punct(text,text2,text3,text4):
#     text = text + "."
#     text2 = text2 + "."
#     text3 = text3 + "."
#     text4 = text4 + "."
#     print(text,text2,text3,text4)
# def primul(text,text2,text3,text4):
#     text = text.split()[0]
#     text2 = text2.split()[0]
#     text3 = text3.split()[0]
#     text4 = text4.split()[0]
#     print(text*4,text2*4,text3*4,text4*4)
# x = "Hello Python "
# y = "Ana are mere "
# z = "Pizza Party "
# a = x + y + z
# print(x,y,z,a,sep="\n")
# replace(x,y,z,a)
# punct(x,y,z,a)
# primul(x,y,z,a)

# Exercitiul 7
# a = 5
# b = 5
# c = "ana"
# print(f"Locatia lui a este {hex(id(a))}")
# print(f"Locatia lui b este {hex(id(b))}")
# print(f"Locatia lui c este {hex(id(c))}")
# print(f"Tipul variabilei a este {type(a)}")
# print(f"Tipul variabilei b este {type(b)}")
# print(f"Tipul variabilei c este {type(c)}")

# Capitolul 3

# Exercitiul 1

# x = str(input("Introduceti primele 7 cifre din CNP:"))
# a = int(x[0])
# y=int(x[1:3])
# if (a==1 or a==2 or 24-y>18):
#      print("Aveti peste 18 ani")
# else:
#      print("Nu aveti inca 18 ani")

# Exercitiul 2

# x = int(input("Numarul este:"))
# for i in range(x+1):
#     if i%2==0:
#         print(i)

# Exercitiul 3
# print ("Cappuccino ... 4 lei")
# print ("Espresso ...3.5 lei")
# x = int(input("Ce optiune alegeti? [1,2]:"))
# if x==1:
#     a = 4
# elif x==2:
#     a = 3.5
# else:
#     print("Optiunea nu este in meniu")
# if x==1 or x==2:
#     y = int(input("Introduceti o bacnota [5,10]:"))
#     if y==5 or y==10:
#         print (f"Veti primi restul de {y-a} lei.")
#         print ("Produsul se livreaza...")
#     else:
#         print ("Bancnota introdusa nu este acceptata. Aceasta va va fi restituita curand. Va multumim")

# Exercitiul 4

# x = int(input("Introduceti parola:"))
# a = 1
# while a == 1:
#     if x == 7788:
#         print("Acces permis.")
#         a = 2
#     else:
#         print("Parola gresita. Mai incercati")
#         x = int(input("Introduceti parola:"))

# Exercitiul 5

# x = ["Masa", 5, "Scaun", 4.5, [5,6,7],8]
# for i in x:
#     print(f"Tipul obiectului {i} este {type(i)}")