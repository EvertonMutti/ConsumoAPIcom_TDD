Objetivo: Consumir API do Github e transferir as informações para class User.

Class User terá que ter 5 atributos para representar os dados do usuário:
        nome: str
        url_perfil: str
        num_repos_publicos: int
        num_seguidores: int
        num_seguindo: int

Class User __init__ receberá 1 argumento sendo ele o nome do usuário.:
	username: str

Class User terá 1 método que obtem os dados do usuário e guardará as informações nos atributos e não retornará nada:
	*O método será chamado sem a necessidade de um argumento*
	
Class User terá 1 método que retornará os repositorios do usuário em dict:
	*O método será chamado sem a necessidade de um argumento*

Class User terá 1 método que cria ou substitui um arquivo txt e não retorna nada:
	*O método será chamado sem a necessidade de um argumento*
	 Obs: utilizar o modo w na criação do arquivo.

Class User __str__ (Bônus opcional) retornará as informações no terminal assim que chamado o objeto:
	nome: str
        url_perfil: str
        num_repos_publicos: int
        num_seguidores: int
        num_seguindo: int
	
