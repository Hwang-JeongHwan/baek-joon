package Javastudy.javaUtilExam;

import java.lang.reflect.Method;

public class MyhelloExam {
    public static void main(String[] args) {
        Myhello hello = new Myhello();

        // 메소드에 대한 정보를 얻어낼수있는 코드 작성
        try {

            Method method = hello.getClass().getDeclaredMethod("hello");
        // getClass라는 메소드는 오브젝트가 가지고 있는 메소드고 모든 클래스들은
        // Object를 상속받으니까 사용 가능 , 이 클래스 getClass라는 메소드는
        // 해당 인스턴스를 만들때 사용한 클래스의 정보를 return
        // 클래스의 정보를 받아서 getDeclaredMethod라는 메소드를 호출하게 되면
        // 그 클래스의 정보를 얻고 그 정보로 부터 hello라는 메소드의 정보를 구하라는것
        // 예외처리를 해야하므로 try catch로 묶음
            if (method.isAnnotationPresent(Count100.class)){
                // 메소드가 가지고 있는 isAnnotationPresent가 특정 어노테이션이
                // 메소드에 적용되어있는지 알아내는 부분
                // 얻어낸 메소드가 Count100이라는 어노테이션을 적용하는가?
                // 적용되어있으면 true 반환
                for (int i = 0; i < 100; i ++){
                    hello.hello();
                }
            }
            else{
                hello.hello();
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
         //직접 어노테이션을 만들어서 사용하는 경우는 많이 없고
         // 자바를 훨씬 잘 쓸수 있을때쯤 사용하게 될거라고함..
    }
}
