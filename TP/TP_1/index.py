nom = input("Ton nom : ")
age = int(input("Ton âge : "))

if age < 18:
    print("Tu es mineur")
else:
    print("Tu es majeur")
    
print("Nombres pairs de 1 à 100 :")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)