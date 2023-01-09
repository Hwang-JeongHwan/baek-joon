package Javastudy.javaIOExam;
// Byte 단위 입출력
// Byte 단위 입출력 클래스는 클래스 이름이 InputStream이나 OutputStream으로 끝남

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class ByteExam1 {
    // 파일로 부터 1byte씩 일어들여 파일에 1byte씩 저장하는 프로그램을 작성
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();        
        FileInputStream fis = null;
        FileOutputStream fos = null;
        
        try {
            fis = new FileInputStream("Javastudy/javaIOExam/ByteExam1.java");
            // 읽어들일 파일의 경로입력
            
            fos = new FileOutputStream("Javastudy/javaIOExam/byte.txt");
            
            int readData = -1;
            // 읽어 들였을때 값을 담기 위해 readData라는 변수하나 선언
            // fileinputstream의 read라는 메소드는 한바이트씩 읽을수 있음
            //read메소드가 return하는 타입은 정수형이고  정수의 4바이트 중에서
            // 마지막 바이트의 읽어들인 1바이트를 저장함
            // byte를 리턴하면 끝을 나타내는 값을 표현할수 없기 때문에 바이트가
            // 아닌 int값을 리턴 , 음수의 경우 맨 좌측비트가 1 , 읽어들일것이 있으면
            // 항상 양수값을 리턴

            // 읽어들일 코드가 여러줄 있을수 있기때문에 반복문으로
            // 읽어들일 데이터를 readDate에 달아줄것
            while ((readData = fis.read()) != -1){ // 파일이 끝나면 -1리턴
                fos.write(readData);
                // System.out.println(readData);


            }
            

        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } finally{
            try {
                fis.close();
                
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            try {
                fos.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

        }
        long endTime = System.currentTimeMillis();
        System.out.println(endTime - startTime);
    }
}
