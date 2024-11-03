from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .aluno_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno
from config import db

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Home page"

## ROTA PARA TODOS OS ALUNOS
@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("aluno.html", alunos=alunos)

## ROTA PARA UM ALUNO
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

## ROTA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UM NOVO ALUNO
@alunos_blueprint.route('/alunos/adicionar', methods=['GET'])
def adicionar_aluno_page():
    return render_template('aluno_create.html')

## ROTA QUE CRIA UM NOVO ALUNO
@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    nome = request.form['nome']
    idade = request.form['idade']
    turma_id = request.form['turma_id']
    data_nascimento = request.form['data_nascimento']
    nota_primeiro_semestre = request.form['nota_primeiro_semestre']
    nota_segundo_semestre = request.form['nota_segundo_semestre']
    media_final = request.form['media_final']
    
    novo_aluno = {
        'nome': nome,
        'idade': idade,
        'turma_id': turma_id,
        'data_nascimento': data_nascimento,
        'nota_primeiro_semestre': nota_primeiro_semestre,
        'nota_segundo_semestre': nota_segundo_semestre,
        'media_final': media_final
    }
    adicionar_aluno(novo_aluno)
    return redirect(url_for('alunos.get_alunos'))

## ROTA PARA O FORMULÁRIO PARA EDITAR UM ALUNO
@alunos_blueprint.route('/alunos/<int:id_aluno>/editar', methods=['GET'])
def editar_aluno_page(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

## ROTA QUE EDITA UM ALUNO
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT', "POST"])
def update_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        nome = request.form['nome']
        idade = request.form['idade']
        turma_id = request.form['turma_id']
        data_nascimento = request.form['data_nascimento']
        nota_primeiro_semestre = request.form['nota_primeiro_semestre']
        nota_segundo_semestre = request.form['nota_segundo_semestre']
        media_final = request.form['media_final']

        aluno_update = {
            'nome': nome,
            'idade': idade,
            'turma_id': turma_id,
            'data_nascimento': data_nascimento,
            'nota_primeiro_semestre': nota_primeiro_semestre,
            'nota_segundo_semestre': nota_segundo_semestre,
            'media_final': media_final
        }
        atualizar_aluno(id_aluno, aluno_update)
        return redirect(url_for('alunos.get_aluno', id_aluno=id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

## ROTA QUE DELETA UM ALUNO
@alunos_blueprint.route('/alunos/delete/<int:id_aluno>', methods=['DELETE', 'POST'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return redirect(url_for('alunos.get_alunos'))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
