package Javastudy.javaUtilExam;

/* Runnable인터페이스를 구현해서 쓰레드를 만드는 방법
   Runable 인터페이스가 가지고 있는 run()메소드를 구현한다
  
 */
public class MyThread2 implements Runnable {
    String str;
    public MyThread2(String str){
        this.str = str;
        // 처음객체가 생성될때부터 String값을 가지고 생성할수 있도록
        // 생성자를 하나 넣어줌
    }
    // 기존에는 쓰레드를 상속받지만 이번에는 Runnable인터페이스를 구현하도록 살짝 바뀜
    // Runnable 인터페이스는 run()이라는 메소드를 가지고 있기 때문에
    // run()을 구현하면됨

    // Runnable 인터페이스를 구현해서 만드는 방법을 자바가 제공하는 이유는
    // 자바는 단일상속만 지원하기 때문임 -> 이미 다른 클래스를 상속받고있었으면
    // 쓰레드 클래스를 또 상속 받을수 없기 때문임
    // 이런경우에도 쓰레드가 꼭필요하다 하는 경우에 사용할수 있는 방법이 있어야함
    // 인터페이스는 여러개 구현해서 사용할 수 있기 때문에 다른 클래스를 상속받고
    // 있다면 Runnable인터페이스를 구현해서 스레드를 작성하면 됨 

    // Runnable 인터페이스를 구혀낳ㄴ MyThread2는 Thread를 상속받지 않았기 때문에
    // Thread가 아님
    // Thread를 생서앟고 해당 생성자에 MyThread2를 넣어서 Thread를 생성해야함

    @Override
    public void run() {
        // TODO Auto-generated method stub
        for(int i = 0; i < 10; i ++){
            System.out.println(str);
            try {   
                Thread.sleep((int)(Math.random() * 1000));
                
            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }
    }
    
}
