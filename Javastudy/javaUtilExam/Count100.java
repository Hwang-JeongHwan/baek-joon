package Javastudy.javaUtilExam;
/* * 어노테이션
   * 클래스나 메소드 위에 붙어있음 @표시 at이라고 읽음
   * 소스코드에 메타 코드(추가정보)를 붙이는것
   * 메타 코드란 소스코드에 추가적인 내용을 붙이는것을 의미
   * 어노테이션을 클래스나 메타코드에 붙인 후에 클래스가 컴파일되거나 실행 되었을때
   * 어노테이션의 유무나 어노테이션에 설정된 값을 통해서 클래스가 좀더 다르게
   * 실행되게 할 수 있음
   * 이런 이유로 어노테이션을 일정의 설정파일처럼 설명하고 있는 경우도 많이 있음
   * 어노테이션은 자바가 기본적으로 제공해주는것도 있고 사용자가 직접 작성할수도있음
   * 사용자가 직접 작성하는 어노테이션을 커스텀 어노테이션이라고함
   * 
   * 1/어노테이션을 정의하고 2.어노테이션을 클래스에서 사용 -> 3.
   * 어노테이션을 이용해서 실행
   

*/ 
// 인터페이스와의 차이점은 인터페이스 키워드 앞에 @가 붙어있는것을 볼수있음
// jvm실행시 감지할수 있게 하려면 @Retention(RetentionPolicy.RUNTIME)을 달아줘야함

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface Count100 {
    
}
