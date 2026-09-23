# 🏛️ Software Architecture Lab

Um laboratório em Python para estudar **arquitetura de software**, com foco em separação de responsabilidades, injeção de dependências e arquitetura em camadas.

> Projeto educacional: o repositório usa um banco de dados em memória para demonstrar conceitos arquiteturais sem depender de serviços externos.

## 🎯 Objetivos

- entender separação de responsabilidades;
- praticar arquitetura em camadas;
- aplicar injeção de dependências;
- manter regras de negócio independentes do armazenamento;
- escrever testes automatizados;
- documentar decisões e conceitos de arquitetura.

## 🧩 Arquitetura demonstrada

O projeto possui três responsabilidades principais:

1. **Repository** — acessa os dados dos usuários.
2. **Service** — concentra a regra de negócio para verificar o status do usuário.
3. **Presentation / Entry Point** — executa a aplicação e apresenta os resultados.

O `UsuarioService` recebe um `UsuarioRepository`, em vez de criar sua própria dependência. Isso demonstra uma forma simples de **injeção de dependência** e reduz o acoplamento entre as camadas.

## ✨ Funcionalidades

- cadastro inicial de usuários em memória;
- busca por ID;
- identificação de usuário ativo ou inativo;
- tratamento de usuário inexistente;
- modelo de domínio com `dataclass`;
- testes automatizados com `unittest`;
- GitHub Actions para execução dos testes.

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/marcellabongiolo/software-architecture-lab.git
cd software-architecture-lab
python camadas_sistema.py
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

O projeto não possui dependências externas.

## 📁 Estrutura

```text
software-architecture-lab/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_camadas_sistema.py
├── .gitignore
├── LICENSE
├── README.md
└── camadas_sistema.py
```

## 🧠 Conceitos praticados

- arquitetura em camadas;
- Separation of Concerns;
- Repository Pattern;
- Service Layer;
- injeção de dependências;
- baixo acoplamento;
- dataclasses;
- type hints;
- testes automatizados;
- integração contínua.

## 🚀 Próximos passos possíveis

- separar as camadas em módulos e diretórios próprios;
- criar uma interface/abstração para o repositório;
- adicionar operações de criação, atualização e remoção;
- substituir o armazenamento em memória por SQLite;
- adicionar uma API HTTP;
- explorar Clean Architecture e Ports and Adapters.

## 👩‍💻 Autora

**Marcella Bongiolo**

- GitHub: https://github.com/marcellabongiolo
- LinkedIn: https://linkedin.com/in/marcellabongiolo

## 📄 Licença

Este projeto está sob a licença MIT.
