#/usr/bin/python3
import random

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def generar_pregunta():
    operacion = random.choice(["suma", "resta", "multiplicación", "división"])
    contador = 0
    if operacion == "suma":
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        respuesta_correcta = num1 + num2
        pregunta = f"Vamos a sumar. ¿Cuánto es {num1} + {num2}?"

    elif operacion == "resta":
        num1 = random.randint(1, 20)
        num2 = random.randint(1, num1)
        respuesta_correcta = num1 - num2
        pregunta = f"Intentemos una resta. ¿Cuánto es {num1} - {num2}?"
    elif operacion == "multiplicación":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        respuesta_correcta = num1 * num2
        pregunta = f"Vamos a multiplicar. ¿Cuánto es {num1} x {num2}?"
    else:
        respuesta_correcta = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num1 = respuesta_correcta * num2
        pregunta = f"Probemos una división. ¿Cuánto es {num1} ÷ {num2}?"


    return pregunta, respuesta_correcta

                
def obtener_respuesta():
    while True:
        try:
            respuesta = int(input("Tu respuesta: "))
            return respuesta
        except ValueError:
            print("\nPor favor, ingresa un número entero válido.")

def retroalimentacion(respuesta_correcta, respuesta_estudiante):
    respuestas_correctas = [
        f"¡Bien hecho, {nombre}! 👏",
        f"¡Eres un matemático brillante, {nombre}! 🌟",
        f"{nombre}, sigues sumando puntos. Muy bien. 🚀",
        f"¡Increíble, {nombre}! Estás en llamas. 🔥",
        f"Correcto, {nombre} 🎉. Sigue sumando éxitos.",
        f"Uff, no por nada eres la Maxima :v ",
        f"Salvaje.... sabia que lo lograrias! 🔥🔥🔥🔥🔥",
        f"{nombre} lo sabia! Tu eres el macho! 💪💪"
    ]

    respuestas_incorrectas = [
        f"¡Oh no, {nombre}! Esa no es la respuesta correcta. 😔\n",
        f"Inténtalo de nuevo, {nombre}. Te acercas. 💪",
        f"Incorrecto, {nombre}. Pero no te rindas, inténtalo otra vez. 🙌",
        f"No te preocupes, {nombre}. Todos cometen errores. Inténtalo de nuevo. 🤔",
        f"Oops, {nombre}, no es la respuesta correcta. Pero sigue intentando. 🚧",
    ]

    intentos = 0
    while intentos < 2:  # Permitir hasta 3 intentos
        if respuesta_estudiante == respuesta_correcta:
            print(GREEN + "\n\t" + RESET, random.choice(respuestas_correctas))
            return True
        else:
            print("\n\t❌", random.choice(respuestas_incorrectas))
            print(" ")
            intentos += 1
            respuesta_estudiante = obtener_respuesta()

    print("\t❌ Incorrecto. Ver el siguiente recurso: https://www.espaciohonduras.net/matematicas")
    return False
    
    




def main():
    global nombre
    nombre = input("\n¡Hola! ¿Cuál es tu nombre? ")
    print(f"\nBienvenido al programa de práctica matemática, {nombre}.")

    preguntas_correctas = 0
    preguntas_incorrectas = 0
    preguntas_id = 1

    for _ in range(15):
        pregunta, respuesta_correcta = generar_pregunta()
        print(f"\n{preguntas_id}. {pregunta}")
        respuesta_estudiante = obtener_respuesta()
        
        if retroalimentacion(respuesta_correcta, respuesta_estudiante):
            preguntas_correctas += 1
        else:
            preguntas_incorrectas += 1
        
        preguntas_id += 1

    porcentaje_correcto = (preguntas_correctas / 15) * 100

    print("\nFin del programa.")
    print(f"\nPreguntas correctas de {nombre}: {preguntas_correctas}")
    print(f"Preguntas incorrectas de {nombre}: {preguntas_incorrectas}")
    print(f"Rendimiento de {nombre}: {porcentaje_correcto:.2f}%")

    if porcentaje_correcto <= 70:
        print(f"\n{nombre}, te sugerimos repetir el ejercicio. 📚\n")
    else:
        print(f"\n¡Felicitaciones, {nombre}! Puedes continuar con el siguiente nivel. 🎉")

if __name__ == "__main__":
    main()
