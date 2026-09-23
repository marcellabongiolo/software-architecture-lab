"""Exemplo de arquitetura em camadas para gerenciamento de usuários.

O exemplo separa acesso a dados, regras de negócio e ponto de entrada da
aplicação, permitindo substituir a implementação do repositório sem alterar
o serviço.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Usuario:
    """Representa um usuário do sistema."""

    id: int
    nome: str
    ativo: bool


class UsuarioRepository:
    """Responsável pelo acesso aos dados dos usuários."""

    def __init__(self, usuarios: list[Usuario] | None = None) -> None:
        self._db = usuarios if usuarios is not None else [
            Usuario(id=1, nome="Marcela", ativo=True),
            Usuario(id=2, nome="Carlos", ativo=False),
        ]

    def buscar_por_id(self, usuario_id: int) -> Usuario | None:
        """Busca um usuário pelo identificador."""
        return next(
            (usuario for usuario in self._db if usuario.id == usuario_id),
            None,
        )


class UsuarioService:
    """Centraliza as regras de negócio relacionadas a usuários."""

    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def verificar_status_usuario(self, usuario_id: int) -> str:
        """Retorna uma mensagem de acordo com o status do usuário."""
        usuario = self.repository.buscar_por_id(usuario_id)

        if usuario is None:
            return f"Erro: usuário com ID {usuario_id} não foi encontrado."

        if usuario.ativo:
            return f"Sucesso: o usuário '{usuario.nome}' está ativo no sistema."

        return f"Aviso: o usuário '{usuario.nome}' está inativo."


def main() -> None:
    """Executa uma demonstração da arquitetura em camadas."""
    repository = UsuarioRepository()
    service = UsuarioService(repository)

    print("=" * 60)
    print("SOFTWARE ARCHITECTURE LAB")
    print("=" * 60)
    print(service.verificar_status_usuario(1))
    print(service.verificar_status_usuario(2))
    print(service.verificar_status_usuario(99))
    print("=" * 60)


if __name__ == "__main__":
    main()
