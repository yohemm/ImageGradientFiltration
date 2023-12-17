from archi.filters.Filter import Filter
import abc
import numpy as np


Mat = np.ndarray

class Checker(abc.ABC):
    history: dict[Filter, any] = {}
    
    @abc.abstractmethod
    def checkLogical(self, filter:Filter)-> any:
        raise NotImplementedError('I need to be implemented!')
    
    def check(self, filter:Filter)-> Mat:
        self.history[filter] = self.checkLogical(filter)
        
    def resultOnce(self, key:Filter):
        print(str(key.__class__) + "  :   "+str(self.history[key] )+" \n")
        
    def result(self)-> None:
        for key in dict(sorted(self.history.items())):
            self.resultOnce(key)
    