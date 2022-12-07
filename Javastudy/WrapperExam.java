package Javastudy;
/*java.lang패키지의 클래스는 import를 하지 않고도 사용할 수 있다.
java.lang패키지에는 기본형타입을 객체로 변환시킬때 사용하는 Wrapper클래스가 있다.
Boolean, Byte, Short, Integer, Long, Float, Double 클래스

모든 클래스의 최상위 클래스인 Object도 java.lang패키지
문자열과 관련된 String, StringBuffer, StringBuilder도 모두 java.lang패키지
화면에 값을 출력할때 사용했던 System클래스도 java.lang패키지
수학과 관련된 Math클래스도 java.lang패키지
Thread와 관련된 중요 클래스들이 java.lang패키지
이외에도 다양한 클래스와 인터페이스가 java.lang패키지에 속해 있다. */
public class WrapperExam {
    public static void main(String[] args) {
        int i = 5;
        Integer i2 = new Integer(5);
        // int i 는 기본형 타입 Integer i2는 실제 인트를 객체로 바꿔주는 래퍼
        // 클래스중의 하나인 인티저라는 클래스임
        // i는 기본형 타입이기 때문에 객체가 아님 -> 참조형이 아니라는 의미임
        // 만약 숫자 5를 참조형처럼 사용하고 싶다면 i2처럼 선언해야지 사용할수 있음
        Integer i3 = 5;
        // 그냥 데이터 타입 5를 넣었는데 전형 문제 없이 작동하는 것을 볼수 있음
        // 숫자 5는 원래 기본형이지만 자동으로 인티저 형으로 변환된것을 볼수 있음
        // 이것을 오토 박싱이라고함 
        // 실제 기본형 데이터 타입을 객체형으로 바꿀때는 new Integer라는 이 타입,
        // 각각의 알맞는 래퍼 wrapper class들을 이용해서 감싸줫어야했는데
        // 자바5버전  이후로 i3처럼 사용할수 있고 이런 기능들을 오토박싱이라고함
        // Integer i3 = new Integer(5)라고 자동으로 변환해 주기 때문에 오토박싱이라고함
        int i4 = i3.intValue();
        // 이러한 메소드를 사용해서 객체로 감싸져있는것을 벗겨내고 인트 타입으로 사용할수
        // 있었는데 자바5 이후부터는 이런식으로
        int i5 = i3; //intValue를 호출하지않고 바로 사용할수 있음
        // 이런걸 오토언박싱이라고 함
        // 이부분도 마찬가지로 내부적으로 컴파일러가 자동으로 해당 매소드를 호출해서
        // 한번 벗겨내서 사용하는거다 라고 기억하면됨
        // 그전에는 사용자가 직접 객체타입으로 바꿔주는 부분을 알아서컴파일러가 변경해주는것을
        // 오토박싱 오토 언박싱이라고 함 
        Integer i1 = 5;
        int max_int = i1.MAX_VALUE;
        long i1_long = i1.longValue();
        System.out.println(i1_long);

    }
    
}
