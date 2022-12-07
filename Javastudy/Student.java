package Javastudy;
// Object 클래스는 모든 클래스의 최상위 클래스
// 아무것도 상속받지 않으면 자동으로 Object를 상속받음
// 이 말은 오브젝트가 가지고 있는 메서드는 모든 클래스에서 다 사용할 수 있다는 것을
// 의미함
// 오브젝트가 가지고 있는 메소드 중에서 가장 많이 사용되는 메서드는 equals, toString,
// hashCode임 이 세가지 메소드들은 반드시 오버라이딩 해서 사용해야함
// equals는 객체가 가진 값을 비교할 때 사용 -> 같은 값인지 아닌지 확인할때
// 객체간의 같다 다르다 라고 비교하려면 어떤 기준을 가지고 있어야함
// 학생이라는 객체가 있을때 학번만 같으면 같다라고 볼건지 이름만 같으면 같다라고 볼건지
// 즉 오브젝트는 같은 값인지 다른값인지에 대해서 비교할 수 있는 메소드는 제공하고
// 있지만 그 메소드를 오버라이딩해서 기준을 정해주는 것은 프로그래머가 할 일임
// String 클래스의 equals메소드는 오브젝트가 가지고 있는 메소드를 오버라이딩 한것임
// String클래스가 가진 이퀄스를 사용했을때 안에 들어있는 문자열들이 다 같으면 같다고
// return


// hashCode라는 메소드는 무엇일까 -> 객체의 해시코드를 구하는것
// 해시코드의 값은 객체별로 서로 다른 값을 가지게 하는 것이 좋음
// 해시코드는 알게모르게 사용됨 -> 자료구조에[서
// toString메소드는 객체가 가지고 있는 값을 문자열로 바꿔줌

// 이런 세가지 메소드는 굉장히 자주 사용되기 때문에 대부분 개발자 도구에서 자동으로
// 생성하는 기능을 가지고 있음.

public class Student {
    String name;
    String number;
    int birthYear;
    // 이름 학번 생년을 속성으로 가지는 스튜던트라는 클래스
    
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "홍길동";
        s1.number = "1234";
        s1.birthYear = 1995;

        Student s2 = new Student();
        s2.name = "홍길동";
        s2.number = "1234";
        s2.birthYear = 1995;

        if (s1.equals(s2)){
            //두개 객체가 같은지 다른지 확인하는 메소드 s1.equals(s2)
            System.out.println("s1 == s2");

        }
        else{
            System.out.println("s1 != s2");
        }
        // 두개가 동일하게 만들어졌긴하지만 다르다고 나옴
        System.out.println(s1.hashCode());
        System.out.println(s2.hashCode());
        // equals라는 메소드와 hashCode라는 메소드를 오브젝트가 구현하고 있는
        // 메소드들을 그냥 사용하고 있기 때문에 다르다고 나옴
        // 알맞게 오버라이딩해서 써야한다고 처음에 얘기함
        System.out.println(s1);
        // student객체의 속성을 출력하고 싶은경우가 많음
        System.out.println(s1.toString());
        // 위아래 출력하는것은 같음 같은 결과가 출력됨
        // 내부적으로 객체를 출력하면 toString()이라는 메소드를 호출해서 출력하는것을
        // 알수있음 
        
    }

    @Override
    public String toString() {
        return "Student [name=" + name + ", number=" + number + ", birthYear=" + birthYear + "]";
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((number == null) ? 0 : number.hashCode());
        return result;
        // 해시코드르르 구하는것은 일종의 수학식
        // 되도록 유일하지 않은 값을 반환하도록 함
        // 소수중의 하나인 31과 특정값을 곱해서 만듬
        // 자동으로 만들어진 이 코드 말고도 다양한 방법이 있을수 있음
        // 이부분은 알고리즘을 따로 공부
    }

    @Override
    public boolean equals(Object obj) {
        // 메소드에 파라미터로 들어온 오브젝트와 자기 자신을 비교
        // this와 obj가 같다면 참조가 같은것을 의미하므로 무조건 같음
        // 인자로 들어온 obj가 null이라면 비교할 필요없이 false return

        // getClass()는 오브젝트가 가지고있는 메소드로 클래스의 정보를 가지고 있음
        // Class라는 객체를 반환함
        // 자기 자신의 클래스 정보와 obj의 클래스 정보가 다른 경우 false반환
        
        // 서로 다른 클래스들 끼리 값을 비교할 필요가 없음
        // 그이유는 obj를 student로 형변환 한후에 자신의 number와 obj의 number를
        // 비교해서 같으면 true 다르면 false반환 
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Student other = (Student) obj;
        if (number == null) {
            if (other.number != null)
                return false;
        } else if (!number.equals(other.number))
            return false;
        return true;
    }
}
