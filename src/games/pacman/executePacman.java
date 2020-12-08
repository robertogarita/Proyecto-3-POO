package games.pacman;

import javax.swing.JFrame;

public class executePacman extends JFrame{
    
    public executePacman(){
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setSize(500,500);
        this.setVisible(true);
        this.add(new MainPacman());
    }

    public static void main(String[] args) {
        new executePacman();
    }
}
