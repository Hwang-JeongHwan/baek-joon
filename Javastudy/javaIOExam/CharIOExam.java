package Javastudy.javaIOExam;
import java.io.*;
import java.io.InputStreamReader;

/*Char 단위 입출력(Console)
char단위 입출력 클래스는 클래스 이름이 Reader나 Writer로 끝이 납니다.

char단위 입출력 클래스를 이용해서 키보드로 부터 한줄 입력 
받아서 콘솔에 출력
System.in - 키보드를 의미 (InputStream )
BufferedReader - 한줄씩 입력 받기위한 클래스
BufferedReader 클래스의 생성자는 InputStream을 입력받는 생성자가 없다.
->  BufferedReader는 Reader객체만 받아들일수 있음
-> System.in을 Reader의 형태로 바꾸어줘야하는데 이걸 해주는게 
InputStreamReader임 -> Reader를 상속받고 있기 때문에 Reader임
System.in은 InputStream 타입이므로 BufferedReader의 
생성자에 바로 들어갈 수 없으므로 InputStreamReader 클래스를 이용해야함.
 */
public class CharIOExam {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 데코레이터 패턴
        // 근원지가 될수있는 부분과 기능을 가지고 있는 부분을 끼워서 사용한다고해서
        // 데코레이터 패턴이라고 할수있음
        // 키보드로부터 한줄씩 입력받을수 있는 코드 작성
        String line = null;
        
        try {
            line = br.readLine();
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
        System.out.println(line);

    }
}
