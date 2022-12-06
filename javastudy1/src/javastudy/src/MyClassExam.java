package javastudy1.src.javastudy.src;

public class MyClassExam {
    public static int returnValue(int x, int y){
        return x + y;
    }
    public static void main(String[] args) {
        MyClass myclass = new MyClass();
        myclass.method1();
        myclass.method2(10);
        int value = myclass.method3();
        System.out.println(value);
        int value1 = returnValue(3, 6);
        returnValues(3,99);
        int[] value2 = new int[1];
        myclass.method4(0, 0);
    }
    public static void returnValues(int x, int y){
        System.out.println(x + y);
    }

    
}
