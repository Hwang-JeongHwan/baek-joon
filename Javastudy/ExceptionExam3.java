package Javastudy;
// 강제로 오류를 발생시키는 throw
// throw는 오류를 떠넘기는 throws와 보통 같이 사용됩니다.
public class ExceptionExam3 {
    public static void main(String[] args) {
        int i = 10;
        int j = 0;
        try{
        int k = divide(i, j);
        System.out.println(k);
        }catch(IllegalArgumentException e){
            System.out.println(e.toString());
        }
    }
    public static int divide(int i, int j)throws IllegalArgumentException{
        if (j == 0){
            // System.out.println("2번째 매개변수는 0이면 안됩니다.");
            // return 0;
            // 0으로 나눈 결과가 0은 아님 -> 어쨋든 return을 0으로 해서 k값이 0이됨
            // 올바르지 않은 결과가 프로그램 내에서 사용될수있음 
            // 오류를 직접 발생시키는 코드
            throw new IllegalArgumentException("0으로 나눌수 없습니다.");
            // 해당 라인에서 exception이 발생한다는 뜻
            // 매개변수가 잘못되어 만들어진 오류다 라는뜻을 가진 객체를 생성
        }
        int k = i / j;
        return k;
        // divide 메소드는 두번째 파라미터가 0인경우 Exception발생
        // 두번째 매개변수가 0으로 전달되는것 자체가 잘못된것 -> 나누기를 하기전에
        // 뭔가 체크를 하고싶다면
    }
}
