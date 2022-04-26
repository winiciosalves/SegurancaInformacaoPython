from bs4 import BeautifulSoup
import requests

site = requests.get('https://climatempo.com.br').content
#Objeto site recebendo o conteúdo da requisição http do site...
soup=BeautifulSoup(site,'html.parser')
#Objeto soup baixando do site o html
#print(soup.prettify())
#Transforma html em string e o print vai exibir o html
temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
print(temperatura.string)

print(soup.title)

print(soup.find())

