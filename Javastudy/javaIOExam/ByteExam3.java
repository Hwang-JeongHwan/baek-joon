package Javastudy.javaIOExam;

import java.io.DataOutput;
import java.io.DataOutputStream;
import java.io.FileOutputStream;

/* 다양한 타입의 출력
try-with-resources 블럭 선언
java io객체는 인스턴스를 만들고, 모두 사용하면 close()메소드를 호출해야 한다.
close()메소드를 사용자가 호출하지 않더라도, Exception이 발생하지 않았다면 
자동으로 close()가 되게 할 수 있는 방법
try-with-resource이용 
*/
public class ByteExam3 {
    public static void main(String[] args) {
        /*다양한 타입으로 저장 할 수 있는 DataOutputStream
            DataOutputStream은 장식이 되는 클래스이기 떄문에
            어디에다가 써라 라든가 이러한 부분은 사용할 수 없음
            장식이 되는 클래스와 어디에다가 쓸건지 지정해주는 클래스
            들을 같이 사용하게 하면됨 

            
            wirteInt() - 정수값으로 저장
            wirteBoolean() - boolean값으로 저장
            writeDouble() - double 값으로 저장
        */
        try(
            DataOutputStream out = new DataOutputStream(new FileOutputStream("Javastudy/javaIOExam/data.txt"));
            // 이렇게 선언하면 여러가지 데이터 타입을 받아서 파일에 저장할 수 있는 부분
            // 수행가능
        ){
            out.writeInt(100);  //4byte
            out.writeBoolean(true); //1byte
            out.writeDouble(50.5); //8byte
            // 원래 기본으로는 문자형이 쓰여지는데 
            // Data타입으로 사용했기 때문에 이부분을 읽어 낼 때에도
            // DataInputStream으로 읽어들여야함
        }catch(Exception e){
            e.printStackTrace();;
        }
        
    }
}
