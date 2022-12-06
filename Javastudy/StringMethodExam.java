package Javastudy;

public class StringMethodExam {
    public static void main(String[] args) {
        //String str = new String("hello");
        String str = "hello";
        System.out.println(str.length());
        System.out.println(str.concat(" world"));
        str += " wo";
        System.out.println(str);
        str = str.concat("rld");
        System.out.println(str);

        System.out.println(str.substring(0, str.length()));
        String str1 = "안녕하세요. ";
        String str2 = "벌써 여기까지 오셨네요. 끝까지 화이팅!!";
        
        String concatResult = str1.concat(str2);
        String substringResult = str1.substring(2, str1.length());
        // 아래쪽에 코드를 작성하세요.
        
        
        
        
        // 이 아래는 정답 확인을 위한 코드입니다. 수정하지 마세요.
        System.out.println(concatResult);
        System.out.println(substringResult);
    }
    
}
