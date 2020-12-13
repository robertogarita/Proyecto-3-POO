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
    private int X;
    private int Y;
    private boolean startOne = true;
    String Mapa, PosX, PosY;
    Image fondo;
    JLabel label1;

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
        drawCharacter(g);
    }
    public void Back(){
        ImageIcon icon = new ImageIcon(loadImage(Mapa));
        label1.setIcon(icon);
    }
    public void drawCharacter(Graphics g) {
        X *= 14;
        Y *= 14;

        g.setColor(Color.YELLOW);
        g.fillOval(X, Y, 14, 14);
        startOne = false;
    }


    public Image loadImage(String file){
        try {
            return ImageIO.read(getClass().getResourceAsStream(file));
        } catch (IOException e) {
            return null;
        }
    }


    @Override
    public void update(Observable o, Object arg) {
        moveCollection = new JSONArray(arg.toString());

        PosX = String.valueOf(moveCollection.get(0));
        PosY = String.valueOf(moveCollection.get(1));
        Mapa = String.valueOf(moveCollection.get(2));

        X = Integer.parseInt(PosX);
        Y = Integer.parseInt(PosY);
        repaint();
    }
}
