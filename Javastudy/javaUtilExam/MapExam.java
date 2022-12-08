package Javastudy.javaUtilExam;
import java.util.*;
// Map은 key와 value를 쌍으로 저장하는 자료구조, 키는 중복될수 없고 값은 중복될수 있다.

public class MapExam {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("001","kim");
        map.put("002","lee");
        map.put("003","choi");
        
        map.put("001","kang");
        
        System.out.println(map.size());
        System.out.println(map.get("001"));
        // Map은 같은키로 값이 새로 들어오면 기존의 값대신 새로운 값으로 저장
        System.out.println(map);
        // Map의 모든 키값을 뽑는법
        Set<String> keys = map.keySet(); 
        Iterator<String> iter = keys.iterator();
        while (iter.hasNext()){
            String key = iter.next();
            String value = map.get(key);
            System.out.println(key + ":" + value);
        }

    }
    
}
