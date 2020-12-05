package jsonPrueba;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import org.json.*;
public class Server {

    public static void main(String[] args) {

        ServerSocket server = null;
        Socket sc = null;
        DataInputStream in;
        DataOutputStream out;

        final int PORT = 5000;

        try {
            server = new ServerSocket(PORT);
            System.out.println("Servidor Iniciado");

            while(true){
                System.out.println("Esperando coneccion del cliente");
                sc = server.accept();
                System.out.println("Cliente conectado");

                in = new DataInputStream(sc.getInputStream());
                out = new DataOutputStream(sc.getOutputStream());

                System.out.println("Mensaje del cliente: ");
                
                JSONObject jsonRecibido = new JSONObject(in.readUTF());
                System.out.println(jsonRecibido);
                jsonRecibido.put("Despedida", "Todos");

                out.writeUTF(jsonRecibido.toString());

                
                System.out.println("\nCliente desconectado");
                sc.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
