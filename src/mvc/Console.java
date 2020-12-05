package mvc;

import sockets.Server;

public class Console {

    public Console(){

        Server s = new Server(6000);
        Thread t = new Thread(s);
        t.start();

    }
    public static void main(String[] args) {
        new Console();
    }
}
