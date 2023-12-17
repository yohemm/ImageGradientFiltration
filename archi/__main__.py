from archi.checkers.TimeChecker import TimeChecker
from archi.filters.GaussianBlur import GaussianBlurFilter



import sys
from pprint import pprint
pprint(sys.path)
sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration\\archi')
pprint(sys.path)
filter = GaussianBlurFilter()
checker = TimeChecker()

checker.check(filter)
checker.result()

