from sys import quit
def ler_senha(msg='Digite a senha: '):
    from getpass import getpass
    senha = getpass(msg)
    while len(senha) < 8:
        print('Digite um senha com 8 ou mais caracteres.')
        senha = getpass(msg)
    return senha


def ler_usuario(msg='Digite um nome de um novo usuário: ', login=False):
    usuario = input(msg)
    with open('./appusuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            while line[:ind] == usuario:
                if login:
                    return True
                print('Digite um nome de usuário que não está em uso.')
                usuario = input(msg)
        return usuario

def leiaopc(msg=''):
    while True:
        try:
            n = int(input(msg))
            if 1 >= n >= 2:
                return n
            else:
                while n not in [1,2]:
                    print('Digite uma opção válida.')
                    n = int(input(msg))
        except:
            print('Digite uma opção válida.')

def criar_arquivo():
    with open('./app/usuarios.txt', 'a'):
        pass

def cadastrar_novo_usuario():
    from os import linesep
    usuario = ler_usuario()
    senha = ler_senha()
    with open('./app/usuarios.txt', 'a', newline='') as file:
        file.write(f'{usuario},{senha}' + linesep)
    print('Usuário cadastrado com sucesso.')
    quit()

def login():
   if (usuario := lerusuario('Informe o nome de usuário: ')):
        pass

def verificar_login(usuario, senha):
    with open('./app/usuarios.txt', 'r') as file:
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



criar_arquivo()

print("""Escolha alguma das opções a baixo:
    [1] - Login
    [2] - Cadastrar um novo usuário""")
opc = leiaopc('Sua opção: ')
if opc == 2:
    cadastrar_novo_usuario()
login()
