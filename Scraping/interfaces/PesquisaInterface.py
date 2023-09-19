from typing import Type
from abc import ABC, abstractmethod
from entities.Pesquisa import Pesquisa

class PesquisaIterface(ABC):
    
    @abstractmethod
    def GetUrl(url:str):
        pass