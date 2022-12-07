package Javastudy;

public class BizService {
    public void bizMethod(int i) throws BizException{
        System.out.println("비지니스 메소드 시작");

        if(i < 0){ 
            throw new BizException("매개변수 i는 0보다 작습니다.");
        }
        System.out.println("비지니스 메소드 종료");
    }
}
