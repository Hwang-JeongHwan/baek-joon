package javastudy1.src.javastudy.src;

public class VariableScopeExam {
    int globalScope = 10;
    static int staticVal = 7;
    public void scopeTest(int value){
        int localScope = 20;
        System.out.println(globalScope);
        System.out.println(localScope);
        System.out.println(value);
    }
    public void scopeTest2(int value2){
        System.out.println(globalScope);
        // System.out.println(localScope);
        // System.out.println(value);
        System.out.println(value2); 
        System.out.println(staticVal);
    }
    public static void main(String[] args) {
        // System.out.println(globalScope);
        // System.out.println(localScope);
        // System.out.println(value);
        // 모든 클래스는 인스턴스화 하지 않은채로 사용할 수 없다.
        // 키워드 static을 사용하면 인스턴스화 하지 않아도 사용할 수 있다.
        System.out.println(staticVal);
        VariableScopeExam v1 = new VariableScopeExam();
        System.out.println(v1.globalScope);
        VariableScopeExam v2 = new VariableScopeExam();
        v1.globalScope = 50;
        v2.globalScope = 20;
        int x2 = 10;
        System.out.println(v1.globalScope);
        System.out.println(v2.globalScope);
        v1.staticVal = 50;
        v2.staticVal = 100;
        System.out.println(v1.staticVal);
        System.out.println(v2.staticVal);
        // 클래스변수 : static한 변수, 값을 저장할 수 있는 공간이 하나 밖에없어서
        // 값을 공유한다.
        System.out.println(VariableScopeExam.staticVal);
    }
    
}
