import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.mercadopago.com.ar/herramientas-para-vender/cobrar-con-qr'
try: 
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error: {response.status_code}')
        
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
except Exception as e:
    print(f'Error: {e}')
   
    
links_data = {}

try:
    for a in links:
        href = a['href']
        
        exp = re.compile(r'^https://www.mercadopago.com.ar/')

        if exp.match(href):
            response = requests.get(href)
            if response.status_code != 200:
                raise Exception(f'Error: {response.status_code}')
                
            
            soup = BeautifulSoup(response.text, 'html.parser')
            h1_tags = [str(tag) for tag in soup.find_all('h1')]
            p_tags = [str(tag) for tag in soup.find_all('p')]
            links_data[href] = {'h1': h1_tags, 'p': p_tags}

            if h1_tags and p_tags:
                links_data[href] = {'h1': h1_tags, 'p': p_tags}
            else:
                links_data[href] = []
             
except Exception as e:
    print(f'Error al procesar los enlaces: {e}')


with open('links_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(links_data, json_file, ensure_ascii=False, indent=4)
