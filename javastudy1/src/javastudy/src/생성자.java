package javastudy1.src.javastudy.src;

public class 생성자 {
    String name;
    int number;
    // public 생성자(){
    //     this.name = "이름없음";
    //     this.number = 0;

    // }
    // 이런식으로 만들면 코드의 중복이 일어남
    // 자신이 가지고 있는 다른 생성자를 이용할 수 있다. 
    public 생성자(){
        // 여기서 this는 나의 생성자를 의미함
        this("이름없음", 0);
    }
    public 생성자(String name){
        this.name = name;
        // 이런식으로 들어오면 컴파일러는 매개변수로 받은 name을 name이라고 생각함
        // this = 내 구성요소, 내 필드 name에 매개변수로 받은name을 넣어주세요
        // this = 객체 자신을 참조하는 키워드 
    }
    public 생성자(String name, int number){
        this.name = name;
        this.number = number;
    }
    // 생성자 오버로딩
    // 메소드와 마찬가지로 매개변수의 수와 타입이 다르다면 여러개의 생성자를
    // 선언할수있다
}
