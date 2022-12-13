package Javastudy.javaUtilExam;

public class ThreadExam2 {
    public static void main(String[] args) {
        MyThread2 t1 = new MyThread2("*");
        MyThread2 t2 = new MyThread2("-");

        // 쓰레드가 run이라는 메소드를 직접호출하는게 아니라 start라는 메소드를 
        // 호출 해야함 -> 근데 MyThread2는 쓰레드를 상속받은게 아니기 때문에 
        // start라는 메소드가 없고 run이라는 메소드 밖에 없음

        // 이상태에서 start라는 메소드를 호출 할수없음
        // 이런 문제들을 해결하기 위해서는 실제 수행할때 쓰레드 객체를 하나 만들어
        // 주어야함
        Thread thread1 = new Thread(t1);
        Thread thread2 = new Thread(t2);
        //여기에다가 아까 Runnable을 상속받은 애를 넣어주면됨
        // Thread의 생성자를 보면  Runnable 받아들일수 있게 되어있음
        // MyThread2는 Runnable을 인터페이스를 구현하고있기 때문에 이 생성자를 이용할
        // 수 있음

        thread1.start();
        thread2.start();
        // 상속을 바로 받을수 없기 때문에 이런 방식을 이용
        // 이렇게해도 실행결과는 똑같음
        System.out.println("main end!!");
    }
    
}
