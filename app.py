from flask import Flask,render_template, request, url_for, redirect

app = Flask(__name__)

musicas =[]

# musicas =[
#     {'name': 'Estudar', 'finished': False},
#     {'name': 'Dormir', 'finished': True},
#     {'name': 'Comer', 'finished': True},
# ]

@app.route('/')
def home():
    return render_template('home.html', musicas=musicas)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    musica = {'name' : name, 'finished': False}
    musicas.append(musica)
    return redirect(url_for('home'))    

@app.route('/Deletar/<name>')
def deletar(name):
    musica = {'name' : name, 'finished': False}
    musicas.remove(musica)        
    return redirect(url_for('home'))
app.run(debug=True)