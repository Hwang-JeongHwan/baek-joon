package Javastudy;
// Math클래스는 이름 그대로 수학계산을 위한 클래스
// cos sin tan abs random등을 구할수 있음
// Math클래스는 생성자 자체가 private로 되어있기 때문에 new연산자로 객체를 생성할수 없음
// but모든 메소드와 속성이 static으로 정의 되어있기 때문에 객체를 생성하지 않고도 사용할수
// 있음
public class MathExam {
    public static void main(String[] args) {
        int value1 = Math.max(5, 30);
        System.out.println(value1);
        int value2 = Math.min(5, 30);
        System.out.println(value2);
        // 최대 최소를 구하는 메소드

        System.out.println(Math.abs(-10));
        // 절대값 반환

        System.out.println(Math.random());

        // random이라는 메소드는 0이상 1.0미만의 실수값을 더블형으로 구해서 반환
        // 실행할때마다 각각 다른값을 return 

        System.out.println(Math.sqrt(25));
        // 제곱근을 구해주는 메소드, double형으로 반환 
        System.out.println("2의 10승 = " + Math.pow(2, 10));
        System.out.println("16의 1/2승 = : " + Math.pow(16, 0.5));
        System.out.println("log200 = " + Math.log10(200));
    }    
}
