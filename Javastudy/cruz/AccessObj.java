package Javastudy.cruz;

public class AccessObj {
/*
 * 접근제한자의 종류
public
어떤 클래스든 접근할 수 있다는 것을 의미 // 가장 넓은의미, 전체 공개라고 생각

protected
자기 자신, 같은 패키지, 서로 다른 패키지다 하더라도 상속받은 
자식 클래스에서는 접근할수 있다는 것을 의미 => 일단 패키지가 같아야함
같은 패키지에 있는것들은 공개할거고 다른 패키지에 있다 하더라도 상속을 받은
내 자식클래스에게는 접근할수 있게 해줌

private
자기 자신만 접근할 수 있다는 것을 의미


접근제한자를 적지 않으면 
default접근 지정자
자기자신과 같은 패키지에서만 접근할 수 있다는 것을 의미


 */    
    public int p = 3;
    protected int p2 = 4;
    private int i = 1;
    int k = 2; //defalut 접근 지정자
    // 자기 자신과 같은 패키지 에서만 접근할수 있다는 것을 의미함

    // 넓은 순 public > protected > defalut > private
}
