package sockets;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Observable;

public class Server extends Observable implements Runnable {

    private int PORT;
    private String messageIncome;

    public Server(int PORT) {
        this.PORT = PORT;
    }

    @Override
    public void run() {

        ServerSocket server;
        Socket sc;
        DataInputStream in;
        DataOutputStream out;

        try {
            server = new ServerSocket(PORT);

            while(true){
                //System.out.println("Esperando cliente");
                sc = server.accept();
                //System.out.println("Cliente conectado");

                in = new DataInputStream(sc.getInputStream());
                out = new DataOutputStream(sc.getOutputStream());

                messageIncome = in.readUTF();

                this.setChanged();
                this.notifyObservers(messageIncome);
                this.clearChanged();

                sc.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void getInfo(){}
}
