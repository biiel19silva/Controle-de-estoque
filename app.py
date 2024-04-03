from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/produtos')
def produtos():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
