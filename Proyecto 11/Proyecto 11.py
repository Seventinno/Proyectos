#Codigo para realizar scrapping en una web ficticia de libros
import bs4
import requests

# lo fundamental del scraping es verificar la etiquetas de lo que deseamos buscar

# url sin numero de paginas
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

'''resultados = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultados.text, 'html.parser')'''

# la siguiente variabla indica todas las clases product_pod
# las cuales se relacionana con los libros
'''libros = sopa.select('.product_pod')'''

# Al colocar el indice 0 nos referimos al primer libro
'''ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)'''

#Lista de titulos con rating alto

titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')

    #seleccionar datos del libro
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:
        #Chequear cantidad de estrellas
        if len(libro.select('.star-rating.four')) != 0 or len(libro.select('.star-rating.five')) != 0:
            #guardar titulo en varible
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

# ver libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
