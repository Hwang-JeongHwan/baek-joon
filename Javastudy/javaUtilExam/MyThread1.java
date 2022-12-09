package Javastudy.javaUtilExam;
/* 쓰레드 만들기(extend Thread)
 * 자바에서 Thread를 만드는 방법은 크게 Thread 클래스를 상속받는 방법과
 * Runnable인터페이스를 구현하는 방법이 있다.
 * 
 * Thread를 상속 받아서 쓰레드를 생성하는 방법 
 * java.lang.Thread클래스를 상속받는다. 그리고 Thread가 가지고 있는 
 * run()메소드를 오버라이딩한다.
 * 10번 반복하면서 str을 찍습니다. */
public class MyThread1 extends Thread {
    String str;
        
    public MyThread1(String str){
        this.str = str;
    }
    
    @Override //Thread의 run메소드를 Overriding
    public void run() {
        // TODO Auto-generated method stub
        //super.run();
        // 수행흐름이 하나 더 생겼을때에 흐름을 가지는 메소드 이기 때문에
        // 다른흐름의 메인메소드 정도라고 생각하면됨
        // 실제 수행흐름에서 하게되는 run이라는 메소드는 내가 수행흐름에서 
        // 뭐든 하고싶은걸로 할수있음
        for(int i = 0; i < 10; i ++){
            System.out.println(str);

            //너무빨리 끝나서 메소드 추가
            try {
                Thread.sleep((int)(Math.random() * 1000)); // 이 시간동안 잠깐 쉬어라, 자라
                // random = 0 ~ 0.9999초까지 랜덤으로 반환
            

            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }
    }

    
}
