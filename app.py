from flask import Flask 

app = Flask(__name__)

@app.route('/')
def bienvenida():
    mensaje = '''
    <h1>bienvenidos desde la calculadora de python</h1>
<h2>1.para sumar teclea la ruta 127.0.0.1:500/suma/10/20</h2>
<h2>2.para restar teclea la ruta 127.0.0.1:500/resta/20/10</h2>
<h2>3.para multiplicar teclea la ruta 127.0.0.1:500/multiplicacion/20/10</h2>
<h2>4.para dividir teclea la ruta 127.0.0.1:500/division/20/10</h2>
<h2>5.para sacar el valor maximo teclea la ruta 127.0.0.1:500/max/20/10</h2>
<h2>6.para sacar el valor minimo teclea la ruta 127.0.0.1:500/min/20/10</h2>
<footer>NOMBRE:Roman Padilla Miguel Angel CORREO:23308060610314@cetis61.edu.mx</footer>
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
    num1 = int(v1)
    num2 = int(v2)
    rest = num1 - num2
    return(f"la resta de {int(v2)}-{int(v1)} es {rest}")

@app.route('/multiplicacion/<v1>/<v2>')
def multiplicacion(v1,v2):
    num1 = int(v1)
    num2 = int(v2)
    mult = num1 * num2
    return(f"la multiplicacion de {int(v2)} x {int(v1)} es {mult}")

@app.route('/division/<v1>/<v2>')
def division(v1,v2):
    num1 = int(v1)
    num2 = int(v2)
    div = num1 / num2
    return(f"la division de {int(v2)} / {int(v1)} es {div}")

@app.route('/max/<v1>/<v2>')
def maximo(v1,v2):
    num1 = int(v1)
    num2 = int(v2)
    maxi = max(num1,num2)
    return(f"el numero maximo entre {int(v2)} y {int(v1)} es {maxi}")

@app.route('/min/<v1>/<v2>')
def minimo(v1,v2):
    num1 = int(v1)
    num2 = int(v2)
    mini = min(num1,num2)
    return(f"el numero minimo entre {int(v2)} y {int(v1)} es {mini}")


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
