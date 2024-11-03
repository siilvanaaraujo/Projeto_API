from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .turma_model import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma
from config import db

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Home page"

## ROTA PARA TODAS AS TURMAS
@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return render_template("turma.html", turmas=turmas)

## ROTA PARA UMA TURMA
@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_id.html', turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

## ROTA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UMA NOVA TURMA
@turmas_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turma_page():
    return render_template('turma_create.html')

## ROTA QUE CRIA UMA NOVA TURMA
@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    descricao = request.form['descricao']
    professor_id = request.form['professor_id']
    ativo = request.form.get('ativo', 'false').lower() == 'true'
    nova_turma = {
        'descricao': descricao,
        'professor_id': professor_id,
        'ativo': ativo
    }
    adicionar_turma(nova_turma)
    return redirect(url_for('turmas.get_turmas'))
    
## ROTA PARA O FORMULÁRIO PARA EDITAR UMA TURMA
@turmas_blueprint.route('/turmas/<int:id_turma>/editar', methods=['GET'])
def editar_turma_page(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_update.html', turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

## ROTA QUE EDITA UMA TURMA
@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT', "POST"])
def update_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        descricao = request.form['descricao']
        professor_id = request.form['professor_id']
        ativo = request.form.get('ativo', 'false').lower() == 'true'
        turma_update = {
            'descricao': descricao,
            'professor_id': professor_id,
            'ativo': ativo
        }
        atualizar_turma(id_turma, turma_update)
        return redirect(url_for('turmas.get_turma', id_turma=id_turma))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

## ROTA QUE DELETA UMA TURMA
@turmas_blueprint.route('/turmas/delete/<int:id_turma>', methods=['DELETE', 'POST'])
def delete_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return redirect(url_for('turmas.get_turmas'))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
