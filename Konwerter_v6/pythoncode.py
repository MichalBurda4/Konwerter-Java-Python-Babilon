
class BubbleSort:

    def bubbleSort(self, array):
        n = None
        n = array.length
        temp = None
        for i in range(n-1):
            for j in range(n-i-1):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp


