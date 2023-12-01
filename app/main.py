from getpass import getpass

def criar_arquivo():
    with open('usuarios.txt', 'a'):
        pass

def cadastrar_novo_usuario(usuario, senha):
    from os import linesep
    with open('usuarios.txt', 'a', newline='') as file:
        file.write(f'{usuario},{senha}' + linesep)

def verificar_login(usuario, senha):
    with open('usuarios.txt', 'r') as file:
        for linha in file:
            ind = linha.index(',')
            if linha[:ind] == usuario:
                if linha[ind+1:] == senha:
                    print('Login efetuado com sucesso!')
                    return True
                else:
                    print('Senha inválida!')
                    return False
        print(f'"{usuario}" não é cadastrado como um nome de usuário.')
        return False



