package Javastudy.javaUtilExam;

public class ThreadExam {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1("*");
        MyThread1 t2 = new MyThread1("-");

        // 쓰레드를 동작시키게 할때 run을 호출하는게 아니라 start라는 메소드를 호출
        // 해야함 -> start : 쓰레드가 실행할 준비를 하게 해주는 메소드
        // 쓰레드가 실행될 준비가 되면 run메소드 호출

        // 즉 start()메소드를 호출하지 않으면 쓰레드는 동작하지 않음 
        t1.start();
        t2.start();
        // 이렇게 하면 수행흐름이 3개가 됨, t1,t2, + main
        System.out.println("main end!!!");
        // main쓰레드가 종료되었다 하더라도 프로그램이 종료되는것이 아님
        // main쓰레드가 종료 되었다 하더라도 다른 쓰레드 모두 흐름이 종류 되어야
        // 프로그램이 종료됨 

    }
}
