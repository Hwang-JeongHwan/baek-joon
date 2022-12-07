package Javastudy;

public class BoxExam {
    public static void main(String[] args) {
        // Box box = new Box();
        // box.setObj(new Object());
        // Object obj = box.getObj();
        // System.out.println(obj);
        
        // box.setObj("hello");

        // // type이 Object라는것은 Object타입만 들어올수 있는게 아니라 
        // // Object의 후손, 자식클래스라면 무엇이든지 다 들어올수 있음
        // // setObj안에는 String, int등 다른 모든 Object를 상속받은 객체들이 들어갈 수 잇음
        // // 이때 box에서 값을 꺼내서 사용하게 되면
        // String str = (String)box.getObj();
        // // String을 reference하는 타입이 Object로 반환됨
        // // Object 타입으로 자식들을 다 가리킬수는 있었으나 그랬을때 자식이 가진 메소드에는
        // // 접근할수 없음 -> String이 가지고 있는 특징을 가지고 다 사용하고 싶다
        // // 할때 사용하는게 형 변환임
        // System.out.println(str);
        // box.setObj(1);
    
        // int value = (int)box.getObj();
        // System.out.println(value);
        // // 자바5에는 Generic이라는 문법이 사용됨으로써 인스턴스를 만들때 
        // // 사용하는 타입을 지정하는 문법이 추가가 됨 
        // // 기존의 그냥 사용했던 방식을 보면
        // // Object타입으로 받았기 때문에 모든 객체가 다 들어갈수 있는데
        // // 모든 객체가 다 들어가기 때문에 다시 꺼내서 사용할때 매번 형변환을
        // // 해야 사용하기 편함
        // // 이부분을 Generic으로 바꿔보도록 하자
        // // 클래스 부분 뒤에 <E>라고  추가
        
        //제너릭 지정한 부분
        Box<Object> box = new Box<>();
        // 박스를 생성하는데 , 이게 제너릭임,
        // Object타입을 받아들일수 있도록 생성하겠다 라고 할 수 있음
        // 아까처럼 똑같이
        box.setObj(new Object());
        Object obj = box.getObj();
        // 이렇게 사용하는건 같은데 제너릭이 가능하기 때문에

        Box<String> box2 = new Box<>();

        // 이렇게 하면 처음부터 Box에는 String값만 받을것이다 라고 선언함
        box2.setObj("hello"); //이렇게하면 String만 받을수 있게 쓸수 잇음
        String str2 = box2.getObj();

        Box<Integer> box3 = new Box<>();
        box3.setObj(4);
        int v2 = box3.getObj();
        // 형변환을 거치지 않고 바로 꺼내서 쓸수 있음

        // 자동으로 인트로 바꿔서 넣어주고 자동으로 인트로 바꿔서 꺼내주기 때문에
        // 이렇게 쓸수 있음 
        // 가상의 타입으로 선언해 주고 실제로 사용할땐 구체적으로 타입들을
        //설정함으로써 다양한  타입의 클래스를 이용하는 클래스를 만들어 낼 수 있음
        // 제너릭을 사용하는 대표적인 클래스는 컬렉션 프레임워크와 관련된
        // 클래스들이 있음 

    }
    
}
