public class SortingAlgorithms {

    public static void bubbleSort(int[] array) {
        int n = array.length;
        int temp;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    private void insertionSort(int[] array) {
        int n = array.length;
        for (int i = 1; i < n; i++) {
            int key = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key;
        }
    }

    public static void merge(int[] array, int left, int middle, int right) {

        int n1 = middle - left + 1;
        int n2 = right - middle;

        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        for (int i = 0; i < n1; ++i) {
            leftArray[i] = array[left + i];
        }

        for (int j = 0; j < n2; ++j) {
            rightArray[j] = array[middle + 1 + j];
        }

        int i = 0;
        int j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                array[k] = leftArray[i];
                i++;
            }
            else {
                array[k] = rightArray[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            array[k] = leftArray[i];
            i++;
            k++;
        }

        while (j < n2) {
            array[k] = rightArray[j];
            j++;
            k++;
        }
    }

    public static void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;

            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);

            merge(array, left, middle, right);
        }
    }

    public static void main(String[] args){

        int[] arrayMS = new int[3];
        int nMS = arrayMS.length;
        arrayMS[0] = 5;
        arrayMS[1] = 1;
        arrayMS[2] = -2;
        mergeSort(arrayMS, 0, nMS - 1);

        for (int i = 0; i < nMS; i++) {
            System.out.println(arrayMS[i]);
        }

        int[] arrayIS = new int[5];
        int nIS = arrayIS.length;
        arrayIS[0] = -1;
        arrayIS[1] = -4;
        arrayIS[2] = 5;
        arrayIS[3] = 1;
        arrayIS[4] = -8;
        SortingAlgorithms sa = new SortingAlgorithms();
        sa.insertionSort(arrayIS);

        for (int i = 0; i < nIS; i++) {
            System.out.println(arrayIS[i]);
        }


    }

}







