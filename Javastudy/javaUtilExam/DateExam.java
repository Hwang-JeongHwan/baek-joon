package Javastudy.javaUtilExam;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateExam {
    public static void main(String[] args) {
        Date date = new Date();
        // date객체를 기본생성자로 생성
        // 현재 시간과 날짜 정보를 date인스턴스가 가지게 됨
        System.out.println(date.toString());
        // 출력되는 부분이 내가 원하는 형식은 아님
        // 원하는 형식으로 출력을 받아보고 싶다 할때는
        // 유틸패키지가 샘플 데이트 포맷이라는 클래스를 제공함

        SimpleDateFormat ft = new SimpleDateFormat("yyyy.MM.dd 'at' hh:mm:ss a zzz");
        System.out.println(ft.format(date));

        // 생성자의 매개변수에 표현하고 싶은 형태의 값을 넣어주면됨
        //"yyyy" = 연도를 4자리로 .MM 월 대문자로 표시, 며칠dd 
        // ' '로 감싸면 문자그대로  츨력 hh 시간 mm 분 ss초
        // a : 오전 오후 표시 
        // zzz : 타임존을 나타냄 -> 한국같은 경우 한국 표준시 kst가 표시가 됨

        //ft.format에 아까 만든 date객체를 넣어주면 내가 원하는대로 나옴
        System.out.println(date.getTime());
        // 현재 시간을 long값으로 구하는 방법

        long today = System.currentTimeMillis();
        System.out.println(today);
        //System의 현재 시간을 long값으로 구해서 나한테 주세요 라는 의미
        System.out.println(today - date.getTime());
        // 이렇게 하면 현재 date라는 객체를 만들고 today라는 객체를 만든시간까지의
        // 차이
    }
    
}
