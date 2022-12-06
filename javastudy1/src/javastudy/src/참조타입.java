package javastudy1.src.javastudy.src;

/* 자바의 변수 타입은 기본형 타입과 참조형 타입이 있음 
 * 기본형 타입은 boolean char 문자형 정수형 byte short, int, long
 * 실수형 float, double 이 있음
 * 기본형 타입은 클래스가 아님
 * 
 * 자바에서의 참조형 타입은 기본형 타입을 제외한 모든 타입
 * 
 */
public class 참조타입 {
    public static void main(String[] args) {
        int i = 4;
        // 기본형 타입, 4바이트 크기의 정수 타입 변수에 숫자 4를 저장한다를 의미

        String str = new String("hello");
        // new라는 키워드는 클래스를 메모리에 올려주세요 라는 뜻임
        // 이렇게 메모리에 올라간 클래스를 인스턴스 라고 얘기함
        // 메모리에 올라간 인스턴스를 가르키는 변수, 참조하는 변수, reference하는 변수
        // 가 str임 -> 참조한다는것은 변수가 인스턴스를 가지고 있는것이 아니라 말그대로
        // 가리킨다 라는 말임
        // str - > hello 라는 String객체를 참조한다
        // 앞으로 배울 클래스들은 모두 참조형임

    }

}
