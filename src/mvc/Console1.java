package mvc;

import java.util.ArrayList;
import java.util.Observable;
import java.util.Observer;
import org.json.JSONArray;
import org.json.JSONObject;
import games.JuegoDePrueba;
import games.pacman.Pacman;
import sockets.Client;
import sockets.Server;

public class Console1 implements Observer {

    private JSONObject keyCollection;
    private JSONArray moveCollection, Obstacules;
    private String keyPressed;
    private Boolean gameInside = false;
    private JuegoDePrueba JP;
    private ArrayList<int[]> obsSelect;

    public Console1() {

        Server s = new Server(6000);
        s.addObserver(this);
        Thread t = new Thread(s);
        t.start();

        new Screen();
        new Controller();
        engine();
    }

    // Comunicacion entre la consola - pantalla
    public void comunicateScreen() {

        moveCollection = new JSONArray();

        moveCollection.put(JP.getPosX());
        moveCollection.put(JP.getPosY());
        moveCollection.put(JP.getfilePath());

        Client cConsole = new Client(7000, moveCollection.toString());
        Thread tConsole = new Thread(cConsole);
        tConsole.start();
    }

    // Comunicacion entre la consola - controller
    @Override
    public void update(Observable o, Object arg) {
        keyCollection = new JSONObject(arg.toString());
        keyPressed = keyCollection.get("KEY").toString();

        engine();
    }

    public void engine() {
        if (!gameInside) {
            JP = new Pacman(24, 30, "/resources/MapaPacman.png");
            gameInside = true;
        }

        if (keyPressed != null) {
            switch (keyPressed) {
                case "d":
                    if (CheckMove(JP.getPosX() + 1, JP.getPosY())) {
                        JP.setPosX(JP.getPosX() + 1);
                    }
                    break;

                case "a":
                    if (CheckMove(JP.getPosX() - 1, JP.getPosY())) {
                        JP.setPosX(JP.getPosX() - 1);
                    }
                    break;

                case "w":
                    if (CheckMove(JP.getPosX(), JP.getPosY() - 1)) {
                        JP.setPosY(JP.getPosY() - 1);
                    }
                    break;

                case "s":
                    if (CheckMove(JP.getPosX(), JP.getPosY() + 1)) {
                        JP.setPosY(JP.getPosY() + 1);
                    }
                    break;
            }
        }
        comunicateScreen();
    }

    public boolean CheckMove(int futureX, int futureY) {
        if (futureX == 0 || futureX == 49 || futureY == 0 || futureY == 49) {
            return false;
        } else {

            obsSelect = new ArrayList<int[]>();

            if (futureX <= 24 && futureY <= 24) {
                obsSelect.add(JP.getObstaculesSquare1());
                obsSelect.add(JP.getObstaculesLine1());
            } else if (futureX >= 25 && futureY <= 24) {
                obsSelect.add(JP.getObstaculesSquare2());
                obsSelect.add(JP.getObstaculesLine2());
            } else if (futureX <= 24 && futureY >= 25) {
                obsSelect.add(JP.getObstaculesSquare3());
                obsSelect.add(JP.getObstaculesLine3());
            } else {
                obsSelect.add(JP.getObstaculesSquare4());
                obsSelect.add(JP.getObstaculesLine4());
            }

            int listSq[] = obsSelect.get(0);
            int listLi[] = obsSelect.get(1);

            int lim;
            int x1, x2, y1, y2;

            for (int i = 0; i < listLi.length; i += 4) {
                x1 = listLi[i];
                x2 = listLi[i + 2];
                y1 = listLi[i + 1];
                y2 = listLi[i + 3];
                if (((x1 <= futureX) && (x2 >= futureX)) && ((y1 <= futureY) && (y2 >= futureY))) {
                    return false;
                }
            }

            for (int i = 3; i < listSq.length; i += 4) {

                lim = listSq[i];
                x1 = listSq[i - 3];
                x2 = listSq[i - 1];
                y1 = listSq[i - 2];

                for (int a = 0; a <= lim; a++) {
                    if (((x1 <= futureX) && (x2 >= futureX)) && ((y1 + a <= futureY) && (y1 + a >= futureY))) {
                        return false;
                    }
                }
            }
            return true;
        }

    }

    public static void main(String[] args) {
        new Console1();
    }
}
