package Javastudy.javaUtilExam;
// 자바8에서 새롭게 추가된 문법인 람다식
// 인터페이스 중에서 메소드를 하나만 가지고 있는 인터페이스를
// 함수형 인터페이스라고 함
// Runnable과 같은 인터페이스
// Runnable은 run이라는 인터페이스 하나만 가지고 있음
public class LambdaExam {
    public static void main(String[] args) {
        
        new Thread(new Runnable() {
            // 이렇게 Runnable 인터페이스를 생성할수 있음
            @Override
            public void run() {
                // TODO Auto-generated method stub
                // run메소드 직접구현
                for (int i = 0; i < 10; i ++){
                    System.out.println("hello");
                }
                
            }
            
        }).start(); // 요 자체가 스레드가 생성된 구문이니까 스레드가 생성되었을때 스레드가 가지고 있는 start라는 메소드를 시작시키면
        // 스레드가 동작해서 hello가 10번 출력됨 
        // 스레드가 실행될때 스레드 생성자 안에 넣은 run이라는 메소드가 실행이 되도록 해라 라고 할수있음
        // 자바는 메소드만 매개변수로 전달할 방법이 없음 , 인스턴스만 전달할수있음
        // 그래서 여기에서는 run이라는 메소드를 메소드를 가지고 있는 runnable을 객체로 만들어서 전달함
        // 메소드만 전달할수있는 방법이 없기 때문에 매번 객체를 생성해서 매개변수로 전달해야만함
        // 이런부분을 개선하려고 만듯것이 람다표현식임

        // 람다표현식에서는 객체 장체를 직정 생성할 필요가 없음 -> new Runnable()을 빼고 람다 표현식의 문법인 ()-> 이렇게 해서 만들어줌

        new Thread(()->{
            // 이부분에서는 메소드 자체를 정의할 필요없고 실제 구현할 부분만 남겨두면 됨
            for (int i = 0; i < 10; i++){
                System.out.println("hello");
            }
            // 이렇게 구현하면 람다표현식으로 표현식으로 바꾼것
            // 괄호열고 

        }).start();
        // ()->{}까지를 람다식이라고 함, 람다식은 다른말로 익명메소드라고 얘기함
        // jvm은 스레드의 생성자를보고 해당 람다식을 보면서 이게무엇인지 대상을 추론하게 됨
        // 스레드 생성자 api를 보면 Runnable인터페이스를 받아들이는것을 알수 있음
        // jvm은 쓰레드 생성자가 runnable인터페이스를 구현한 것이 와야하는것을 알게 되고 람다식을 Runnable을 구현하는 객체로
        // 자동으로 만들어서 매개변수를 넣어주게 됨 
        /* 
        ()->{ ..... } 부분이 람다식, 다른말로 익명 메소드

        JVM은 Thread생성자를 보고 ()->{} 이 무엇인지 대상을 추론한다.

    Thread생성자 api를 보면 Runnable인터페이스를 받아들이는 것을 알 수 있다.

    JVM은 Thread생성자가 Runnable인터페이스를 구현한 것이 와야 하는 것을 알게 되고 
    람다식을 Runnable을 구현하는 객체로 자동으로 만들어서 매개변수로 넣어준다.


*/
    }
}
