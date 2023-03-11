# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:14:28 2023

@author: Everton
"""
from user.user import User

if __name__ == '__main__':
    usuario = User('EvertonMutti')
    usuario.obterDados()
    print(usuario.nome)
    print(usuario.url_perfil)
    print(usuario.num_repos_publicos)
    print(usuario.num_seguidores)
    print(usuario.num_seguindo)
    print(usuario.obterRepositorios())