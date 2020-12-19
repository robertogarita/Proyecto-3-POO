package sockets;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Observable;

public class Server extends Observable implements Runnable {

    private int PORT;
    private String messageSent;

    public Server(int PORT) {
        this.PORT = PORT;
    }

    @Override
    public void run() {

        ServerSocket server;
        Socket sc;
        DataInputStream in;

        try {
            server = new ServerSocket(PORT);

            while(true){
                //System.out.println("Esperando cliente");
                sc = server.accept();
                //System.out.println("Cliente conectado");

                in = new DataInputStream(sc.getInputStream());

                messageSent = in.readUTF();

                this.setChanged();
                this.notifyObservers(messageSent);
                this.clearChanged();

                sc.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
