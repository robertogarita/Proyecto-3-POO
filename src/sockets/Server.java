package sockets;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server implements Runnable {

    private int PORT;
    private String instruction = "";

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
                System.out.println("Esperando cliente");
                sc = server.accept();
                System.out.println("Cliente conectado");

                in = new DataInputStream(sc.getInputStream());
                out = new DataOutputStream(sc.getOutputStream());

                out.writeUTF(instruction);
                instruction = in.readUTF();

                sc.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
