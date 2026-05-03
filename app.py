from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
pedido = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pedido['produto'] = request.form['produto']
        pedido['peso'] = request.form['peso']
        pedido['quantidade'] = int(request.form['quantidade'])
        return redirect(url_for('review'))
    return render_template('index.html')

@app.route('/review')
def review():
    return render_template('review.html', pedido=pedido)

@app.route('/production')
def production():
    tempo_unitario = 45 if pedido['peso'] == '500g' else 60
    tempo_total = tempo_unitario * pedido['quantidade']
    return render_template('production.html', pedido=pedido, tempo=tempo_total)

if __name__ == '__main__':
    app.run(debug=True)
