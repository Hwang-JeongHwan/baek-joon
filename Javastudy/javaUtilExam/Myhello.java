package Javastudy.javaUtilExam;

public class Myhello {


    // Myhello는 hello라고 출력해주는 메소드를 하나 가지고 있음
    // 지정한 annotation Count100을 사용하려하면  hello라는 메소드에다가
    // 어노테이션 이름을 붙여주면됨
    @Count100
    public void hello(){
        System.out.println("hello");
    }
}
