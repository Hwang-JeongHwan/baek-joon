package Javastudy.javaUtilExam;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Month;

/*java.time 패키지
Java에서 제공하는 Date, Time API는 부족한 기능 지원을 포함한 여러가지 문제점을 
가지고 있었다. JDK 코어에서 이런 문제점들을 해결하고
 더 좋고 직관적인 API들을 제공하기 위해 새롭게 재 디자인한 
 Date, Time API를 Java SE 8부터 제공한다.
새로운 API의 핵심 클래스는 오브젝트를 생성하기 위해 다양한 factory 메서드를 사용한다.
오브젝트 자기 자신의 특정 요소를 가지고 오브젝트를 생성할 경우 of 
메서드를 호출하면 되고, 다른 타입으로 변경할 경우에는 from 메서드를 호출하면 된다.
LocalDateTime 클래스를 이용해서 현재 시간 time객체 만드는 방법
now는 현재 시간을 구한다. */
public class TimeExam {
    public static void main(String[] args) {
        LocalDateTime timePoint = LocalDateTime.now();
        System.out.println(timePoint);
        // 지금 현재에 대한 객체가 생성됨
        // 내가 원하는 시간을 가지는 객체도 생성가능
        LocalDate ld1 = LocalDate.of(2012, Month.DECEMBER, 12);
        System.out.println(ld1);

        LocalTime lt1 = LocalTime.of(17, 18);
        System.out.println(lt1);

        LocalTime lt2 = LocalTime.parse("10:15:30");
        System.out.println(lt2);

        LocalDate theDate = timePoint.toLocalDate();
        System.out.println(theDate);
        System.out.println(timePoint.getMonth());
        System.out.println(timePoint.getMonthValue());
        
        Month month = timePoint.getMonth();
        System.out.println(month.getValue());
        // Date나 Calendar와 다르게 +1을 하지않아도 제대로 나옴 
    
    }
}
