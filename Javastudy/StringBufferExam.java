package Javastudy;
// String클래스와 비슷한 클래스인 StringBuffer클래스
// String 클래스는 자기 자신이 변하지 않는 불변클래스
// StringBuffer 클래스는 자기자신이 변하는 클래스임
public class StringBufferExam {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("world");
        // StringBuffer가 가진 toString이라는 메소드를 보면 return type이 String인걸
        // 알수있음
        // String str = new String();
        // str += "hello";
        // System.out.println(sb);
        // System.out.println(str);
        String str = sb.toString();
        System.out.println(str);
        // StringBuffer가 가지고 있는 메소드들은 대부분 자기 자신을 반환함

        StringBuffer sb2 = new StringBuffer();
        StringBuffer sb3 = sb2.append("hello");
        if (sb2 == sb3){
            System.out.println("sb2 == sb3");
            // sb2가 가지고 있는 append메소드를 통해 hello를 추가 했고
            // 이때 append메소드는 자기자신 this가 반환됨
            // 이 반환된것을 sb3로 받음 -> 그러므로 두개가 같음
            // 자기 자신을 return하는 것을 이용해서 자기 자신의 메소드를 호출하면서
            // 자기 자신의 값을 바꿔나가는것을 메소드 체이닝 이라고함


        }
        System.out.println(sb2);
        System.out.println(sb3);
        // 둘이 같음
        // 메소드 체이닝(Method Chaining)이란 자기 자신을 리턴하여 계속해서 자신의
        // 메소드를 호출하는 방식 
        // StringBuffer클래스는 메소드 체이닝방식을 사용할수 있도록 만들어져있음
        // 자바에서 이런방법들을 자주 사용되니까 잘 알아 두어야함

        String str2 = new StringBuffer().append("hello").append(" ").append("world").toString();
        System.out.println(str2);
        // str2에 각각 붙여준 문자열이 잘 출력됨
        // 맨처음에 여러줄에 걸쳐서 작성했던 코드를 한줄로 만들수 있음

        // StringBuffer는 append메소드 이외에도 길이를 구한다거나 자른다거나 하는
        // 다양한 메소드들을 가지고 있음
        // 스트링버퍼를 잘이용하면 스트링클래스가 가진 단점을 잘 보안할수 있음 
    }
    
}
