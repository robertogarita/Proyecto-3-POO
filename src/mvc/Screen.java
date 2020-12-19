package mvc;

import java.util.Observable;
import java.util.Observer;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import org.json.JSONArray;
import java.awt.*;
import java.io.IOException;

import sockets.Server;

public class Screen extends JFrame implements Observer {

    private static final long serialVersionUID = 1L;
    private Server s;
    private JSONArray moveCollection;
    private int X, ShX = 0;
    private int Y, ShY = 0;
    private boolean startOne = true, gameIn = false;
    private String map = "", posX, posY, shotX, shotY, previousMap = "";
    private JLabel label1;

    public Screen() {
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);
        setUndecorated(true);
        setSize(700, 700);
        setVisible(true);

        getContentPane().setBackground(Color.BLACK);

        label1 = new JLabel();
        label1.setBounds(0, 0, 700, 700);
        add(label1);

        s = new Server(7000);
        s.addObserver(this);
        Thread t = new Thread(s);
        t.start();
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        if (startOne) {
            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            Back();
        }
        if(gameIn){
            drawCharacter(g);
            if(ShY != 0){
                drawShot(g);
            }
        }
    }

    public void Back() {
        try {
            previousMap = map;
            ImageIcon icon = new ImageIcon(loadImage(map));
            label1.setIcon(icon);
        } catch (NullPointerException ex) {
        }
    }

    public void drawShot(Graphics g){
        g.setColor(Color.GREEN);
        g.fillRect(ShX*14, ShY*14, 14, 14);
    }

    public void drawCharacter(Graphics g) {
        X *= 14;
        Y *= 14;
        g.setColor(Color.YELLOW);
        g.fillOval(X, Y, 14, 14);
        startOne = false;
    }

    public Image loadImage(String file) {
        try {
            return ImageIO.read(getClass().getResourceAsStream(file));
        } catch (IOException e) {
            return null;
        }
    }

    @Override
    public void update(Observable o, Object arg) {
        moveCollection = new JSONArray(arg.toString());
        gameIn = true;

        posX = String.valueOf(moveCollection.get(0));
        posY = String.valueOf(moveCollection.get(1));
        map = String.valueOf(moveCollection.get(2));
        shotX = String.valueOf(moveCollection.get(3));
        shotY = String.valueOf(moveCollection.get(4));

        if(!(previousMap.equals(map))){
            startOne = true;
        }

        X = Integer.parseInt(posX);
        Y = Integer.parseInt(posY);
        ShY = Integer.parseInt(shotY);
        ShX = Integer.parseInt(shotX);
        repaint();
    }
}
