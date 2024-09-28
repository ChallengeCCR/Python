import os 

# Função para limpar o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Declarações 
menuAtivo = True
alertasAtivos = []

while menuAtivo:
    cls() # clear
    # Exibe as opções do menu
    print("Escolha uma opção:")
    print("[A] Registrar alerta")
    print("[B] Remover alerta")
    print("[C] Exibir alertas")
    print()
    print("[..] Encerrar programa") 
    print()
    
    # Define as opções existentes
    opcoesMenu = ["a", "b", "c", ".."] 
    
    # Escolhe uma opção
    opcaoUsuario = input().lower()
    
    # Verifica se a opção é válida ,caso contrário aponta erro
    if opcaoUsuario in opcoesMenu:
        
        ## OPÇÃO A - REGISTRAR ALERTAS
        if opcaoUsuario == "a":
            cls() # clear
            print("\t### REGISTRAR ALERTA")
            print()
            print("# Informe os seguintes dados para registrar")
            print()
            
            # Dados sobre os alertas
            alertaNomeInput = input("Nome: ")
            alertaDescricaoInput = input("Descrição: ")
            
            # Verificação se as informações para preenchimento de NOME e DESCRIÇÃO são válidas
            if alertaNomeInput.strip() and alertaDescricaoInput.strip():
                
                # Objeto de alerta
                alerta = {
                "nome": alertaNomeInput,
                "descricao": alertaDescricaoInput
                }
                
                # Adiciona o alerta na Array
                alertasAtivos.append(alerta)
                       
                # Mensagem de confirmação          
                cls() # clear        
                print(f"Alerta \"{alertaNomeInput}\" registrado!")
                print()
                print("Pressione ENTER para voltar")
                input()
                
            # Mensagem caso uma das informações seja vazia, "" ou " "
            elif not alertaNomeInput.strip() or not alertaDescricaoInput.strip():
                cls() # clear
                print("\t!!! Nenhum dos dados podem ser vazios !!!")
                print()
                print("Retorne ao menu e tente novamente")
                print()
                print("Pressione ENTER para voltar")
                input()

        ## OPÇÃO B -- REMOVER ALERTAS
        if opcaoUsuario == "b":
            cls() # clear            
            # Mensagem de erro caso não haja alertas registrados
            if not alertasAtivos:
                print("Nenhum alerta ativo.")
                print()
            else:
                print("\t### REMOVER ALERTAS ATIVOS")
                print()
                print("_" * 60)
                # Lista todos os alertas presentes em [alertarAtivos]
                for i, alerta in enumerate(alertasAtivos):
                    print()
                    print(f"ID: {i}\nNome: {alerta["nome"]}\nDescrição: {alerta["descricao"]}")
                    print("_" * 60)
                  
                print()  
                print("Informe o ID do alerta a ser removido: ")
            
                # Try and Except para remover o alerta
                try:
                    idParaRemover = int(input())
                            
                    # Verifica se o alerta existe e o remove           
                    if 0 >= idParaRemover < len(alertasAtivos): 
                        cls() # clear
                        print(f"Alerta \"{alertasAtivos[idParaRemover]["nome"]}\" removido!")
                        
                        # Remove o alerta da array
                        del alertasAtivos[idParaRemover]
                      
                    # Mensagem de erro para ID inválido, inexistente   
                    else: 
                        print("Esse alerta não existe!")
                # Mensagem de erro caso a input não seja do tipo Int
                except ValueError:
                        cls() # clear
                        print("\t!!! O ID deve ser obrigatoriamente um número INTEIRO !!!")
                        print()
                        print("Retorne ao menu e tente novamente")
                
            # Volta ao início do programa
            print()
            print("Pressione ENTER para voltar")
            input()

        ## OPÇÃO C -- VISUALIZAR ALERTAS
        if opcaoUsuario == "c":
            cls() # clear
            # Mensagem de erro caso não haja alertas registrados
            if not alertasAtivos:
                print("Nenhum alerta ativo.")
                print()
                
            else:
                print("\t### ALERTAS ATIVOS")
                print()
                print("_" * 60)
                # Lista todos os alertas presentes em [alertarAtivos]
                for i, alerta in enumerate(alertasAtivos):
                    print()
                    print(f"ID: {i}\nNome: {alerta["nome"]}\nDescrição: {alerta["descricao"]}")
                    print("_" * 60)
                
            # Volta ao início do programa
            print()
            print("Pressione ENTER para voltar")
            input()

        ## OPÇÃO .. - ENCERRAR O MENU                
        if opcaoUsuario == '..':
            cls() # clear
            print("Encerrando...")
            menuAtivo = False          
    else:
        cls() # clear
        print("\t!!! OPÇÃO INVÁLIDA !!!")
        print()   
