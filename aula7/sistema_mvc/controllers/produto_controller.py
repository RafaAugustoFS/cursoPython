from sistema_mvc.models.produto import Produto
from models.produto import produto
from flask import current_app, render_template, Blueprint, request, redirect, url_for

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/')
def index():
    produtos = produto.listar(current_app.mysql)
    return render_template('index.html', produtos=produtos)

@produto_bp.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.salvar(Produto(None, nome, preco), current_app.mysql)
        return redirect(url_for('produto.index'))
    return render_template("criar.html")

@produto_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.atualizar(Produto(None, nome, preco), current_app.mysql)
        return redirect(url_for('produto.index'))
    prod = Produto.buscar_por_id(current_app.mysql, id)
    return render_template("editar.html", produto=prod)

@produto_bp.route('/deletar/<int:id>')
def deletar(id):
    Produto.deletar(current_app.mysql, id)
    return redirect(url_for('produto.index'))