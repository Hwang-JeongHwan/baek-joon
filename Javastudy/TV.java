package Javastudy;
/*인터페이스: 서로 관계가 없는 물체들이 상호 작용을 하기 위해서 사용하는 장치나 시스템 */
public interface TV{
    public int MAX_VOLUME = 100;
    public int MIN_VOLUME = 0;

    public void turnOn();
    public void turnOff();
    public void changeVolume(int volume);
    public void changeChannel(int channel);
}
/*
 * 인터페이스에서 변수를 선언하면 컴파일시 자동으로 아래와 같이 바뀐다.

    public static final int MAX_VOLUME = 100;
    public static final int MIN_VOLUME = 0;
    인터페이스에서 정의된 메소드는 모두 추상 메소드이다. 
    위에서 선언된 모든 메소드는 컴파일 시에 다음과 같이 자동으로 변경된다.

    public abstract void on();
    public abstract void off();
    public abstract void volume(int value);
    public abstract void channel(int number);
 */