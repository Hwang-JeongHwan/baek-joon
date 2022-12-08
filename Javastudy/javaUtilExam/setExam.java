package Javastudy.javaUtilExam;
import java.util.*;
public class setExam {
    public static void main(String[] args) {
    // set은 중복이 없고 순서도 없는 자료구조
    // HashSet과 TreeSet이 있다
        // 타입은 인스턴스 타입, lang패키지가 아니라서 반드시 import해야함
        Set<String> set1 = new HashSet<>();
        // Set은 인터페이스 이기 때문에 new로 객체를 생성할수 없음
        // Set을 구현한 클래스인 HashSet을 이용해서 인스턴스를 생성.
        boolean flag1 = set1.add("kang");
        boolean flag2 = set1.add("kim");
        boolean flag3 = set1.add("kang");
        System.out.println(set1.size());
        
        System.out.println(set1);
        System.out.println(flag1);
        System.out.println(flag2);
        System.out.println(flag3);
        // 같은 값이 또들어가면 false리턴하는것을 확인할수 있음

        
        // add는 저장할때마다 boolean값을 return함
        // 이미 같은 값이 존재하는 경우 false반환
        // Set자료구조에서 들어있는 값들을 하나씩 하나씩 꺼내보기 위해서는
        // Set의 부모클래스인 컬렉션이 가지고 있는 이터레이터라는 인터페이스를 이용해야함
        Iterator<String> iter = set1.iterator();

        // 이터레이터는 hasnext라는 메소드를 가지고 있는데 지금 현재 set자료구조에 
        // 데이터가 있으면 true 없으면 false를 리턴해주는 메소드
        // 값을 꺼낼때 인덱스가 필요하지 않기 때문에 for가 아닌 while문 사용
        while (iter.hasNext()){
            String str = iter.next();// 값을 꺼내는 메소드
            //next메소드는 하나를꺼내고 꺼내고 나면 자동으로 다음것을 참조하게됨
            System.out.println(str);
        }
        for (String str1 : set1){
            System.out.println(str1);
        }
    }

}
