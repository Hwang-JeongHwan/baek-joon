package Javastudy;

import Javastudy.cruz.AccessObj;

public class AccessObjExam extends AccessObj {
    public static void main(String[] args) {
        AccessObjExam obj = new AccessObjExam();
        System.out.println(obj.p); // public
        System.out.println(obj.p2); // protected
       // System.out.println(obj.k); // defalut 
       // System.out.println(obj.i); // i는 private라 접근 불가
        // 다른 패키지로 이동시
        // public을 제외한 모든 접근제한자에서 오류를 발생
        // 만약 AccessObj Exam이 AccessObj를 상속하고 있다면
        // protected까지 사용가능 => 자식 클래스이기 때문에 
        // 접근제한자는 필드뿐 아니라 메소드와 클래스 앞에도 붙여서 사용가능
        // 접근제한자에 따라서 해당 클래스나 해당필드, 메소드에 어디까지 접근해서 사용
        // 할건지 정의활수 있는 부분임
    }   
}
