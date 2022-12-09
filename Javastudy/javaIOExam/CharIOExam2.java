package Javastudy.javaIOExam;
import java.io.*;
/*
 * char단위 입출력 클래스는 클래스 이름이 Reader나 Writer로 끝이 납니다.
 * 파일에서 한 줄씩 입력 받아서 파일에 출력
 * 파일에서 읽기위해서 FileReader 클래스 이용
 * 한 줄 읽어 들이기 위해서 BufferedReader 클래스 이용
 * BufferedReader 클래스가 가지고 있는 readLine() 
 * 메소드가 한줄씩 읽게 해준다.
 * readLine()메소드는 읽어낼 때 더 이상 읽어 들일 내용이 없을 때 
 * null을 리턴한다.
 * 파일에 쓰게하기 위해서 FileWriter 클래스 이용
 * 편리하게 출력하기 위해서 PrintWriter 클래스 이용

 */
public class CharIOExam2 {
    public static void main(String[] args) {
        // 파일에서 읽어들이기 위해서는 FileReader가 필요하고
        // 한줄씩 읽어들이기 위해서는 BufferedReader가 필요함
        BufferedReader br = null;
        PrintWriter pw = null;

        try {
            br = new BufferedReader(new FileReader("Javastudy/javaIOExam/CharIOExam.java"));
            // 익셉션 처리할때 try catch사용
            // 트라이 블록 안에 선언된 부분이 들어가면 외부에서 사용불가,
            // 선언과 익셉션 처리 부분을 분리해 주는게 좋음
            pw = new PrintWriter(new FileWriter("Javastudy/javaIOExam/test.txt"));
            String line = null;

            while((line = br.readLine()) != null){
                //null 이 return되면 파일의 끝
                pw.println(line);
                // 이러면 아무것도 안나옴 
                // 파일에 뭔가썻는데 파일을 닫아주지 않아서 그럼
                // 항상IO는 열었으면 닫아야함
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }finally{
            pw.close();
            try{
                br.close();
            }catch(Exception e){
                e.printStackTrace();
            }
            // IO는 어디서 읽을거냐 어디에 쓸거냐
            // 어떤방법으로 읽을거냐 어떤방법으로 쓸거냐
            // 에 따라 여러종류의 객체들을 연결시켜서 조합해서 사용
            // 할수 있는 부분임
            
        }
        
    }
    
}
