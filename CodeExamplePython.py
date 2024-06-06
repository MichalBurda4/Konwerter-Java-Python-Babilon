
class SortingAlgorithms:

    @staticmethod
    def bubbleSort(array):
        n = len(array)
        temp = None
        for i in range(0, n-1, 1):
            for j in range(0, n-i-1, 1):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

    def insertionSort(self, array):
        n = len(array)
        for i in range(1, n, 1):
            key = int(array[i])
            j = int(i-1)
            while j>=0 and array[j]>key:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key

    @staticmethod
    def merge(array, left, middle, right):
        n1 = int(middle-left+1)
        n2 = int(right-middle)
        leftArray = [0] * n1
        rightArray = [0] * n2
        for i in range(0, n1, 1):
            leftArray[i] = array[left+i]
        for j in range(0, n2, 1):
            rightArray[j] = array[middle+1+j]
        i = int(0)
        j = int(0)
        k = int(left)
        while i<n1 and j<n2:
            if leftArray[i]<=rightArray[j]:
                array[k] = leftArray[i]
                i+=1
            else:
                array[k] = rightArray[j]
                j+=1
            k+=1
        while i<n1:
            array[k] = leftArray[i]
            i+=1
            k+=1
        while j<n2:
            array[k] = rightArray[j]
            j+=1
            k+=1

    @staticmethod
    def mergeSort(array, left, right):
        if left<right:
            middle = int((left+right)/2)
            SortingAlgorithms.mergeSort(array,left,middle)
            SortingAlgorithms.mergeSort(array,middle+1,right)
            SortingAlgorithms.merge(array,left,middle,right)

def main():
    arrayMS = [0] * 3
    nMS = len(arrayMS)
    arrayMS[0] = 5
    arrayMS[1] = 1
    arrayMS[2] = -2
    SortingAlgorithms.mergeSort(arrayMS,0,nMS-1)
    for i in range(0, nMS, 1):
        print(arrayMS[i])
    arrayIS = [0] * 5
    nIS = len(arrayIS)
    arrayIS[0] = -1
    arrayIS[1] = -4
    arrayIS[2] = 5
    arrayIS[3] = 1
    arrayIS[4] = -8
    sa = SortingAlgorithms()
    sa.insertionSort(arrayIS)
    for i in range(0, nIS, 1):
        print(arrayIS[i])

if __name__ == "__main__":
    main()
