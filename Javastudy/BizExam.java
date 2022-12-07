package Javastudy;

public class BizExam {
    public static void main(String[] args) {
        BizService biz = new BizService();
        biz.bizMethod(5);
        try{
        biz.bizMethod(-1);
        }catch(Exception e){
            e.printStackTrace();
        }
        // 이런 부분들에 있어서 익셉션이 발생했을때 처리를 하고 싶다면 트라이 캐치
        // 같은 블록으로 묶어서 처리해도 되고
        // 런타임 익셉션을 상속받고 있는 메소드를 throw하고 있기 때문에 컴파일상에
        // 반드시 익셉션 처리를 하라고 에러를 발생하지 않음
        
        
    }
    
}
