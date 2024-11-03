Atividade que vamos evoluir ao longo do semestre.

Professor
- Id
- nome
- idade
- matéria
- observações

Turma
- id
- descricao
- Professor
- ativo

Aluno
- id
- nome
- idade
- Turma
- data de nascimento
- nota do primeiro semestre
- nota do segundo semestre
- media final

- A entidade professor deverá ser relacionado com turma, One to Many (um professor
  poderá estar presente em muitas turmas, porém uma turma terá apenas um
  professor)

- A entidade de aluno devera estar relacionado com turma, One to Many (O aluno
  poderá ter apenas uma turma, porém uma turma poderá ter muitos alunos)
 No código podemos implementar as relações entre as entidades Professor e Turma, e entre Turma e Aluno, de maneira simples usando IDs.  

1. Relação entre Professor e Turma
Um professor pode estar em muitas turmas (One-to-Many).
Uma turma tem apenas um professor
A relação entre Professor e Turma é estabelecida através do campo professor_id dentro da entidade Turma. Esse campo armazena o ID do professor que ensina a turma.

  
2. Relação entre Turma e Aluno
Um aluno pode ter apenas uma turma (One-to-Many).
Uma turma pode ter muitos alunos.
 A relação entre Turma e Aluno é estabelecida através do campo turma_id dentro da entidade Aluno. Esse campo armazena o ID da turma à qual o aluno pertence.
