package Javastudy;
// String Class의 문제점

public class StringExam2 {
    public static void main(String[] args) {
        // String Class는 불변클래스
        String str1 = "hello world";
        String str2 = str1.substring(5);
        System.out.println(str1);
        System.out.println(str2);
        // str1자체는 변하지 않음

        String str3 = str1 + str2;
        // 문자열과 문자열은 + 로 결합할수 있음

        System.out.println(str3);
        // 이렇게 실행해보면 전혀 문제가 없어 보임
        // 문자열하고 문자열하고 더하면 내부적으로는 StringBuffer라는 클래스를 하나
        // 생성하고 StringBuffer가 가지고있는 append를 이용해서 str1을 하나 붙여주고
        // 또하나 append()를 이용해서 str2를 붙여주고 이걸 toString으로 str4에게 
        // 전달함
        String str4 = new StringBuffer().append(str1).append(str2).toString();
        System.out.println(str4);
        // 문자열과 문자열을 더하는 코드가 실제는 스트링 버퍼라는 객체를 만들고
        // 이 객체가 가지고 있는 append라는 메소드를 이용해서 문자열이 누적되고
        // 그 누적된 문자열을 toString메소드로 다시 String객체로 변환해서 리턴하는것

        // 다시 말해서 문자열을 + 로 붙이게 되면 항상 StringBuffer라는 객체가 생성됨
        // 만약 문자열과 문자열을 반복문안에서 사용하게 된다면 어떻게 될까?

        String str5 = "";
        for (int i = 0; i < 100; i ++){
            str5 = str5 + "*";

        }
        System.out.println(str5);
        // 실제 이 반복문 안에서 문자가 더해질때 마다 100번동안 내부적으로
        // StringBuffer객체를 한번씩 만들어냄
        // 자바 언어는 new 연산자가 많이 사용될수록 프로그램의 속도가 느려짐
        // 이렇게 빈번하게 플러스 연산이 일어난다면 이렇게 사용하는것보다
        // StringBuffer라는 클래스를 적절히 이용
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < 100; i  ++){
            sb.append("*");
        }
        String str6 = sb.toString();
        //이렇게 하는것이 훨씬 효율적인 코드임
        System.out.println(str6);
        // 문자열을 반복문 안에서 사용하는것은 성능상으로 문제가 발생할수있기때문에
        // 반드시 피하는것이 좋음 
        
    }
}
