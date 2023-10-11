from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularios')
def formularios():
    return render_template('formularios.html')

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')

@app.route('/tarjetas')
def tarjetas():
    return render_template('tarjetas.html')

if __name__ =='__main__':
	app.run(debug=True,port=5000)
