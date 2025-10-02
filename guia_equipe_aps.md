# README — Guia de Trabalho em Equipe

**Repositório:** APS 4º semestre — Algoritmos de Estruturação de Dados

> Guia simples e funcional para o fluxo de trabalho GitHub do time. Ideal para primeiros projetos em equipe.

---

## 🚀 Objetivo

Manter um fluxo claro e leve para que cada membro trabalhe isoladamente, o líder revise e o `main` sempre contenha código estável e entregável.

---

## 🔁 Visão geral do fluxo

* `main`: código final / estável. Somente merges aprovados pelo líder (ou por revisão).
* `feature/<nome>`: branch criada por cada membro para implementar uma funcionalidade ou tarefa.

**Regra simples:**

* Trabalho diário em `feature/*` → abrir Pull Request para `main` quando pronto → revisão e merge.

---

## 📥 Como clonar (passo a passo)

```bash
# clonar o repositório
git clone git@github.com:SEU_USUARIO/NOME_REPOSITORIO.git
cd NOME_REPOSITORIO

# garantir que main está atualizada
git checkout main
git pull origin main
```

---

## 🌿 Criando e trabalhando em uma branch de feature

1. Puxe as atualizações do `main` antes de criar a branch:

```bash
git checkout main
git pull origin main
```

2. Crie a branch de feature (nome curto e descritivo):

```bash
git checkout -b feature/nome-da-funcionalidade
```

3. Faça commits pequenos e com mensagens claras (veja convenção abaixo).
4. Quando terminar, suba sua branch e abra um Pull Request:

```bash
git push -u origin feature/nome-da-funcionalidade
```

---

## ✍️ Convenção de mensagens de commit (sugestão simples)

Use mensagens curtas e descritivas: `tipo: descrição curta`

* Exemplos:

  * `feat: implementar fila encadeada`
  * `fix: corrigir caso de borda na ordenação`
  * `docs: adicionar explicação no README`

Prefira commits pequenos (1 responsabilidade por commit).

---

## 🔀 Pull Request (PR) — checklist antes de pedir revisão

* [ ] Código compila / roda localmente.
* [ ] Testes básicos (se houver) passam.
* [ ] Não há `console.log` / prints desnecessários.
* [ ] Adicionei descrição clara do que o PR faz.
* [ ] Marquei reviewer(s) (o líder pelo menos).

---

## ✅ Política de merge

* O líder revisa e aprova PRs. Pode delegar revisão a outro membro.
* Só faça merge quando a checklist estiver OK.

---

## 🐞 Issues e Organização de Tarefas

* Crie uma **Issue** para cada tarefa (ex: "Implementar busca binária").
* Use labels (ex: `bug`, `feat`, `docs`) e atribua um responsável.

---

## 💬 Boas práticas de equipe

* Faça `git pull` antes de começar a trabalhar no dia.
* Comunique impedimentos no PR ou na issue.
* Comente e explique código se a lógica não for trivial.
* Respeite revisões: aceite feedbacks e atualize o PR.

---

## 🔧 Comandos úteis (resumo rápido)

```bash
# atualizar main
git checkout main
git pull origin main

# criar branch
git checkout -b feature/nome

# adicionar, commitar e enviar
git add .
git commit -m "feat: descrição"
git push -u origin feature/nome

# após review, atualizar branch com main (se necessário)
git checkout feature/nome
git pull origin main
# ou
git fetch origin
git rebase origin/main
```

> Se não tiver prática com `rebase`, usar `merge` para reduzir erros: `git merge origin/main`.

---

## 📛 Exemplo de nomes de branch

* `feature/lista-encadeada`
* `feature/ordenacao-merge`
* `fix/caso-borda-insercao`
* `docs/readme-exemplos`

---

## 🧑‍💻 Papéis e responsabilidades (sugestão)

* **Líder (Nicolas):** revisão final, merges, gerenciamento de issues e organização.
* **Membros:** desenvolver features, abrir PRs, corrigir pontos apontados nas reviews.

---

## 🎯 Lider — ações imediatas (é necessário?)

Sim — como líder você não precisa fazer tudo sozinho, mas **precisa organizar** o fluxo para evitar confusão e plágio. Para um trabalho de faculdade simples, essas ações são suficientes e rápidas.

### Por que é importante

* Garante que o `main` fique estável.
* Evita sobrescrever trabalho de colegas.
* Facilita revisão e nota (professor pode olhar o repo).

### Ações que eu já preparei para você (pronto para copiar/colar)

Abaixo há **templates e arquivos úteis** para você colocar no repositório. Eu já incluí o conteúdo aqui para você criar no GitHub (ou eu posso gerar arquivos separados se quiser).

---

## 📄 CONTRIBUTING.md (cole como `CONTRIBUTING.md`)

```
# Contribuindo — Repositório APS 4º semestre

Obrigado por contribuir! Siga estas regras simples antes de abrir um Pull Request.

## Regras rápidas
- Crie uma branch a partir do `main` com nome `feature/<nome>` ou `fix/<nome>`.
- Faça commits pequenos e com mensagens no formato: `tipo: descrição` (ex: `feat: implementar fila encadeada`).
- Sempre puxe (`git pull`) o `main` antes de criar sua branch.
- Abra um Pull Request com descrição clara e assinale o revisor (o líder do projeto).

## Pull Requests
- Inclua o que foi feito, por que foi feito e instruções de como testar.
- Corrija comentários do revisor o quanto antes.
- Não faça merge até receber aprovação.

## Conduta
- Respeito nas revisões e feedbacks.
- Evite copiar código sem entender — cite fontes externas quando usar.
```

---

## 📝 ISSUE TEMPLATE (cole como `.github/ISSUE_TEMPLATE/issue_template.md`)

```
# Título: [tipo] resumo curto

**Tipo**: bug / feature / docs

**Descrição**:
Descreva o problema ou tarefa.

**Passos para reproduzir (se for bug)**:
1. 
2. 

**Resultado esperado**:

**Responsável sugerido**: @usuario
```

---

## 🔁 PULL REQUEST TEMPLATE (cole como `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`)

```
## Descrição
Que change este PR traz? (curto e objetivo)

## Tipo
- [ ] feat
- [ ] fix
- [ ] docs
- [ ] chore

## Como testar
Passos para avaliar este PR:
1. 
2. 

## Checklist
- [ ] Código compila/rode localmente
- [ ] Não há prints desnecessários
- [ ] Testes (se houver) passam
- [ ] Peer review solicitado (@lider)
```

---

## 🧭 Controle de Mudanças — políticas práticas (detalhado)


### Regras essenciais

* **Branches:** cada membro usa `feature/*` ou `fix/*` para desenvolver.
* **Pull Requests:** todo código entra no `main` via PR aprovado pelo líder.
* **Commits pequenos:** evita conflitos e facilita reverts.
* **Revisão:** leia o diff, rode o código localmente se necessário e deixe comentários claros.
* **Rebase vs Merge:** para iniciantes, usar `merge` é mais seguro.

### Como lidar com conflitos

* Peça ao autor para atualizar a branch com `git pull origin main` e resolver os conflitos localmente, depois atualizar a PR.
* Se o autor tiver dificuldades, ajude a resolver em par (pair programming) ou faça o merge manual com cuidado.

---

## 🗂️ Organização (tarefas e visibilidade)

### Issues

* Cada tarefa virou uma Issue com título claro e um responsável.
* Use labels: `todo`, `in-progress`, `done`, `bug`, `feature`, `docs`.

### Releases / Entregas

* Para entregas, crie uma **Release** no GitHub apontando a tag (ex: `v1.0`) contendo o que foi entregue.

