package mvc;

import java.util.ArrayList;
import java.util.Observable;
import java.util.Observer;
import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.json.JSONArray;
import org.json.JSONObject;
import games.SelectedGame;
import games.pacman.Pacman;
import games.spaceInvaders.SInvaders;
import sockets.Client;
import sockets.Server;

public class Console extends JFrame implements Observer, ActionListener, Runnable {

    private JSONObject keyCollection;
    private JSONArray moveCollection;
    private String keyPressed;
    private Boolean canShot, haveObs, UpDownMove, gameIn = false;
    private SelectedGame JP;
    private ArrayList<int[]> obsSelect;
    private JButton game1, game2;
    private Thread tshot;

    public Console() {
        setBounds(900, 100, 300, 300);
        setVisible(true);

        game1 = new JButton("Pacman");
        game1.setBounds(75, 100, 150, 30);
        game1.addActionListener(this);
        add(game1);
        game2 = new JButton("Space Invaders");
        game2.setBounds(75, 145, 150, 30);
        game2.addActionListener(this);
        add(game2);

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
        moveCollection.put(JP.getShotX());
        moveCollection.put(JP.getShotY());

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
        if (keyPressed != null && gameIn) {
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
                    if (CheckMove(JP.getPosX(), JP.getPosY() - 1) && UpDownMove) {
                        JP.setPosY(JP.getPosY() - 1);
                    }
                    break;

                case "s":
                    if (CheckMove(JP.getPosX(), JP.getPosY() + 1) && UpDownMove) {
                        JP.setPosY(JP.getPosY() + 1);
                    }
                    break;
                case "k":
                    if(canShot){
                        tshot = new Thread(this);
                        tshot.start();
                    }
            }
            comunicateScreen();
        }
    }

    public boolean CheckMove(int futureX, int futureY) {
        if (futureX == 0 || futureX == 49 || futureY == 0 || futureY == 49) {
            return false;
        } else if (haveObs) {
            
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
        return true;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == game1) {
            JP = new Pacman(24, 30, "/resources/MapaPacman.png");
            game1.setEnabled(false);
            game2.setEnabled(true);
            canShot = false;
            haveObs = true;
            UpDownMove = true;
            gameIn = true;
            comunicateScreen();
        }
        if (e.getSource() == game2) {
            game1.setEnabled(true);
            game2.setEnabled(false);
            JP = new SInvaders(24, 45, "/resources/MapaSpaceInvaders.png");
            canShot = true;
            haveObs = false;
            UpDownMove = false;
            gameIn = true;
            comunicateScreen();
        }
    }

    @Override
    public void run() {
        int defineX = JP.getPosX();
        int defineY = JP.getPosY();

        JP.setShotY(defineY-1);
        JP.setShotX(defineX);

        while (JP.getShotY() > -1) {
            canShot = false;
            JP.setShotY(JP.getShotY() - 1);
            comunicateScreen();
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        canShot = true;
    }

    public static void main(String[] args) {
        new Console();
    }
}
