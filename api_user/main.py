# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:14:28 2023

@author: Everton
"""
from user.user import User

if __name__ == '__main__':
    usuario = User('EvertonMutti')
    usuario.obterDados()
    print(usuario)
    print(usuario.obterRepositorios())
    if usuario.gerarArquivo():
        print('Arquivo gerado com sucesso')