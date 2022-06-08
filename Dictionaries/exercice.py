# Create a program to manage data of club partners allowing
# get info of the partners in a dictionarie to access by partner number.
# the data will be: number, name, last_name  insription date cuote up to day
# the program sart with the data of preload partners

def cargarSocios(partners):
    num=int(input("Partner number (0 to stop): "))
    while num!=0:
        name=input("Full name: ")
        date=input("Ingress Date (DDMMAAAA): ")
        payment=input("Payments up to day? y/n: ")
        partners[num]=[name,date,payment.lower()=="y"]
        num=int(input("Partner number (0 to stop1): "))
    return partners

def modificarFecha(socios, fecha_anterior, fecha_nueva):
    for datos in socios.values():
        if datos[1]==fecha_anterior:
            datos[1]=fecha_nueva
    return socios

def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
    for numero,datos in socios.items():
        print("-Number:",numero)
        print("-Name:",datos[0])
        print("-Igress date:", formatoFecha(datos[1]))
        if datos[2]:
            print("-Up to date")
        else:
            print("-not up tpo date")

active_users = {
    1:["Amanda Nuñez",  "17032009", True],
    2:["Bárbara Molina",  "17032009", True],
    3:["Lautaro Campos", "17032009", True]
}
print("1 Add user")
print("2 Number of users")
print("3 Register payment")
print("4 Modify ingress date")
print("5 Delete Partner")
print("0 End")
opc = int(input("Select an option "))
while opc != 0:
    if opc == 1:
        print("***Add user")
        active_users=cargarSocios(active_users)
    if opc == 2:
        print("The club has", len(active_users), "partners")

    if opc == 3:
        print("***Register payment")
        num=int(input("partner number: "))
        active_users[num][2]=True
        
    if opc == 4:
        print("***Modify ingress date")
        active_users=modificarFecha(active_users, "13032018", "14032018")

    
    if opc == 5:        
        print("***Delete Partner")
        name=input("Full Name: ")
        num=numeroSocio(active_users, name)
        if num in active_users:
            del active_users[num]

    imprimirListado(active_users)
    print("1 Add user")
    print("2 Number of users")
    print("3 Register payment")
    print("4 Modify ingress date")
    print("5 Delete Partner")
    print("0 End")
    opc = input("Select an option ")

