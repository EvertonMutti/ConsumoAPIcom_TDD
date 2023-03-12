# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:54:53 2023

@author: Everton
"""
import requests

class User:
    def __init__(self, username: str):
        self.username: str = username
        self.nome: str = ''
        self.url_perfil: str = ''
        self.num_repos_publicos: int = 0
        self.num_seguidores: int = 0
        self.num_seguindo: int = 0

    def obterDados(self) -> None:
        """
        Obtêm os dados do usuário a partir do username passado na inicialização da classe.
        
        Raises
        ------
        Exception
            Informa o status code da requisição.

        Returns
        -------
        None
            preenche os atributos do objeto com a informação do username.

        """
        
        url: str = f'https://api.github.com/users/{self.username}'
        resposta = requests.get(url)

        if resposta.status_code == 403:
            raise Exception(f'Api do github tem limite de requisições: {resposta.status_code}')
        elif resposta.status_code != 200:
            raise Exception(f'Erro ao fazer requisição: {resposta.status_code}')

        dados: dict = resposta.json()        
        self.nome = dados.get('name')
        self.url_perfil = dados.get('html_url')
        self.num_repos_publicos = dados.get('public_repos')
        self.num_seguidores = dados.get('followers')
        self.num_seguindo = dados.get('following')
    
    def obterRepositorios(self) -> dict[str: str]:
        """
        Obtêm os repositórios do usuário a partir do username passado na inicialização da classe.

        Raises
        ------
        Exception
            Informa o status code da requisição.

        Returns
        -------
        dict
            {'repositórios': 'urls'}.

        """
        
        url: str = f'https://api.github.com/users/{self.username}/repos'
        resposta = requests.get(url)
        
        if resposta.status_code == 403:
            raise Exception(f'Api do github tem limite de requisições: {resposta.status_code}')
        elif resposta.status_code != 200:
            raise Exception(f'Erro ao fazer a requisição: {resposta.status_code}')

        dados: dict = resposta.json()
        repositorios = {}
        for repo in dados:
            repositorios[repo.get('name')] = repo.get('html_url')

        return repositorios
        
    def gerarArquivo(self) -> bool:
        """
        Obtêm os repositórios e dados do usuário os transferindo para um arquivo
        txt com o nome do username fornecido na inicialização do objeto.
        
        Returns
        -------
        bool
            Retorna True caso gere o arquivo.

        """
        
        self.obterDados()
        repositorios = self.obterRepositorios()
        nome_arquivo = f"{self.username}.txt"
        
        try:
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(f"Nome: {self.nome}\n")
                arquivo.write(f"Perfil: {self.url_perfil}\n")
                arquivo.write(f"Número de repositórios publicos: {self.num_repos_publicos}\n")
                arquivo.write(f"Número de seguidores: {self.num_seguidores}\n")
                arquivo.write(f"Número de usuários seguidos: {self.num_seguindo}\n\n")
                
                arquivo.write("Repositórios:\n")
                for nome, url in repositorios.items():
                    arquivo.write(f"\t{nome}: {url}\n")
            
                    
        except PermissionError:
            raise PermissionError("Não foi possível criar nem escrever no arquivo. Verifique as permissões de acesso.")
        
        except Exception as erro:
            raise erro
            
        return True

if __name__ == '__main__':
    usuario = User('EvertonMutti')
    usuario.obterDados()
    usuario.obterRepositorios()
    usuario.gerarArquivo()
