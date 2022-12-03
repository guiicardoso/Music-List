from flask import Flask,render_template, request, url_for, redirect
import json
app = Flask(__name__)

musicas =[]

# musicas =[
#     {'name': 'Estudar', 'finished': False},
#     {'name': 'Dormir', 'finished': True},
#     {'name': 'Comer', 'finished': True},
# ]

@app.route('/')
def home():
    with open ("app.json", 'r') as f:
        musicas = json.load(f)
    return render_template('home.html', musicas=musicas)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    musica = {'name' : name, 'finished': False}
    with open ("app.json", 'r') as f:
        musicas = json.load(f)
    musicas.append(musica)
    with open("app.json", 'w') as f:
        json.dump(musicas,f, indent = 2)
    return redirect(url_for('home'))    

@app.route('/Deletar/<name>')
def deletar(name):
    with open ("app.json", 'r') as f:
        musicas = json.load(f)
    musica = {'name' : name, 'finished': False}
    musicas.remove(musica)
    with open("app.json", 'w') as f:
        json.dump(musicas,f, indent = 2)        
    return redirect(url_for('home'))
app.run(debug=True)