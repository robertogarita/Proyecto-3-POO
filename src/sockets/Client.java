package sockets;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client implements Runnable {

    private int PORT;
    private String key, HOST;

    public Client(int PORT, String key) {
        this.PORT = PORT;
        this.key = key;
    }

    @Override
    public void run() {

        DataOutputStream out;
        DataInputStream in;

        HOST = "127.0.0.1";

        try {
            Socket sc = new Socket(HOST, PORT);

            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());

            out.writeUTF(key);

            sc.close();

        } catch (UnknownHostException ex) {
            ex.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
