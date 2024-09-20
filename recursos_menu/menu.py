# Fazer um menu de navegação relacionada à solução


# Ver alertas atuais e históricos de alertas, ver histórico de alertas, 


# BEM-VINDO(A) AO SISTEMA


# COLOCAR A LÓGICA DO MENU DENTRO DE UMA FUNÇÃO (melhor) OU USAR UMA ESTRUTURA DE REPETIÇÃO (do, do-while)

# MÍNIMO DE 3 OPÇÕES
# 1. ALERTAS ATUAIS (exibe alertas atuais ou nenhum)
# 2. HISTÓRICO DE ALERTAS (busca o histórico de alertas)
# 3. INFORMAÇÕES OPERAÇÕES (operações normais, um pouco mais lentas)

# Falar que a opção é INVÁLIDA
# Deve incluir a opção de encerrar o programa


# EXEMPLO

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

from datetime import datetime

# PRIMEIRA TELA DE EXECUÇÃO
def inicioMenu():
    # Mensagem de boas vindas
    print("Seja bem-vindo!")
    
    # Opções principais
    print("Opções: \n")
    print("1. Cadastrar alertas")
    print("2. Alertas atuais")
    print("3. Histórico de alertas")
    print("4. Status de operação")
    
    # Opção de encerrar
    print("\n\n0. Encerrar menu")

# Chama a função para iniciar
inicioMenu()

# Função para voltar menus
def voltarMenu():
    print("\n\n")
    input("0. Voltar para menu inicial")
    
    inicioMenu()

# Função da opção 1 para REGISTRAR

# SALVAR AQUI: https://awari.com.br/python-como-salvar-um-arquivo-json/
def registrarAlerta():
        print("Para registrar seu alerta informe as seguintes informações: ")
        data = datetime.now()
        
        # Código para registrar alertas
        nomeAlerta = input("Nome: ")
        
        descricaoAlerta = input("Descrição: ")
        
        objetoAlerta = {
            "nome": nomeAlerta,
            "descricao": descricaoAlerta,
            "horario_registro": data
        }
        
        print(f"Seu alerta foi registrado!\nInformações:\n", objetoAlerta)

menu_ativo = True # Condição que ativa o menu no loop

while (menu_ativo): 
    opcao = int(input())
    
    if opcao == 1:
        cls()
        registrarAlerta()
    
    if opcao == 2:
        # Código que exibe alertas atuais
        print("Nenhum alerta no momento, operações normais")
        voltarMenu()
        
    if opcao == 3:
        # Código que exibe o histórico de alertas
        print("Não há registros de ocorrência")
        voltarMenu()
        
    if opcao == 4:
        # Código para verificar operações 
        print("Todas as operações funcionando")
        voltarMenu()
        
    if opcao == 0:
        confirmar = input("Tem certeza que deseja encerrar o sistema? (S/N)")
        if (confirmar.lower() == "s"):
            menu_ativo = False

# REGISTRAR ALERTAS E CADASTRAR EM UMA VARIÁVEL, SALVANDO APENAS DURANTE A EXECUÇÃO

