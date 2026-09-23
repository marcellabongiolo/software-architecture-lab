"""
Módulo: Demonstração de Arquitetura em Camadas (Layered Architecture)
Autor: Marcella Bongiolo
Descrição: Exemplo prático de separação de responsabilidades: 
           Camada de Dados (Simulando DB), Camada de Regra de Negócio (Serviço) 
           e Camada de Apresentação.
"""

# ==========================================
# 1. CAMADA DE DADOS (Persistência / Simulação de Banco)
# ==========================================
class UsuarioRepository:
    """Responsável exclusivamente por buscar e salvar dados."""
    def __init__(self):
        # Simulando um banco de dados em memória
        self._db = [
            {"id": 1, "nome": "Marcela", "ativo": True},
            {"id": 2, "nome": "Carlos", "ativo": False}
        ]

    def buscar_por_id(self, usuario_id: int):
        for usuario in self._db:
            if usuario["id"] == usuario_id:
                return usuario
        return None


# ==========================================
# 2. CAMADA DE NEGÓCIO (Serviços / Regras)
# ==========================================
class UsuarioService:
    """Responsável pelas regras de negócio da aplicação."""
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def verificar_status_usuario(self, usuario_id: int) -> str:
        usuario = self.repository.buscar_por_id(usuario_id)
        
        if not usuario:
            return f"Erro: Usuário com ID {usuario_id} não foi encontrado."
        
        if usuario["ativo"]:
            return f"Sucesso: O usuário '{usuario['nome']}' está ativo no sistema."
        else:
            return f"Aviso: O usuário '{usuario['nome']}' está inativo."


# ==========================================
# 3. CAMADA DE APRESENTAÇÃO (Interface / Execução)
# ==========================================
def main():
    print("=" * 60)
    print(" 🏛️ SOFTWARE ARCHITECTURE LAB: ARQUITETURA EM CAMADAS ⚙️")
    print("=" * 60)

    # Inicializando as dependências (Injeção de dependência básica)
    repo = UsuarioRepository()
    service = UsuarioService(repo)

    # Testando cenários diferentes
    print(service.verificar_status_usuario(1))
    print(service.verificar_status_usuario(2))
    print(service.verificar_status_usuario(99)) # Testando ID inexistente
    
    print("=" * 60)

if __name__ == "__main__":
    main()
  Add layered architecture and repository pattern example
