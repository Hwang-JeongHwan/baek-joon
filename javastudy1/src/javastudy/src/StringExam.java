package javastudy1.src.javastudy.src;

public class StringExam {
    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "hello";
        // 이런식으로 생성하면 str1에서 hello 라는 문자열이 메모리중에 
        // 상수들이 저장되는곳에 저장됨
        // str2는 hello 라는 문자열을 상수 영역에서 저장하고 있는지 확인
        // 있으면 새로 만들지 않고 str1을 참조 즉 str1과 str2는 같은 인스턴스를 참조
        String str3 = new String("hello"); 
        String str4 = new String("hello");
        // str3과 str4처럼 new연산자를 이용해서 인스턴스를 만들게 되면
        // 새로 인스턴스를 힙 영역에 만들게 됨 
        // str3과 str4는 새로 만듬
        
        if (str1 == str2){
            //참조형일때는 가르키고있는 메모리 영역이 같는지 비교
            System.out.println("str1과 str2는 같은 래퍼런스 입니다.");

        }
        if (str3 == str4){
            System.out.println("str3과 str4는 같은 래퍼런스 입니다.");
        }
        // String은 한번 선언된 클래스는 변하지 않음

        System.out.println(str1);

        System.out.println(str1.substring(3)); // index가 3번인것부터 잘라서 보여달라
        
        //string이 가지고 있는 메소드 들은 새로운 스트링을 만들어서 반환함
        String str5 = "hello world";
        String str6 = str5.substring(3);
        System.out.println(str6);
        if (str1.equals(str5.substring(0, 5))){
            System.out.println("같습니다.");
            // 파이썬에서의 str1[start:end - 1] = 자바 str1.substring(start, end - 1)
        }

        // 문자열을 비교할때는 String객체.equals(비교대상)

        //
    }   
}
