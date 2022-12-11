package Javastudy.javaUtilExam;
// thread제어문중 wait와 notify메소드
// wait와 notify메소드는 동기화된 블럭 안에서 사용해야함

// wait()를 만나게 되면 해당 스레드는 해당 객체의 모니터링락에 대한 권한을 가지고
// 있었다면 모니터링락의 권한을 놓고 대기하게 됨

public class ThreadB extends Thread {
    int total;
    @Override
    public void run() {
        // TODO Auto-generated method stub
        //super.run();
        synchronized(this){ // 해당 부분은 동기화 되고 있어야 된다고 했기 때문에 synchronized블록으로 감싸줌
        // 해당 스레드가 실행되면 자기 자신의 모니터링 락을 획득하게 됨
            for (int i = 0; i < 5; i++){
                System.out.println(i + "을 더합니다");
                total += i;

                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }


            }
            notify();
            // 이 일이 모두 끝나면 그만 스레드를 깨울수있는 notify()라는 메소드를 호출하게
            // 수행하도록 해봄


        }
    }
    
}
