from flask import Flask 

app = Flask(__name__)

@app.route('/')
def bienvenida():
    mensaje = '''
    <h1>bienvenidos desde la calculadora de python</h1>
<h2>1.para sumar teclea la ruta 127.0.0.1:500/suma/10/20</h2>
<h2>2.para restar teclea la ruta 127.0.0.1:500/resta/20/10</h2>
    '''
    return(mensaje)


@app.route('/factorial/<v>')
def factorial(v1):
    fact = 1
    for x in range(1, int(v1)+1):
        fact *= x
    return(f"el factorial de {v1}! es {fact}")

@app.route('/suma/<v1>/<v2>')
def suma(v1,v2):    
    num1 = int(v1)
    num2 = int(v2)
    sum = num1 + num2
    return(f"la suma de {int(v1)}+{int(v2)} es {sum}")

@app.route('/resta/<v1>/<v2>')
def resta(v1,v2):
    rest = v2 - v1
    return(f"la resta de {int(v2)}+{int(v1)} es {rest}")

@app.route('/multiplicacion/<v1>/<v2>')
def multiplicacion(v1,v2):
    mult = v2 * v1
    return(f"la multiplicacion de {int(v2)}+{int(v1)} es {mult}")

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
