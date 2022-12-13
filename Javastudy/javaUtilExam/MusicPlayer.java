package Javastudy.javaUtilExam;

public class MusicPlayer extends Thread {
    int type;
    MusicBox musicBox;
    // 객체 자체에 MusicBox를 가질수 있게 -> 아까 그네를 가질수있다 했던것처럼 가지게
    // 생성

    public MusicPlayer(int type, MusicBox musicBox){
        this.type = type;
        this.musicBox = musicBox;
        
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        // super.run();
        // 뮤직박스가 가지고있던 메소드들을 다르게 호출할수 있게 하려고 run()메소드 추가
        switch (type){
            case 1:
                musicBox.playMusicA();
                break;
            case 2:
                musicBox.playMusicB();
                break;
            case 3:
                musicBox.playMusicC();
                break;
        }
    }

    
}
