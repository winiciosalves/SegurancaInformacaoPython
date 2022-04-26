import os #Importa o módulo ou biblioteca OS (Integra os recursos do S.O)

print("#" * 60) ##Imprimindo #60 vezes

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
#Criamos uma variavel que vai receber do usuario um IP
print("-" * 60) #Imprimindo - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) ## Chamando System da biblioteca OS comando ping -n 6 - num de pacotes que serão 6 {}
print("-" * 60) #Imprimindo - 60 vezes
