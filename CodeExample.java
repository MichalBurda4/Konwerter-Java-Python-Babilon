private class test{
    private string myString = "abc";
    public int myInt = 4 * 5;

    private void run(){
        int x = 0;
        x = myInt;
        string myString2;
        string my = myString2;
        x = 5 * myInt;
    }
}


class test2{
    private void print(){
        string wypiszNaEkran = "abc"; 
    }
}

class test3{
    protected void print(){
        string wypiszNaEkran = "xyz"; 
    }
}

class tablica{
    protected void print(){
        int[] numbers = new int[5]; 
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        } 
    }
}

class TestOsiaganiaPola{
    public void pobierz(int pole1){
        int a = testPola.myInt;
    }
    private void sprawdz(){
        pobierz(testPola.myInt);
    }
}
