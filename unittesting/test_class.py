import sys
path = sys.path.append(".") # Adds higher directory to python modules path.
# https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import
# Check the above stackoverflow for explaination of the single dot for accessing higher-level files
from Grokking_Algorithms import GrokkingAlgorithms
class TestClass:
        def test_answer(self):        
                assert GrokkingAlgorithms().BinarySearch([1, 4, 5, 7, 9, 10], 5) == 2
        
