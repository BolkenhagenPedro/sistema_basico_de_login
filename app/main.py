from getpass import getpass

def ler_usuario():
    usuario = input('Digite um nome de um novo usuário: ')
    with open('./appusuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            while line[:ind] == usuario:
                print('Digite um nome de usuário que não está em uso.')
                usuario = input('Digite um nome de um novo usuário: ')
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

def cadastrar_novo_usuario(usuario, senha):
    from os import linesep
    with open('./app/usuarios.txt', 'a', newline='') as file:
        file.write(f'{usuario},{senha}' + linesep)

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
    pass