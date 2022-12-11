package Javastudy.javaUtilExam;

public class JoinExam {
    public static void main(String[] args) {
        MyThread5 thread = new MyThread5();
        thread.start();
        // 스레드를 상속받았기 때문에 thread.start()하면 실행됨
        // main도 하나의 스레드고 상속받은 thread도 하나의 스레드임 수행흐름이 2개가 만들어졋다는 의미
        System.out.println("시작");

        // join()이라는 메소드를 이용하게 되면 해당 스레드가 끝나버리지 않고
        // MyThread가 모두 실행이 될때 까지 기다려 줄수있는 메소드임
        try {
            thread.join();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // join이라는 메소드는 이렇듯 쓰레드가 멈출때 까지 기다리게 해주는 메소드임 

        System.out.println("종료");
    
    }
    
}
