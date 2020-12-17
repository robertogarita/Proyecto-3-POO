package mvc;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import org.json.JSONObject;
import sockets.Client;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.util.ArrayList;
import java.awt.event.KeyEvent;
import java.awt.*;

public class Controller extends JFrame implements KeyListener, MouseListener {

    private static final long serialVersionUID = 1L;
    
    private int control_position[] = { 30, 135, 210, 135, 120, 55, 120, 215 };
    private ArrayList<Image> imageList;
    private String btnPressed = "";
    private int counter = 0;
    private boolean releaseKey = true;

    private JSONObject jObject;

    Client clientControl;

    public Controller() {
        jObject = new JSONObject();
        setImageList();

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);
        setSize(700,360);
        getContentPane().setBackground(new Color(215,215,215));
        setVisible(true);
        addKeyListener(this);
        addMouseListener(this);
    }

    // ---------------- START User Inputs ------------------------------

    // Keyboard Actions
    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
        try {
            btnPressed = String.valueOf(e.getKeyChar());
        } catch (NullPointerException ex) {
        }

        jObject.put("KEY", btnPressed);

        clientControl = new Client(6000, jObject.toString());
        Thread t = new Thread(clientControl);
        t.start();

        jObject.remove(btnPressed);

        if (releaseKey) {
            repaint();
            releaseKey = false;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        repaint();
        btnPressed = "";
        releaseKey = true;
    }

    // Mouse actions
    @Override
    public void mouseClicked(MouseEvent e) {
    }

    @Override
    public void mousePressed(MouseEvent e) {
    }

    @Override
    public void mouseReleased(MouseEvent e) {
    }

    @Override
    public void mouseEntered(MouseEvent e) {
    }

    @Override
    public void mouseExited(MouseEvent e) {
    }

    // ---------------- END User Inputs ------------------------------

    private void setImageList() {
        imageList = new ArrayList<Image>();

        imageList.add(ReadImage("/resources/arrowLeft.png"));
        imageList.add(ReadImage("/resources/arrowRight.png"));
        imageList.add(ReadImage("/resources/arrowUp.png"));
        imageList.add(ReadImage("/resources/arrowDown.png"));
    }

    public Image ReadImage(String file_path) {
        try {
            return ImageIO.read(getClass().getResourceAsStream(file_path));
        } catch (IOException e) {
            return null;
        }
    }

    public void paint(Graphics g) {
        super.paint(g);

        setControllers(g);
        setControlArrows(g);
    }

    private void setControllers(Graphics g) {

        for (int i = 0; i < control_position.length; i += 2) {
            g.setColor(new Color(183, 28, 28));
            g.fillOval(425, 75, 200, 200);

            g.setColor(new Color(212, 212, 212));
            g.fillRect(control_position[i], control_position[i + 1], 75, 75);

            g.setColor(new Color(147, 147, 147));
            switch (btnPressed) {
                case "a":
                    g.fillRect(30, 135, 75, 75);
                    break;
                case "d":
                    g.fillRect(210, 135, 75, 75);
                    break;
                case "w":
                    g.fillRect(120, 55, 75, 75);
                    break;
                case "s":
                    g.fillRect(120, 215, 75, 75);
                    break;
                case "k":
                    g.setColor(new Color(140, 22, 22));
                    g.fillOval(425, 75, 200, 200);
                    break;

            }
        }
    }

    private void setControlArrows(Graphics g) {
        for (int i = 0; i < control_position.length; i += 2) {
            g.drawImage(imageList.get(counter), control_position[i], control_position[i + 1], null);
            counter++;
        }
        counter = 0;
    }

    public static void main(String[] args) {
        new Controller();
    }
}