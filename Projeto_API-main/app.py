import os
from config import app,db

from professores.professor_routes import professores_blueprint
from turmas.turma_routes import turmas_blueprint
from alunos.aluno_routes import alunos_blueprint
# from professor.index import professor

app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)
app.register_blueprint(alunos_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )