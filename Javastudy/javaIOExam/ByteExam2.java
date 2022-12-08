package Javastudy.javaIOExam;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
// Byte단위 입출력 심화
// Byte단위 입출력 클래스는 클래스의 이름이 InputStream이나 OutputStram으로 끝남


// 파일로 부터 512Byte씩 읽어들여 512Byte씩 저장하는 프로그램을 작성
public class ByteExam2 {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        FileInputStream fis = null;
        FileOutputStream fos = null;
        
        try {
            fis = new FileInputStream("Javastudy/javaIOExam/ByteExam2.java");
            // 읽어들일 파일의 경로입력
            
            fos = new FileOutputStream("Javastudy/javaIOExam/byte2.txt");
            int readCount = -1;
            // 읽어들은 수를 저장하기 위해서 사용할 변수 readCount

            byte[] buffer = new byte[512];

            
            // byte[] buffer = new byte[512];
            // 512byte 만큼 읽어들이기 위해 byte배열 사용
            // 최대 512바이트를 읽어들인다. 
            // 처음 읽을떄는 512바이트가 될수있지만 두번째는 아닐수도 있음
            // 더이상 읽어들일것이 없으면 read메소드는 -1을 반환
            while ((readCount = fis.read(buffer)) != -1){ // 파일이 끝나면 -1리턴
                fos.write(buffer, 0, readCount);
                // readCount 만큼 써주세요 라는뜻 
                // 이전 예제보다 훨씬 수행시간이 짧음

                

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
        // 속도차이가 나는 이유 : 우리가 사용하는 운영체제는 1바이트씩만
        // 읽어오려고해도 보통 512바이트씩 읽어옴
        // 그래서 1바이트를 두번읽어오라고 하면 512바이트를 한번 읽어온뒤에
        // 한바이트만쓴다음에 그다음 511바이트는 버리고 이런식으로 반복
        // 어차피 OS에서 512바이트씩 읽어오기 때문에 파일을 읽어올때는
        // 512바이트의 배수로 배열의 크기를 잡아주는것이 성능상 좋음 
    }
}