import abc
from archi.checkers.Checker import Checker
import numpy as np


Mat = np.ndarray
class CheckerReverseRes(Checker, metaclass=abc.ABCMeta):
    def result(self)-> None:
        for key in dict(sorted(self.history.items(), key=lambda item: item[1])):
            self.resultOnce(key)