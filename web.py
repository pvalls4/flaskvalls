from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/formulari', methods=['GET', 'POST'])
def formulari():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        
        return render_template('confirmacion.html', nombre=nombre, email=email)
    
    # Mostrar el formulario
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=False)

