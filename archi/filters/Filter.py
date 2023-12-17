import abc
import cv2
import numpy as np


Mat = np.ndarray

class Filter(abc.ABC,metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def logical(self, image:Mat)-> Mat:
        raise NotImplementedError('I need to be implemented!')
    
    def use(self, image:Mat, filterFuturPath:str)-> Mat:
        cv2.imwrite("src/retourn_image/"+filterFuturPath, self.logical(image))

    
    