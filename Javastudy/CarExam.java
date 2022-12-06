package Javastudy;

import java.util.Scanner;

public class CarExam {
    public static void main (String [] args){
        Car c1 = new Car();
        Car c2 = new Car();
        // new 라는 연산자는 new연산자 뒤에나오는 생성자  -> 생성자를 이용해서
        // 메모리에 객체를 만듦
        // 메모리에 만들어진 객체를 instance라고 함  
        
        c1.name = "소방차";
        c1.number = 1234;
        String num = "1";
        int name = 1234;
        c2.name = Integer.toString(name);
        c2.number = Integer.parseInt(num);
        Scanner sc = new Scanner(System.in);
        System.out.println(c1.name);
        System.out.printf("%s %d \n",c2.name, c2.number);
        if (!c1.name.equals(c2)){
            System.out.printf("%s %s \n",c1.name, c2.name);
        }
        생성자 c3 = new 생성자("경찰차");
        System.out.println(c3.name);
        생성자 c4 = new 생성자("구급차");
        c3.number = 1234;
        생성자 c5 = new 생성자("경찰차123", 123);
        System.out.printf("%s %d\n",c5.name, c5.number);
        생성자 c6 = new 생성자();
        System.out.printf("%s %d",c6.name, c6.number);
    }
}
