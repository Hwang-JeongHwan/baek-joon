package Javastudy.javaUtilExam;

import java.util.Calendar;
import java.text.SimpleDateFormat;
//Date의 단점을 해결하고 등장한것이 Calendar클래스
public class CalendarExam {
    public static void main(String[] args) {
        // Date가 지역화에 대한 고려가 되어있지 않아 그부분을 고려하여 만든 클래스
        Calendar cal = Calendar.getInstance();
        // Calendar는 추상클래스이기 때문에 Calendar.getInstance라는 메소드를 사용해서
        // 인스턴스를 만들어서 리턴
        // 상속에서 Calendar가 return된다는것은 Calendar뿐만 아니라 Calendar의 자식 
        // 클래스 들이 return될수도 있다는 의미
        // getInstance라는 메소드가 호출되면 캘린더의 자식클래스인 Gregorian Calendar
        // 라는 클래스가 존재함 -> 이 클래스의 인스턴스를 만들어서 return함
        // 애초에 캘린더를 만들때 new GregorianCalendar라고 할수도있었겠지만
        // 자바에서는 calendar의 생성과정을 숨김 
        // 이렇게 하는 이유는 나중에 미래의 새로운 형식의 달력이 표준이 될수도 있을거다
        // 라는 것을 고려 -> 이런경우 다른 클래스가 표준이 될수도 있기 때문에
        // 이렇게 되었을때 버전업만해주면 다른 달력의 클래스가 return될수있기때문에
        System.out.println(cal.get(Calendar.YEAR));
        // cal.get(상수) // 상수를 사용할때는 클래스명. 하고 사용
        System.out.println(cal.get(Calendar.MONTH) + 1);
        // 자바는 월을 표현할때 0월부터 11월까지 표현하기 때문에 뒤에 1을 더해줘야함

        System.out.println(cal.get(Calendar.DATE));
        System.out.println(cal.get(Calendar.HOUR)); // 12시간으로 표현
        System.out.println(cal.get(Calendar.HOUR_OF_DAY)); // 24시간으로 표현

        System.out.println(cal.get(Calendar.MINUTE));
        System.out.println(cal.get(Calendar.SECOND));

        cal.add(Calendar.DATE, 100);
        // 음수 사용하면 전, 양수 사용시 후
        System.out.println(cal.get(Calendar.YEAR));
        // cal.get(상수) // 상수를 사용할때는 클래스명. 하고 사용
        System.out.println(cal.get(Calendar.MONTH) + 1);
        // 자바는 월을 표현할때 0월부터 11월까지 표현하기 때문에 뒤에 1을 더해줘야함

        System.out.println(cal.get(Calendar.DATE));
        System.out.println(cal.get(Calendar.HOUR)); // 12시간으로 표현
        System.out.println(cal.get(Calendar.HOUR_OF_DAY)); // 24시간으로 표현

        System.out.println(cal.get(Calendar.MINUTE));
        System.out.println(cal.get(Calendar.SECOND));

        System.out.println(cal);
        
        String str = cal.toString();
        System.out.println(str);
        int year = cal.get(Calendar.YEAR);
        int month = cal.get(Calendar.MONTH);
        int date = cal.get(Calendar.DATE);

        String answer = Integer.toString(year) + "년" + Integer.toString(month) + "월" + Integer.toString(date) + "일";
        System.out.println(answer);
        SimpleDateFormat f = new SimpleDateFormat("yyyy'년'M'월'dd'일'");
        System.out.println(f.format(cal.getTime()));        

    }
}
