package Javastudy.javaUtilExam;

public class CompareExam {
    // 컴페어 인터페이스를 받아들여서 해당 인터페이스를 이용
    // 이 인터페이스는 Compare인터페이스에 compareTo라는 메소드가 어떻게 구현 되었는가에 따라 출력값이 달라짐
    public static void exec(Compare compare){
        // Compare 인터페이스를 받아들여서 사용하는 거니까 이런식으로 받아들이도록 정의
        // 이 메소드는 정수값을 2개 갖게 할거고
        int k = 10;
        int m = 20;
        int value = compare.compareTo(k, m);
        System.out.println(value);
        
    }// 이때 정의되는 메소드를 실행하는쪽에서 실제 어떻게 실행되는지 구현부를 작성하면됨
    public static void main(String[] args) {
        exec((i, j)->{ // 괄호안에 매개변수 목록 적어주고
            // 이부분에 구현
            return i - j;
            // 이렇게 되면 매개변수 2개가 들어왔을떄 결과가 수행이 될테고 수행이 될 때 큰수면 i가 크다라고 판단
            // 만약 음수가 나오면 j 가 크다고 판단, 0이나오면 2개값이 같은것으로 판단 가능
            
            // 괄호안에 i, j 두개를 적어 줫고 중괄호 안에서는 i - j를 넣어줌
            // jvm은 exec메소드를 찾아보고 매개변수 2개를 받아들이는 인터페이스를 받아들이고있는 메소드가 무엇인지 찾아봄
            // 그러면 해당 인터페이스가 Compare라는 인터페이스를 받아들이는 exec메소드가 알맞는 메소드인것을 찾게 되고
            // jvm은 이 람다식을 Compare을 구현하는 익명객체로 만들어서 exec에게 전달을 하게됨
            // 이렇게 실행되게 되면 i크면 양수, 작으면 음수, 같으면 0 리턴

            // 사용자가 이 부분을 어떠헥 구현하는지에 따라서 결과값은 달라짐


        });
    }
    
}
