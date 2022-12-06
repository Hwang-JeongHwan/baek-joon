package Javastudy;

public abstract class Bird {
    public abstract void sing();
    // 추상클래스는 메소드 뒤에 세미콜론찍으면됨 
    // 메소드가 하나라도 추상 메소드인경우 해당 클래스는 추상 클래스이다.

    public void fly(){
        //추상클래스는 추상메소드만 가질수 있진 않음
        // 일반 메소드도 구현 가능
        System.out.println("날다");
    }
}
