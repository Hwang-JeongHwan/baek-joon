package Javastudy.javaUtilExam;
/* 쓰레드와 공유객체 
 * 하나의 객체를 여러개의 Thread가 사용한다는 것을 의미
 * 
 * 놀이터에 그네가 하나있고 놀이터에 뛰어노는 아이가 3명 -> 어린이들을 쓰레드라고 생각
 * 하면 그네는 공유객체라고 말할수있음, 하나의 객체를 여래개의 쓰레드가 사용한다는것
 * 을 의미함
 * 
 * 다른 말로는 하나의 객체를 여러개의 쓰레드가 함께 가지고 있다고도 말할 수 있음
 */

// MusicBox : 공유객체
// 세개의 메소드가 동시에 호출이되면 뮤직박스 내부가 고장이 난다면
// 어떻게 해야할까

// 한가지 메소드가 사용될때 다른 메소드는 사용되지 못하도록 대기 하도록하고
// 끝나고 나면 실행, 다른 메소드들은 대기
/* 동기화 메소드와 동기화 블록
 * 공유객체가 가진 메소드를 동시에 호출 되지 않도록 하는 방법
 * 메소드 앞에 synchronized 를 붙힌다.
 * 여러개의 Thread들이 공유객체의 메소드를 사용할 때 메소드에 
 * synchronized가 붙어 있을 경우 먼저 호출한 메소드가 
 *  객체의 사용권(Monitoring Lock)을 얻는다.
 * 
 */
public class MusicBox {
    // 세게의 메소드를 가지고 있다고 가정
    /* 메소드 앞에 synchronized 를 붙혀서 실행해 보면, 
     * 메소드 하나가 모두 실행된 후에 다음 메소드가 실행된다.
     * 해당 모니터링 락은 메소드 실행이 종료되거나, wait()와 같은 
     * 메소드를 만나기 전까지 유지된다.
     
     * 다른 쓰레드들은 모니터링 락을 놓을때까지 대기한다.
     * synchronized를 붙히지 않은 메소드는 다른 쓰레드들이 
     * synchronized메소드를 실행하면서 모니터링 락을 획득했다 하더라도, 
     * 그것과 상관없이 실행된다.
     * synchronized를 메소드에 붙혀서 사용 할 경우, 
     * 메소드의 코드가 길어지면, 마지막에 대기하는 쓰레드가 
     * 너무 오래 기다리는것을 막기위해서 메소드에 synchronized를 붙이지 않고, 
     * 마지막에 메소드를 호출하는 쓰레드는 가장 오랫동안 기다려 줘야함
     * 문제가 있을것 같은 부분만 synchronized블록을 사용한다. 
     * 
     * 
     * 다른 쓰레드 들이 모니터링 락을 획득했다 하더라도 synchronized가 안붙은 메소드는
     * 그것과 상관없이 막 실행이됨 
     * 
     * */
    

    public synchronized void playMusicA(){
        for(int i = 0; i < 10; i++){
            System.out.println("신나는 음악!!!");
            try {

                Thread.sleep((int)(Math.random() * 1000));
                
            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }

    }
    public synchronized void playMusicB(){
        for(int i = 0; i < 10; i++){
            System.out.println("슬픈 음악!!!");
            try {
                
                Thread.sleep((int)(Math.random() * 1000));
                
            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }

    }
    public void playMusicC(){
        for(int i = 0; i < 10; i++){
            // 메소드 내에 중복되면 안되는 부분이 있으면 메소드 자체에
            // synchronize를 붙이는게 아니라 
            // 중복되면 안되는 부분에만 synchronized블록을 부텽줌
            synchronized(this){
                System.out.println("카페 음악!!!");
                // 자기 객체 자신을 의미하는 this로 매개변수를 넣어주면
                // 이 블록 부분만 synchronized로 동작 (동기)
                // synchronized this라는 부분을 생각해보면 현재 객체가 
                // 모니터락을 가질수 있을경우에 모니터링락을 가지게 해서
                // 동기화 하겠다는 얘기임
                // playMusicA 메소드가 종료될때 모니터링락을 놓게 되는데
                // synchronized 블록에서 대기하던 쓰레드는 이때 실행됨

                // 딱 한줄만 블록으로 감싸져있으니까 그때만 모니터링락을 가지고
                // 실행하게 되니 그 이외의 다른 쓰레드들이 조금더 빠르게 진입
                // 할수 있게됨 
            }try {
                
                Thread.sleep((int)(Math.random() * 1000));
                
            } catch (Exception e) {
                // TODO: handle exception
                e.printStackTrace();
            }
        }

    }
}
