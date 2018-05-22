def registerUser(acess, nameEmployee, cpfEmployee, birthdayEmployee, officeEmployee, usersDictionary):
    if checkPermission(acess) == True:
        count = 0
        while(count<=3):
            password = input('Digite sua senha de acesso ao sistema: ')
            if checkPassword(password)==True:
                if cpfEmployee not in usersDictionary:
                    user=(nameEmployee, birthdayEmployee, officeEmployee, password)
                    usersDictionary[cpfEmployee] = user
                    return "Usuário cadastrado com sucesso!"
                else:
                    return "Usuário já existe no banco de dados!"
            count+=1

def deleteUser(acess, cpfEmployee, usersDictionary):
    if cpfEmployee in usersDictionary:
        usersDictionary.pop(cpfEmployee)
        return "Usuário deletado com sucesso!"
    return "Usuário não encontrado!"

def updateUser(acess, nameEmployee, cpfEmployee, birthdayEmployee, officeEmployee, usersDictionary):
    if cpfEmployee in usersDictionary:
        altera = input("Digite 's' para alterar sua senha: ")
        if(altera == 's'):
            count = 0
            while (count <= 3):
                password = input('Digite sua senha de acesso ao sistema: ')
                if checkPassword(password) == True:
                    user = (nameEmployee, birthdayEmployee, officeEmployee, password)
                else:
                    return "Não foi possível alterar a senha, tente novamente mais tarde!"
    else:
        if cpfEmployee in usersDictionary:
            password = usersDictionary[cpfEmployee][3]
            user = (nameEmployee, birthdayEmployee, officeEmployee, password)
    usersDictionary[cpfEmployee] = user;
    return "Usuário atualizado com sucesso!"

def checkPassword (password, cont = 0):
    passwordConfirmation = input('Digite novamente sua senha: ')
    if password == passwordConfirmation and cont <=3:
        print("Senha cadastrada com sucesso!")
        return True
    else:
        return "Não conseguimos cadastrar este usuário!"

def checkPermission(acess, key=0):
    if acess == "gerencia":
        return True
    elif acess == "operacional" and key == 1:
        return True
    else:
        return False

usersDictionary={}
print(registerUser("gerencia", "Eva Marla", "12300452448", "14/09/2000", "operacional", usersDictionary))
