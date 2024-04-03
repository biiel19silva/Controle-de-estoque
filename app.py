from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/produtos')
def produtos():
    return render_template('products.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/localidades')
def localidades():
    return render_template('locations.html')

@app.route('/movimentacoes')
def movimentacoes():
    return render_template('movements.html')

if __name__ == '__main__':
    app.run(debug=True)
