package Javastudy.javaUtilExam;



import java.util.ArrayList;
import java.util.List;

// list는 데이터의 중복이 있을수 있고, 순서도 있다.
// 배열과 리스트는 비슷함 -> 배열은 한번생성하면 크기 변경 불가
// 리스트는 저장공간이 필요에 따라 자유

public class ListExam {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("kim");
        list.add("kang");
        list.add("kim");
        for (int i = 0; i < list.size(); i ++){
            String str = list.get(i);
            System.out.println(str);
            System.out.println(list);
        }     
        for (String str1 : list){
            System.out.println(str1);
        }   
    }
    
}
