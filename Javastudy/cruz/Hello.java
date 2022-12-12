package Javastudy.cruz;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.TimeZone;

public class Hello {
    public static void main(String[] args) {
        // LocalDateTime date = LocalDateTime.now();
        // //System.out.println(date);
        // System.out.println(date.toLocalDate());
        
        // Date date = new Date();
        // SimpleDateFormat simple = new SimpleDateFormat("yyyy-MM-dd");
        // simple.setTimeZone(TimeZone.getTimeZone("Asia.Seoul"));
        
        // System.out.println(simple.format(date));
        ArrayList al = new ArrayList();
        al.add("one");
        al.add("two");
        al.add("three");
        for (int i = 0; i < al.size(); i ++){
            String val = (String)al.get(i);
            System.out.println(val);
        }
        ArrayList<String> al2 = new ArrayList<String>();
        al2.add("one");
        al2.add("two");
        al2.add("three");
        for (String str : al2){
            System.out.println(str);
        }
        for (int i = 0; i < al2.size(); i ++){
            String val = al2.get(i);
            System.out.println(val);
        }
    }
}
