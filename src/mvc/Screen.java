package mvc;

import java.util.Observable;
import java.util.Observer;
import javax.swing.JFrame;
import org.json.JSONArray;
import java.awt.*;
import sockets.Server;


public class Screen extends JFrame implements Observer{

    private static final long serialVersionUID = 1L;
    private Server s;
    private int matriz[][];
    private JSONArray moveCollection;
    private int X;
    private int Y;

    public Screen() {

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);
        setVisible(true);
        setSize(700, 700);

        s = new Server(7000);
        s.addObserver(this);
        Thread t = new Thread(s);
        t.start();
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        drawCharacter(g);
    }

    public void drawCharacter(Graphics g){
        X *= 14;
        Y *= 14;

        g.setColor(Color.CYAN);
        g.fillOval(X, Y, 14, 14);
    }

    
    @Override
    public void update(Observable o, Object arg) {
        moveCollection = new JSONArray(arg.toString());

        String PosX = String.valueOf(moveCollection.get(0));
        String PosY = String.valueOf(moveCollection.get(1));

        X = Integer.parseInt(PosX);
        Y = Integer.parseInt(PosY);

        repaint();
    }
}
