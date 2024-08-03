from PIL import Image

def busqueda_en_imagen(imagen_path, tono):
    imagen = Image.open(imagen_path).convert("L")
    ancho, alto = imagen.size
    pixeles_encontrados = {}
    
    for x in range(ancho):
        for y in range(alto):
            tono_actual = imagen.getpixel((x, y))
            if tono_actual == tono:
                pixeles_encontrados[(x, y)] = tono_actual
    
    return pixeles_encontrados

imagen_path = '../TP-10/Piastri.jpg'
tono_buscado = 128
resultado = busqueda_en_imagen(imagen_path, tono_buscado)

for coordenada, tono in resultado.items():
    print(f"Coordenada: {coordenada}, Tono: {tono}")