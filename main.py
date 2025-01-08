import functools
import pandas as pd
from flask import Flask, request, jsonify

# Iniciar App
app = Flask(__name__)

#Cargar el archivo
resultado = pd.read_excel('C:\\Users\\Cpu\\OneDrive\\Escritorio\\proyectos\\Prueba exportar\\outputfinal.xlsx')

#Crear la Api
@app.route('/api/Walmart', methods=['POST'])
def apiWalmart():
    data = request.get_json()

    #Obtener el valor del producto
    n_producto = data['Producto']
    valor_producto = resultado.loc[resultado['Producto'] == n_producto]
    precio_producto = valor_producto['Valor']

    #Crear Diccionario del Json
    resultado_json = {
        'Producto': str(n_producto),
        'Precio': precio_producto
    }
    return jsonify(resultado_json)


if __name__ == '__main__':
    app.run()