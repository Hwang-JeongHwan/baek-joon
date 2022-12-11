package Javastudy;

public class BusExam {
    public static void main(String[] args) {
        BusExam busExam = new BusExam();
        // // Bus bus = new Bus();
        // // bus.run();
        // // bus.name = "버스";
        // // System.out.println(bus.name);
        // // bus.num = 123;
        // // System.out.println(bus.num);
        // // bus.ppangppang();
        // //Car car = new Car();
        // //car.run();
        // //car.ppangppang(); 부모클래스는 자식이 가지고 있는것은 사용할수 없음 
        // // Bus bus = new Bus();
        // // bus.run();
        // Car c = new Bus();
        // // c.run();
        // // 실제로 생성된것은 Bus
        // //c.ppangppang() // 부모 타입으로 자식을 가리킬수는 있지만
        // // 이 경우 부모가 가지고 있는 내용만 사용가능
        // // 이런경우 Bus의 메소드를 사용하고 싶다면 형변환 해야함
        
        // //Bus bus = c;// 이렇게 하면 오류발생
        // // 컴파일러 입장에서는 Car타입인데 Bus가 가리킬수는 없다
        // // Car가 더 큰, 상위 개념이기 때문에 뭐가 올지 모름
        // // 아무런 Car를 가리키면서 Bus라고 할수없기 때문에 허용하지 않음
        // Bus bus = (Bus)c;
        // // bus.run();
        // // bus.ppangppang();
        // // bus.name = "버스";
        // // System.out.println(bus.name);
        // Bus bus1 = new Bus();
        // busExam.fill(bus1);
        // busExam.fill(bus1);
        // 이게 가능한게 Car가 참조하는 객체가 원래 Bus였기 때문에 가능
        //Car가 처음 생성됐을때 Car c = new Car();로 생성됐다면 오류가 나옴
        // 처음 생성할때 Bus였기 때문에 형변환이 가능
        
        //클래스들 끼리의 형 변환은 부모가 자식을 가리킬수는 있으나
        // 부모가 가리키고 있었을때는 부모가 알고있는 메소드까지만 접근이 가능함
        // 이런 이유 때문에 형변환을 해야지만 그 객체가 가지고 있는 모든 부분들을
        // 사용할수 있는경우가 있음 

        Suv suv = new Suv(); //suv 인스턴스 생성
        Truck truck = new Truck(); //truck 인스턴스 생성
        Bus bus = new Bus(); //bus 인스턴스 생성
        
        //gasStation에서 suv에 기름을 넣습니다.
        busExam.fill(suv);
        
        //gasStation에서 truck에 기름을 넣습니다.
      //  gasStation.fill(truck);
        
        //gasStation에서 bus에 기름을 넣습니다.
       // gasStation.fill(bus);
        
    }
    // public void fill(Car car){
    //     //참고. car.getClass().getName()은 car오브젝트가 실제로 어떤 클래스인지를 알려줍니다.
    //     System.out.println(car.getClass().getName()+"에 기름을 넣습니다.");

    //     car.gas += 10;
    //     System.out.println("기름이 "+car.gas+"리터 들어있습니다.");
    // }
    public void fill(Car car){
        //참고. car.getClass().getName()은 car오브젝트가 실제로 어떤 클래스인지를 알려줍니다.
        System.out.println(car.getClass().getName()+"에 기름을 넣습니다.");

        car.gas += 10;
        System.out.println("기름이 "+car.gas+"리터 들어있습니다.");
    }

}
/*
 * 접근제한자의 종류
public
어떤 클래스든 접근할 수 있다는 것을 의미
protected
자기 자신, 같은 패키지, 서로 다른 패키지다 하더라도 상속받은 자식 클래스에서는 접근할수 있다는 것을 의미
private
자기 자신만 접근할 수 있다는 것을 의미
접근제한자를 적지 않으면 default접근 지정자
자기자신과 같은 패키지에서만 접근할 수 있다는 것을 의미
 */