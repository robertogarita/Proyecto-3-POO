package games.pacman;

import java.awt.Color;
import javax.swing.JPanel;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class MainPacman extends JPanel implements KeyListener {

    private int PosX = 50;
    private int PosY = 50;

    public MainPacman() {

        this.setBackground(new Color(0, 8, 40));
        this.setFocusable(true);

        repaint();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;
    }

    // -------------------USER INPUTS----------------------------

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }

        // -------------------END USER INPUTS----------------------------
    
}
