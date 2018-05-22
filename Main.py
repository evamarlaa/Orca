def generateCodeServiceOrder():
    codeOrderServiceFile = open('OS_CODE.txt', 'r')
    count = codeOrderServiceFile.read()
    codeOrderServiceFile.close()
    if(count==""):
        codeOrderServiceFile = open('OS_CODE.txt', 'w')
        codeOrderServiceFile.write('1')
        codeOrderServiceFile.close()
        return 1
    elif int(count) >= 1:
        codeOrderServiceFile = open('OS_CODE.txt', 'w')
        codeOrderServiceFile.write(str(int(count) + 1))
        codeOrderServiceFile.close()
        return int(count)+1
    else:
        return "Arquivo inválido"

def generateServiceOrder(acess, fileName, nameCarrying, cpfCarrying, companyName, companyCNPJ, dispatcherName, dispatcherOffice, description, date):
    fileName += ".txt"
    fileOS = open(fileName, 'w')
    data = [nameCarrying, cpfCarrying, companyName, companyCNPJ, dispatcherName, dispatcherName, dispatcherOffice, description, date]
    code = generateCodeServiceOrder()
    fileOS.writelines(str(code), "\n", "TRANSPORTADOR RESPONSÁVEL: ", data[0], "\n", "CPF DO TRANSPORTADOR: ", data[1], "\n", "EMBARCADOR: ", data[2], "\n", "CNPJ EMBARCADOR: ", data[3],"\n", "AUTORIZADO POR: ", data[4],"\n", "DESPACHANTE CARGO: ", data[5], "\n\n", data[6], "\n\n", data[7])
    fileOS.close()
    return "OS CRIADA COM SUCESSO!"

def checkPermission(acess, key=0):
    if acess == "gerencia":
        return True
    elif acess == "operacional" and key == 1:
        return True
    else:
        return False

def checkPassword (password, cont = 0):
    passwordConfirmation = input('Digite novamente sua senha: ')
    if password == passwordConfirmation and cont <=3:
        print("Senha cadastrada com sucesso!")
        return True
    else:
        return "Não conseguimos cadastrar este usuário!"

usersDictionary={}

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


