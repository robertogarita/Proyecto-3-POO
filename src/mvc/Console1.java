package mvc;


import java.util.Observable;
import java.util.Observer;
import org.json.JSONArray;
import org.json.JSONObject;

import games.JuegoDePrueba;
import sockets.Client;
import sockets.Server;

public class Console1 implements Observer {

    Client clientConsole;
    JSONObject keyCollection;
    JSONArray moveCollection;
    String keyPressed;
    Boolean gameInside = false;
    JuegoDePrueba JP;

    public Console1() {

        Server s = new Server(6000);
        s.addObserver(this);
        Thread t = new Thread(s);
        t.start();

        new Screen();
        new Controller();
        engine();
    }

    //Comunicacion entre la consola - pantalla
    public void comunicateScreen(){

        moveCollection = new JSONArray();

        moveCollection.put(JP.getPosX());
        moveCollection.put(JP.getPosY());

        Client cConsole = new Client(7000, moveCollection.toString());
        Thread tConsole = new Thread(cConsole);
        tConsole.start();
    }

    //Comunicacion entre la consola - controller
    @Override
    public void update(Observable o, Object arg) {
        keyCollection = new JSONObject(arg.toString());
        keyPressed = keyCollection.get("KEY").toString();

        engine();
    }

    public void engine(){
        if(!gameInside){
            JP = new JuegoDePrueba(5, 8);
            gameInside = true;
        }

        if(keyPressed != null){
            switch (keyPressed) {
                case "d":
                    JP.setPosX(JP.getPosX()+1);
                    break;
                case "a":
                    JP.setPosX(JP.getPosX()-1);
                    break;
                case "w":
                    JP.setPosY(JP.getPosY()-1);
                    break;
                case "s":
                    JP.setPosY(JP.getPosY()+1);
                    break;
            }
        }
        comunicateScreen();

    }

    public static void main(String[] args) {
        new Console1();
    }
}
