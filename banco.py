import os, time

saldo = 100.00
historico = "Seu histórico está vazio"

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostra_saldo():
    print("=================")
    print("Saldo: R$", saldo)    
    print("=================")
    
while True:
    limpa()
    
    if saldo >= 1000:
        print("🎉 Você alcançou sua meta financeira!")
    print("Bem vindo ao Banco")
    print(historico)
    print("Selecione uma opção:")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = int(input("O que deseja fazer?: "))
    
    while True:
        if opcao in [1, 2, 3, 4]:
            if opcao == 1: #ver saldo 
                limpa()
                mostra_saldo()
                volta = int(input("Pressione '1' para voltar: "))
                if volta == 1:
                    limpa()
                    break
                else:
                    continue
                
            elif opcao == 2: #deposito
                limpa()
                mostra_saldo()
                deposito = float(input("Quanto você deseja depositar?: "))
                saldo += deposito
                print("Depósito concluído! Seu novo saldo é:", saldo)
                historico = "Sua última ação foi: Depósito"    
                time.sleep(1)
                print("Retornando para a central...") 
                time.sleep(1)    
                limpa()  
                break     
            
            elif opcao == 3: #sacar
                limpa()
                mostra_saldo()
                saque = float(input("Quanto deseja sacar?"))
                if saque <= saldo:
                    saldo -= saque
                    print("Saque realizado com sucesso! Seu novo saldo agora é:", saldo)
                    historico = "Sua última ação foi: Saque"   
                    time.sleep(1)
                    print("Retornando para a central...") 
                    time.sleep(1)    
                    limpa()  
                    break  
                else:
                    print("Saldo insuficiente!")
                    time.sleep(1)
                    print("Retornando para a central...") 
                    time.sleep(1)    
                    limpa()  
                    break  
            elif opcao == 4:
                print("Programa encerrado! Obrigado por escolher o nosso banco!")
                break
        else:
            print("Erro") 
            break   
        
    if opcao == 4:
        break