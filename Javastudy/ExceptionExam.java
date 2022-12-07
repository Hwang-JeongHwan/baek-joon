package Javastudy;

import javax.swing.event.SwingPropertyChangeSupport;

public class ExceptionExam {
    public static void main(String[] args) {
        int i = 10;
        int j = 0;
        // 자바는 정수를 0으로나눌때 예외 발생
        // 프로그램실행중 예기치 못한 사건을 예외라고 한다. 예외상황을 미리 예측하고 처리할 수
        // 있는데 이렇게 하는것을 예외 처리 라고 한다. 
        try{ //예외가 발생할것 같은 부분을 try라는 블록으로 감싸줌
            int k = i / j;
            System.out.println(k);
        }catch(ArithmeticException e) 
        //예외 클래스 변수명, 예외가 발생했을때 실행할수있는 코드를 넣어줄수있음
            { System.out.println("0으로 나눌수 없습니다." + e.toString());
            //e.toString() -> 예외정보를 String으로 나타내줌 
        // 예외 클래스에 Exception 객체를 상속받게 되면 어떤 오류를 발생하든지간에
        // 하나의 catch블록에서 모든 오류를 처리할수 있음 
        /*실행결과
0으로 나눌 수 없습니다. : java.lang.ArithmeticException: / by zero

오류가 발생하든 안하든 무조건 실행되는 블록입니다.

Exception 처리하지 않았을때는 프로그램이 강제 종료되었는데
 catch라는 블록으로 Exception을 처리하니 강제종료되지 않고 잘 실행되는 것을 알 수 있다.

try블록에서 여러종류의 Exception이 발생한다면 catch라는 블록을 여러개 둘 수 있다.

Exception클래스들은 모두 Exception클래스를 상속받으므로,
 예외클래스에 Exception을 두게 되면 어떤 오류가 발생하든지 간에 하나의 catch블록에서 모든 오류를 처리할 수 있다. */
        }
        finally{ // 예외를 발생하든 아니든 무조건 실행
            System.out.println("오류가 발생했든 발생하지 않았든 무조건 실행!");
        }
        // 원래 수행할 코드는 try라는 블록이 가지고 있음
        // 그런데 try라는 블록에서 예외가 발생하면 발생한 지점부터 try블록 마지막 까지는 실행할
        // 수 없음
        // catch 블록으로 넘어오는데 그때 발생한 예외와 catch블록에 내가 선언해 놓은
        // 예외가 맞아야 해당 catch블록을 실행함

        // 그렇게 되기 때문에 예외가 발생하지 않았다거나 혹시 예외가 발생되면 try블록에 있는
        // 부분이나 catch부분은 반드시 실행할거라고 예측할수 없음 -> 실행되지 않을수도있음
        // but finally블록은 반드시 실행함 
        System.out.println("main end!!");
    }
        
    
}
