package Javastudy;

public class Duck extends Bird {

    @Override
    public void sing() {
        // TODO Auto-generated method stub
        System.out.println("꽥꽥!!");
    }
    //추상클래스를 상속받은 클래스는 무조건 추상메소드를 구현해야함
    // 추상클래스를 상속받고 추상 클래스가 가지고 있는 추상메소드를 구현하지
    // 않으면 해당 클래스도 추상 클래스가 된다. 

}
