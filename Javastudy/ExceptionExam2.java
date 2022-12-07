package Javastudy;
// throws는 예외가 발생했을때 예외를 호출한 쪽에서 처리하도록 던져준다.
// exception 키워드를 무시하는 throws키워드
public class ExceptionExam2 {
    public static void main(String[] args) {
        int i = 10;
        int j = 0;
        try{
            int k = divide(i, j);
            System.out.println(k);
        }catch(Exception e){
            System.out.println(e.toString());
        }
    }
    public static int divide(int i, int j) throws Exception{
        int k = i / j;
        // 내가 처리하지 않고 나를 호출한쪽에서 처리하도록 해주는 키워드가 throws임

        return k;
    }
}
