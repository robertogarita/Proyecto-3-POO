package mvc;

import javax.swing.JFrame;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import sockets.Client;

public class Screen extends JFrame implements MouseListener{

    Client clientScreen;
    public Screen(){
        
        setVisible(true);
        setSize(500,500);
        addMouseListener(this);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        clientScreen = new Client(6000, null);
        Thread t = new Thread(clientScreen);
        t.start();
    }

    @Override
    public void mousePressed(MouseEvent e) {
        // TODO Auto-generated method stub

    }

    @Override
    public void mouseReleased(MouseEvent e) {
        // TODO Auto-generated method stub

    }

    @Override
    public void mouseEntered(MouseEvent e) {
        // TODO Auto-generated method stub

    }

    @Override
    public void mouseExited(MouseEvent e) {
        // TODO Auto-generated method stub

    }
    
    public static void main(String[] args) {
        new Screen();
    }
}
