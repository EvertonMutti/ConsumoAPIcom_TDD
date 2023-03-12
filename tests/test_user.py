# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:55:15 2023

@author: Everton
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../api_user'
            )
        )
    )
except:
    raise
    
import unittest
from user.user import User
from unittest.mock import patch

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User('EvertonMutti')
    
    def test_User_assertion_username_str(self):
        self.assertIsInstance(self.user.username, str)
    
    def test_User_assertion_atributos(self):
        self.assertIsInstance(self.user.nome, str)
        self.assertIsInstance(self.user.url_perfil, str)
        self.assertIsInstance(self.user.num_repos_publicos, int)
        self.assertIsInstance(self.user.num_seguidores, int)
        self.assertIsInstance(self.user.num_seguindo, int)
    
    def test_obterDados(self):
        #Dados falsos
        resposta_dados_mock = {
            'name': 'Everton Mutti',
            'html_url': 'https://github.com/EvertonMutti',
            'public_repos': 10,
            'followers': 2,
            'following': 5,
        }
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = resposta_dados_mock
            self.user.obterDados()
            
        self.assertEqual(self.user.nome, 'Everton Mutti')
        self.assertEqual(self.user.url_perfil, 'https://github.com/EvertonMutti')
        self.assertEqual(self.user.num_repos_publicos, 10)
        self.assertEqual(self.user.num_seguidores, 2)
        self.assertEqual(self.user.num_seguindo, 5)
    
    def test_repositorios(self):
        #Dados falsos
        respositorios_mock = [
            {'name': 'igottafeeling', 'html_url': 'https://github.com/testuser/igottafeeling'},
            {'name': 'millaeumanoite', 'html_url': 'https://github.com/testuser/millaeumanoite'},
            {'name': 'prefixodeverao', 'html_url': 'https://github.com/testuser/prefixodeverao'},
        ]
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = respositorios_mock
            repositorios = self.user.obterRepositorios()
            
        for res_mock in respositorios_mock:
            with self.subTest(saida=res_mock.get('html_url')):
                self.assertEqual(repositorios['igottafeeling'], 'https://github.com/testuser/igottafeeling')
                self.assertEqual(repositorios['millaeumanoite'], 'https://github.com/testuser/millaeumanoite')
                self.assertEqual(repositorios['prefixodeverao'], 'https://github.com/testuser/prefixodeverao')
    
    def test_gerarArquivo(self):
        resposta_dados_mock = {
            'name': 'Everton Mutti',
            'html_url': 'https://github.com/EvertonMutti',
            'public_repos': 10,
            'followers': 2,
            'following': 5,
        }
        respositorios_mock = [
            {'name': 'igottafeeling', 'html_url': 'https://github.com/testuser/igottafeeling'},
            {'name': 'millaeumanoite', 'html_url': 'https://github.com/testuser/millaeumanoite'},
            {'name': 'prefixodeverao', 'html_url': 'https://github.com/testuser/prefixodeverao'},
        ]
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.side_effect = [resposta_dados_mock, respositorios_mock]
            
            self.user.gerarArquivo()
            
            with open(self.user.username + '.txt', 'r') as arquivo:
                arquivo_text = arquivo.read()
                
            self.assertIn("Nome: Everton Mutti", arquivo_text)
            self.assertIn("Perfil: https://github.com/EvertonMutti", arquivo_text)
            self.assertIn("Repositórios:", arquivo_text)
            self.assertIn("igottafeeling: https://github.com/testuser/igottafeeling", arquivo_text)
            self.assertIn("millaeumanoite: https://github.com/testuser/millaeumanoite", arquivo_text)
            self.assertIn("prefixodeverao: https://github.com/testuser/prefixodeverao", arquivo_text)
            
        os.remove(self.user.username + '.txt')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
        