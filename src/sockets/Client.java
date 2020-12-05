package sockets;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client implements Runnable {

    private int PORT;
    private String key;

    public Client(int PORT, String key) {
        this.PORT = PORT;
        this.key = key;
    }

    @Override
    public void run() {

        final String HOST = "127.0.0.1";
        DataOutputStream out;
        DataInputStream in;

        try {
            Socket sc = new Socket(HOST, PORT);

            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());

            if(key == null){
                System.out.println(in.readUTF());
            }else{
                out.writeUTF(key);
            }


            sc.close();

        } catch (UnknownHostException ex) {
            ex.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
