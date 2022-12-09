package Javastudy.javaIOExam;

import java.io.DataInputStream;
import java.io.FileInputStream;

/*data.txt로부터 값을 읽어들여 화면에 출력하는 클래스

다양한 타입의 데이터를 읽어낼 수 있는 DataInputStream

readInt() -정수를 읽어들이는 메소드
readBoolean() - boolean 값을 읽어들이는 메소드
readDouble() - douboe 값을 읽어들이는 메소드 */
public class ByteExam4 {
    public static void main(String[] args) {
        try (
            DataInputStream in = new DataInputStream(new FileInputStream("Javastudy/javaIOExam/data.txt"));
        ) {
            int i = in.readInt();
            boolean b = in.readBoolean();
            double d = in.readDouble();
            // 파일에 있는 순서대로 읽어야함
            /*  파일에 저장된 순서대로 읽어 들여야한다.
                int, boolean, double순서대로 저장하였기 
                때문에 읽어들일 때도 같은 순서로 읽어여야 한다.
            */
            System.out.println(i);
            System.out.println(b);
            System.out.println(d);
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    
}
