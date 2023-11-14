#Codigo de asistente virtual

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# escuchar microfono y devolver el audio como texto


def transformarAudio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera para verificar errores
        r.pause_threshold = 0.5

        # informar que comenzo la grabacion
        print('Ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-MX")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("Ups no entendi")

            # devolver error
            return "Sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # devolver error
            return "Sigo esperando"

        # error inesperado:
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "Sigo esperando"


# funcion para que el asistente pueda ser escuchado

def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


engine = pyttsx3.init()
'''for voz in engine.getProperty('voices'):
    print(voz)'''


# Informar el dia de la semana
def pedir_dia():
    # crear variable del dia de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}

    hablar(f'Hoy es {calendario[dia_semana]}')


# informar hora
def pedir_hora():

    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    # decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():

    # crear variables con datos de hora
    hora = datetime.datetime.now()
    if 6 < hora.hour > 20:
        momento = 'buenas noches'

    elif 6 <= hora.hour < 13:
        momento = 'Buen día'

    else:
        momento = 'Buenas tardes'

    # decir el saludo
    hablar(f'{momento}, soy Helena tu asistente personal. Por favor, dime en que te puedo ayudar')


def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    while comenzar:

        #activar micro y guardar pedido en un str
        pedido = transformarAudio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'que dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
            except:
                hablar('Perdon no la he encontrado')
        elif 'adiós' in pedido:
            hablar('Me voy descansar, cualquier cosa me avisas')
            break

pedir_cosas()


