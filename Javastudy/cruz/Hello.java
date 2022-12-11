package Javastudy.cruz;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.TimeZone;

public class Hello {
    public static void main(String[] args) {
        // LocalDateTime date = LocalDateTime.now();
        // //System.out.println(date);
        // System.out.println(date.toLocalDate());
        
        Date date = new Date();
        SimpleDateFormat simple = new SimpleDateFormat("yyyy-MM-dd");
        simple.setTimeZone(TimeZone.getTimeZone("Asia.Seoul"));
        
        System.out.println(simple.format(date));
    }
}
