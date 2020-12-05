package jsonPrueba;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import org.json.*;

public class Client {

    public static void main(String[] args) {

        final String HOST = "127.0.0.1";
        final int PORT = 5000;
        DataInputStream in;
        DataOutputStream out;
        //OutputStreamWriter out;

        JSONObject jArray = new JSONObject();

        jArray.put("Saludo_1", "Deyner");
        jArray.put("Saludo_2", "Lidia");
        jArray.put("Saludo_3", "Guego");

        try {
            Socket sc = new Socket(HOST, PORT);

            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());
            //out = new OutputStreamWriter(sc.getOutputStream(), StandardCharsets.UTF_8);

            System.out.println("Mensaje enviado");
            out.writeUTF(jArray.toString());

            JSONObject json = new JSONObject(in.readUTF());
            System.out.println(json);
            System.out.println(json.getString("Despedida"));

            System.out.println("\nCliente desconectado");
            sc.close();

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
