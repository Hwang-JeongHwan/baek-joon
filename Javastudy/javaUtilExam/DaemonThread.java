package Javastudy.javaUtilExam;
// 데몬이란 보통 리눅스나 유닉스 계열의 운영체제에서 백그라운드로 동작하는 프로그램
// 윈도우 계열 운영체제에서는 보통 서비스 라고 함

// 자바에서도 데몬스레드라고 해서 이와 유사하게 동작하는 스레드를 만들수 있음
// 데몬 스레드를 만드는 방법은 스레드에 데몬을 설정해 주면됨
// 이런 스레드는 자바 프로그램을 만들때 백그라운드에서 특별한 작업을 처리하게 하는 용도로 쓰여짐
// 예를들어서 주기적으로 자동으로 저장하게 하는 기능을 구현한다든지 에디터를 만드는데 일정한 시간마다 맞춤법 검사를
// 하게 한다던지 하는 게 데몬스레드의 용도라고 할 수 있음
// 데몬스레드는 일반스레드가 모두 종료되면 강제적으로 종료되는 특징을 가지고 있음
public class DaemonThread implements Runnable{

    @Override
    public void run() {
        // TODO Auto-generated method stub
        // 계속 무한루프를 돌면서 0.5초씩 쉬면서 데몬쓰레드가 실행중입니다 라는 문자열을 출력하는 데몬스레드 작성
        while (true){
            System.out.println("데몬 스레드가 실행중입니다.");
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
                break;
                // sleep 하는 동안 exception 발생시 while문을 빠져나가기 위해 break
  
            }
        }
    }
    public static void main(String[] args) {
        // 수행하기 위한 main메소드
        // Runnable을 구현하고 있는 데몬스레드 실행시켜주기 위해 Thread를 상속받은 thread를 실행시키는 방법과
        // Runnable인터페이스를 구현하고 있는 스레드를 실행시키는 방법은 조금 달랏었음
        // 인터페이스는 runnable을 구현한 객체는 스스로가 thread가 아니기 때문에 thread를 생성해 주어야함
        Thread thread = new Thread(new DaemonThread()); // Runnable을 구현했던 Thread객체인 DaemonThread를 생성해줌
        thread.setDaemon(true);// 바로 start하는게 아니라 setDaemon이라는 메소드에 true값으로 주면 데몬스레드로 설정이됨
        thread.start();

        // 데몬 스레드의 성질 자체가 모든 스레드들이 종료가 되면 같이 종료된다고 했었음 -> main도 하나의 스레드고
        // main메소드가 종료가 되면 바로 종료 될거니까 main도 조금 쉬었다가 종료될수있도록 sleep사용
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println("메인 스레드가 종료됩니다.");
        // 데몬스레드가 실행되다가 main스레드가 종료되면 같이 종료됨 
    }
    
}
