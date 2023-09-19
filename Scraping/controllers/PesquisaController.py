from typing import Type

from repositories.PesquisaRepository import PesquisaRepository

class PesquisaController:
    
    def Pesquisar(url:str):
        
        urlTratada = url.trim().lower()
        df = PesquisaRepository.get_pesquisa(url)
        return df
        
