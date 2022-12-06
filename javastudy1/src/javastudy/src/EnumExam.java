package javastudy1.src.javastudy.src;

public class EnumExam {
    public static final String MALE = "MALE";
    public static final String FEMALE = "FEMALE";
    public static void main(String[] args) {
        String gender1;
        gender1 = EnumExam.MALE;
        gender1 = EnumExam.FEMALE;

        gender1 = "boy";
        System.out.println(gender1);

        Gender gender2;
        gender2 = Gender.MALE;
        gender2 = Gender.FEMALE;

        System.out.println(gender2);
        //gender2 = "boy"
        // 이런식으로 값 변경 불가
        
    }    
}
// 열거형 enum 변수명
enum Gender{
    MALE, FEMALE;

}