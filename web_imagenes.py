import requests
import bs4 
import os
import re

def directorio_imagenes(imagenes):
    if not os.path.exists('imagenes'):
        os.makedirs('imagenes')

def descargar_imagenes(url):
    for i, img in enumerate(url):
        try:
            respuesta = requests.get(img)
            if respuesta.status_code == 200:
                ext = re.search(r'\.jpg|\.png|\.webp', img).group()
                with open(f'imagenes/imagen_{i}.jpg', 'wb') as archivo:
                    archivo.write(respuesta.content)
            print(f'Imagen {i} descargada {ext}')
        except requests.exceptions.RequestException as e:
            print(f'Error al descargar la imagen {i}: {e}')

url = 'https://www.mercadolibre.com.ar/c/deportes-y-fitness#menu=categories'

def obtener_imagenes(url):
    try:
        respuesta = requests.get(url)
       
        if respuesta.status_code != 200:
            raise Exception(f'Error: {respuesta.status_code}')
            
        soup = bs4.BeautifulSoup(respuesta.text, 'html.parser')
        imagenes = soup.find_all('img')

        url_imagen = []
        for img in imagenes:
            if 'data-src' in img.attrs:
                url_imagen.append(img['data-src'])

        img_extencion = []
        for img in url_imagen:
            if re.search(r'\.jpg|\.png|\.webp', img) is not None:
                img_extencion.append(img)
        url_imagen = img_extencion
        url_imagen = list(set(url_imagen))
        directorio_imagenes(imagenes)
        descargar_imagenes(url_imagen)

    except Exception as e:
        print(f'Error: {e}')

obtener_imagenes(url)

