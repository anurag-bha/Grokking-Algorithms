import sys
path = sys.path.append(".") # Adds higher directory to python modules path.
from Grokking_Algorithms import GrokkingAlgorithms
class TestClass:
        def test_answer(self):        
                assert GrokkingAlgorithms().BinarySearch([1, 4, 5, 7, 9, 10], 5) == 2
        
