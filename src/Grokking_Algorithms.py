import numpy
class GrokkingAlgorithms:

        def __init__(self):
                self.BinSearch_idx = []
                self.MinNumber = []
                self.MinId = []
        
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


        def SmallestNumber(self, arr):
                # function to find the smallest number in an array
                self.MinNumber = arr[0]
                self.MinId = 0
                for i in range(len(arr)-1):
                
                    if arr[i+1] < self.MinNumber:
                        self.MinNumber = arr[i+1]
                        self.MinId = i+1
                return self.MinNumber, self.MinId
    
    
        def SelectionSort(self, arr):
                # function for selection sort
                new_arr = []
                while len(arr)>0:
                    self.SmallestNumber(arr)
                    new_arr.append(self.MinNumber)
                    arr.pop(self.MinId)
                return new_arr


        
