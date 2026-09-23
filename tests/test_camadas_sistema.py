import unittest

from camadas_sistema import Usuario, UsuarioRepository, UsuarioService


class TestUsuarioService(unittest.TestCase):
    def setUp(self):
        repository = UsuarioRepository([
            Usuario(id=1, nome="Ana", ativo=True),
            Usuario(id=2, nome="Bruno", ativo=False),
        ])
        self.service = UsuarioService(repository)

    def test_usuario_ativo(self):
        resultado = self.service.verificar_status_usuario(1)
        self.assertIn("Ana", resultado)
        self.assertIn("ativo", resultado)

    def test_usuario_inativo(self):
        resultado = self.service.verificar_status_usuario(2)
        self.assertIn("Bruno", resultado)
        self.assertIn("inativo", resultado)

    def test_usuario_inexistente(self):
        resultado = self.service.verificar_status_usuario(99)
        self.assertIn("não foi encontrado", resultado)

    def test_repository_busca_por_id(self):
        repository = UsuarioRepository([Usuario(id=7, nome="Lia", ativo=True)])
        usuario = repository.buscar_por_id(7)

        self.assertEqual(usuario.nome, "Lia")
        self.assertTrue(usuario.ativo)

    def test_repository_retorna_none_para_id_inexistente(self):
        repository = UsuarioRepository()
        self.assertIsNone(repository.buscar_por_id(999))


if __name__ == "__main__":
    unittest.main()
