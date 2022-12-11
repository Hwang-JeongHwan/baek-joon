package Javastudy.javaUtilExam;
/* 쓰레드 제어문중 하나인 join() 메소드
 * join()메소드는 쓰레드가 멈출때 까지 기다리게 해주는 메소드임
 * 
*/
public class MyThread5  extends Thread{
   
    @Override
    public void run() {
        // TODO Auto-generated method stub
        //super.run();
        for (int i =0; i < 5; i++){
            System.out.println("Mythread5 : " + i);
            try {
                Thread.sleep(500);
                // 0.5초 씩 쉬면서 실행시킴
                // join이라는 메소드를 통해서 테스트진행
            } catch (Exception e) {
                //TODO: handle exception
                e.printStackTrace();
            }
        }
    } 
}
