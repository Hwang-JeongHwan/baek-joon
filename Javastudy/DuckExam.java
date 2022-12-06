package Javastudy;

public class DuckExam {
    public static void main(String[] args) {
        Duck duck = new Duck();
        duck.sing();
        duck.fly();
        // 상속받은 클래스이기 때문에 추상메소드 이외의 메소드도 사용 가능
        Bird b = new Bird();
        // 추상클래스는 부모로서의 역할을 가능하지만 추상클래스를 이용해서
        // 객체를 생성한다던지 하는 기능은 사용할수 없음 
    }
    
}
