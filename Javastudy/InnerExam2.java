package Javastudy;
//두번째는 내부 클래스가 static으로 정의된 경우, 정적 중첩 클래스 또는 static 클래스라고 한다.
//필드 선언할 때 스태틱한 필드로 선언한 것과 같다. 이 경우에는 InnerExam2객체를 생성할 필요없이 new InnerExam2.Cal() 로 객체를 생성할 수 있다.
public class InnerExam2{
    static class Cal{
        int value = 0;
        public void plus(){
            value++;
        }
    }

    public static void main(String args[]){
        InnerExam2.Cal cal = new InnerExam2.Cal();
        cal.plus();
        System.out.println(cal.value);

    }
}