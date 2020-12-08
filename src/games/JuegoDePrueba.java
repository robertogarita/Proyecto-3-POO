package games;

public class JuegoDePrueba {

    private int PosX;
    private int PosY;

    public JuegoDePrueba(int PosX, int PosY){
        this.PosX = PosX;
        this.PosY = PosY;
    }


    //-------------------Getter y Setter-------------------

    public int getPosX(){
        return PosX;
    }
    public void setPosX(int PosX){
        this.PosX = PosX;
    }
    public int getPosY(){
        return PosY;
    }
    public void setPosY(int PosY){
        this.PosY = PosY;
    }
    
}
