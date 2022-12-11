package Javastudy.javaUtilExam;
// ThreadB를 사용하며 wait 하는 클래스
public class ThreadA {
    public static void main(String[] args) {
        ThreadB b = new ThreadB();
        b.start();
        // System.out.println("b 실행");
        // 이렇게 스레드가 실행되면 해당 스레드는 run()메소드  안에서 자신의 모니터링락을 획득
        // b에 대하여 동기화 블록을 설정했었었음
        // 만약 메인스레드가 아래의 블록을 위의 스레드보다 먼저 실행하게 되었다면 wait를 하게 되면서
        // 모니터락을 놓게됨
        synchronized (b){
            try {

                System.out.println("b가 완료될때 까지 기다립니다.");
                b.wait();
                // b라는 스레드가 모두 완료 될때까지 기다릴수있도록 wait() 메소드 호출 
                
            } catch (Exception e) {
                //TODO: handle exception
                e.printStackTrace();
            }
        }
        // 이렇게 실행하게되면 synchronized 블록안에서 해당 메인 부분은 기다리게 됨
        // 그래서 b.wait()메소드를 호출하면 메인스레드는 정지함
        // ThreadB가 다섯번 값을 더한후에 notify라는 메소드가 호출하게되면 wait에서 깨어나게 됨
        // 깨어 낫기 떄문에 메인스레드 나머지 부분에서 메인의 일을 할수있게됨
        // 그래서 깨어난 뒤에 모두 더한 값을 출력할 수 있도록 출력문 하나 만들어줌
        System.out.println("Total is : " + b.total);
        // 이 synchronized 블록안에서 b가 완료될때까지 wait라는 메소드를 만났기 때문에 잠들어서
        // 기다리고 있는 상태 -> 이 wait에 빠져있는 상태에서는 반드시 다른 스레드가 notify라는
        // 메소드를 호출해주어야 지만 깨어남 해당 스레드가 동작을 모두 마치고 notify를 호출했을때
        // 그제서야 main스레드는 깨어났을거고 자기의 일을 수행할수 있을것임

        
    }
    
}
