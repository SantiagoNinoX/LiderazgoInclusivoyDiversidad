import speech_recognition as sr
import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para reconocer comandos de voz
def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Di tu decisión.")
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language="es-ES").lower()
            return comando
        except sr.UnknownValueError:
            speak("No entendí, intenta de nuevo.")
            return None
        except sr.RequestError:
            speak("Hubo un problema con el reconocimiento de voz.")
            return None

# Historia interactiva mejorada
speak("Bienvenido a la aventura por voz. Te encuentras en un bosque oscuro. Puedes 'avanzar', 'esperar' o 'explorar'.")
while True:
    decision = escuchar_comando()
    if decision == "avanzar":
        speak("Caminas por el bosque y encuentras un río. ¿Quieres 'cruzar', 'seguir la orilla' o 'buscar un puente'?")
        decision = escuchar_comando()
        if decision == "cruzar":
            speak("Cruzas el río y encuentras un tesoro. ¡Has ganado!")
            break
        elif decision == "seguir la orilla":
            speak("Sigues caminando y llegas a un pueblo seguro. ¡Fin de la aventura!")
            break
        elif decision == "buscar un puente":
            speak("Encuentras un viejo puente, pero parece frágil. ¿Quieres 'cruzar' o 'buscar otra ruta'?")
            decision = escuchar_comando()
            if decision == "cruzar":
                speak("El puente es resistente y logras pasar al otro lado. ¡Has ganado!")
                break
            elif decision == "buscar otra ruta":
                speak("Sigues explorando y encuentras un camino secreto que te lleva a una cueva misteriosa. ¡Fin de la historia!")
                break
    elif decision == "esperar":
        speak("Te quedas quieto y escuchas ruidos. Un lobo aparece y debes correr. ¿Quieres 'esconderte' o 'enfrentarlo'?")
        decision = escuchar_comando()
        if decision == "esconderte":
            speak("Encuentras un árbol hueco y te refugias hasta que el lobo se va. ¡Estás a salvo!")
            break
        elif decision == "enfrentarlo":
            speak("El lobo te observa fijamente... pero decides arrojarle comida que llevas contigo. Se calma y se va. ¡Sigues vivo!")
            break
    elif decision == "explorar":
        speak("Encuentras una cueva misteriosa. ¿Quieres 'entrar' o 'seguir explorando el bosque'?")
        decision = escuchar_comando()
        if decision == "entrar":
            speak("Dentro de la cueva hay un antiguo cofre. Lo abres y encuentras un mapa del tesoro. ¡La aventura continúa!")
            break
        elif decision == "seguir explorando el bosque":
            speak("Sigues tu camino y descubres un claro con una fogata encendida. ¿Quieres 'acercarte' o 'alejarte'?")
            decision = escuchar_comando()
            if decision == "acercarte":
                speak("La fogata pertenece a un viajero amable que te invita a cenar. ¡Has encontrado compañía!")
                break
            elif decision == "alejarte":
                speak("Decides seguir tu viaje solo en la oscuridad del bosque. ¡La historia continúa!")
                break
    else:
        speak("Esa opción no es válida, intenta de nuevo.")