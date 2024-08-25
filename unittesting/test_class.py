
from src import GrokkingAlgorithms
class TestClass:
        def test_answer(self):        
                assert GrokkingAlgorithms().BinarySearch([1, 4, 5, 7, 9, 10], 5) == 2

        def test_selection_sort(self):
                assert GrokkingAlgorithms().SelectionSort([1, 5, 4, 7, 10, 9]) == [1, 4, 5, 7, 9, 10]

        def test_selection_sort_with_equal_numbers(self):
                assert GrokkingAlgorithms().SelectionSort([1, 4, 4, 7, 10, 9, 5, 6]) == [1, 4, 4, 5, 6, 7, 9, 10]
        
