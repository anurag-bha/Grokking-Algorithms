import numpy
class GrokkingAlgorithms:

        def __init__(self):
                self.BinSearch_idx = []
        
        def BinarySearch(self, arr, keynumber):
                low = 0
                high = len(arr)-1
                
                flag = 1
                itr = 0
                while flag == 1:
                        mid = (low + high) // 2
                        if arr[mid] == keynumber:
                
                                flag = 0
                                itr = itr + 1
                                self.BinSearch_idx = mid
                                break
                        elif keynumber > arr[mid]:
                                low = mid +1
                                itr = itr + 1
                        elif keynumber < arr[mid]:
                                high = mid-1
                                itr = itr + 1
                        else:
                                return None
                return self.BinSearch_idx


        
