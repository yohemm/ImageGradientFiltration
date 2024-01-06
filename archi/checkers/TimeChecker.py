if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.checkers.CheckerReverseRes import CheckerReverseRes
from archi.filters.Filter import Filter
import cv2
import os
import time

class TimeChecker(CheckerReverseRes):
    
    def checkLogical(self, filter:Filter)-> any:
        stri = os.path.join(os.getcwd(), 'src', 'source_image', 'barnard_stacked_gradient.png')
        start = TimeChecker.current_milli_time()
        # A tester (cause de problem)

        filter.use(cv2.imread(stri), "poubel.png")
        end = TimeChecker.current_milli_time()
        return end - start
        
    @staticmethod
    def current_milli_time():
        return time.time()
    
if __name__ == "__main__":
    from archi.filters.SobelFilter import SobelFilter
    timeCheck = TimeChecker()
    timeCheck.check(SobelFilter())
    timeCheck.result()
                        