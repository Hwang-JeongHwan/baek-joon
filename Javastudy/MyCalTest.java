package Javastudy;

public class MyCalTest {
    public static void main(String[] args) {
        
        Calculator cal = new MyCal();
        cal.plus(3, 1);
        int i = cal.exec(5, 6);
        System.out.println(i);
        // 인터페이스가 default키워드로 선언되면 메소드가 구현될 수 있다. 
        // 또한 이를 구현하는 클래스는 default메소드를 오버라이딩 할 수 있다.
        Calculator.exec2(3, 4);
        // 인터페이스의 static method 사용법
    }
    
}
