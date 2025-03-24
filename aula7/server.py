from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route("/helloWorld", methods=['GET'])
def helloWorld():
    return jsonify({
        "msg": "Olá mundo.",
        "list": tarefas
    })

tarefas = [
    {"id":1, "titulo": "Estudar", "Feito":False},
    {"id":2, "titulo": "Descansar", "Feito":True}
]

@app.route("/tarefas", methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

@app.route("/")
def get_html():
    return render_template('index.html')

@app.route("/tarefas", methods=["POST"])
def post_tarefa():
    nova_tarefa = request.json
    nova_tarefa['id'] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa),

if __name__ == '__main__':
    app.run(debug=True)