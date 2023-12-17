if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.checkers.CheckerReverseRes import Checker
from archi.filters.Filter import Filter


class TemplateChecker(Checker):
    
    def checkLogical(self, filter:Filter)-> any:
        pass
    
    
    
    
    
if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(TemplateChecker()) # A remplace
    
    timeCheck.result()
                        