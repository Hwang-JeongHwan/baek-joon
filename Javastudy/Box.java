package Javastudy;

// public class Box {
//     private Object obj;

//     //값을 설정할수있는 setobj라는 메소드와 해당 obj의 값을 반환하는 get메소드 설정
//     public void setObj(Object obj){
//         this.obj = obj;
//     }

//     public Object getObj(){
//         return obj;
//     }
//             // 자바5에는 Generic이라는 문법이 사용됨으로써 인스턴스를 만들때 
//         // 사용하는 타입을 지정하는 문법이 추가가 됨 
//         // 기존의 그냥 사용했던 방식을 보면
//         // Object타입으로 받았기 때문에 모든 객체가 다 들어갈수 있는데
//         // 모든 객체가 다 들어가기 때문에 다시 꺼내서 사용할때 매번 형변환을
//         // 해야 사용하기 편함
//         // 이부분을 Generic으로 바꿔보도록 하자
//         // 클래스 부분 뒤에 <E>라고  추가
//         // Object가 들어간 부분 뒤에도 다 <E>라고 추가
// }

public class Box<E> {
    private E obj;

    //값을 설정할수있는 setobj라는 메소드와 해당 obj의 값을 반환하는 get메소드 설정
    public void setObj(E obj){
        this.obj = obj;
    }

    public E getObj(){
        return obj;
    }
            // 자바5에는 Generic이라는 문법이 사용됨으로써 인스턴스를 만들때 
        // 사용하는 타입을 지정하는 문법이 추가가 됨 
        // 기존의 그냥 사용했던 방식을 보면
        // Object타입으로 받았기 때문에 모든 객체가 다 들어갈수 있는데
        // 모든 객체가 다 들어가기 때문에 다시 꺼내서 사용할때 매번 형변환을
        // 해야 사용하기 편함
        // 이부분을 Generic으로 바꿔보도록 하자
        // 클래스 부분 뒤에 <E>라고  추가
        // Object가 들어간 부분 뒤에도 다 E로 변경
        // E는 실제로 존재하는 클래스는 아님, 그래서 이제 이렇게 지정하는 것을
        // 제너릭을 사용했다고 보면됨 


}
