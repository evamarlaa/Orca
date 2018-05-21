def checkPermission(acess, key=0):
    if acess == "gerencia":
        return True
    elif acess == "operacional" and key == 1:
        return True
    else:
        return False

def generateCodeServiceOrder():
    codeOrderServiceFile = open('OS_CODE.txt', 'r')
    count = codeOrderServiceFile.read()
    codeOrderServiceFile.close()
    if(int(count)==None):
        codeOrderServiceFile = open('OS_CODE.txt', 'w')
        codeOrderServiceFile.write('1')
        codeOrderServiceFile.close()
        return 1
    elif int(count) >= 1:
        codeOrderServiceFile = open('OS_CODE.txt', 'w')
        codeOrderServiceFile.write(str(int(count) + 1))
        codeOrderServiceFile.close()
        return count+1
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

def registerUser(acess, nameEmployee, cpfEmployee, birthdayEmployee, officeEmployee, usersDictionary):
    if checkPermission(acess) == True:
        password = input('Digite sua senha de acesso ao sistema: ')
        if checkPassword(password)==True:
            user=(nameEmployee, birthdayEmployee, officeEmployee, password)
            usersDictionary[cpfEmployee] = user
            #VERIFICAR SE JÁ EXISTE ALGUM CADASTRO COM O CPF INFORMADO
            return "Usuário cadastrado com sucesso!"

def checkPassword (password, cont = 0):
    passwordConfirmation = input('Digite novamente sua senha: ')
    if password == passwordConfirmation and cont <=3:
        print("Senha cadastrada com sucesso:")
        return True
    elif password != passwordConfirmation and cont <=3:
        print("Senha incorreta, tente novamente!")
        return checkPassword(password, cont+1)
    else:
        return "Não conseguimos cadastrar este usuário!"


