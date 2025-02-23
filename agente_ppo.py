import random  

def agente_inteligente(entorno):

    acciones = ['moverse', 'explorar', 'recolectar']  
    
    if entorno == 'peligroso':  
        return 'retroceder'  
    
    return random.choice(acciones)  


entornos = ['seguro', 'seguro', 'peligroso', 'seguro']

for e in entornos:
    print(f"Entorno: {e} -> Acción del agente: {agente_inteligente(e)}")

#1.	Agregar más tipos de entornos (Ejemplo: incierto, oscuro).
#2.	Incluir más acciones (Ejemplo: esconderse, pedir ayuda).
#3.	Permitir que el agente aprenda de sus experiencias previas.
#4.	Modificar la lógica para que el agente tenga un historial de decisiones 
# y evite repetir errores.
