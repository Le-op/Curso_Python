import numpy as np
import matplotlib.pyplot as plt

def simular_galton(num_canicas, niveles):
    """
    Simula el comportamiento de una máquina de Galton.
    
    Args:
        num_canicas (int): Número total de canicas a simular.
        niveles (int): Número de niveles en la máquina de Galton.
        
    Returns:
        np.ndarray: Un array que contiene el conteo de canicas en cada contenedor.
    """
    # Inicializar un array para contar las canicas en cada contenedor
    conteo_contenedores = np.zeros(niveles + 1)
    
    for _ in range(num_canicas):
        # Cada canica tiene 12 decisiones: -1 (izquierda) o +1 (derecha)
        decisiones = np.random.randint(0, 2, niveles)  # 0 para izquierda, 1 para derecha
        # Sumar las decisiones: 0 se convierte en -1 y 1 se queda como 1
        posicion_final = np.sum(decisiones)  # Sumar las decisiones (0 o 1)
        conteo_contenedores[posicion_final] += 1  # Incrementar el contenedor correspondiente
    
    return conteo_contenedores

def graficar_histograma(conteo_contenedores):
    """
    Grafica un histograma del conteo de canicas en los contenedores.
    
    Args:
        conteo_contenedores (np.ndarray): Un array que contiene el conteo de canicas en cada contenedor.
    """
    # Crear una figura para la gráfica
    plt.figure(figsize=(12, 7))
    
    # Crear las barras del histograma
    barras = plt.bar(range(len(conteo_contenedores)), conteo_contenedores, color='#0000FF', alpha=0.8)
    
    # Agregar etiquetas a cada barra
    for barra in barras:
        yval = barra.get_height()  # Obtener la altura de la barra
        plt.text(barra.get_x() + barra.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10)
    
    # Personalización de la gráfica
    plt.title('Simulación de la Máquina de Galton con 3000 Canicas', fontsize=16, fontweight='bold')
    plt.xlabel('Contenedores', fontsize=14)
    plt.ylabel('Número de Canicas', fontsize=14)
    plt.xticks(range(len(conteo_contenedores)), fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')
    
    # Agregar una línea de media
    media = np.mean(conteo_contenedores)  # Calcular la media del conteo
    plt.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.2f}')
    plt.legend()  # Mostrar la leyenda
    
    # Cambiar el fondo
    plt.gca().set_facecolor('#00FFFF')  # Establecer el color de fondo
    
    # Mostrar la gráfica
    plt.show()

# Parámetros de la simulación
num_canicas = 3000  # Definir el número de canicas a simular
niveles = 12  # Definir el número de niveles en la máquina de Galton

# Simulación
conteo_contenedores = simular_galton(num_canicas, niveles)  # Ejecutar la simulación

# Graficar resultados
graficar_histograma(conteo_contenedores)  # Graficar el histograma de resultados                 