package games;



public class JuegoDePrueba {

    private int PosX;
    private int PosY;
    private String filePath;
    private int ObstaculesSquare1[], ObstaculesLine1[];
    private int ObstaculesSquare2[], ObstaculesLine2[];
    private int ObstaculesSquare3[], ObstaculesLine3[];
    private int ObstaculesSquare4[], ObstaculesLine4[];

    public JuegoDePrueba(int PosX, int PosY, int[] ObsSquare1, int[]ObsLine1,
    int[] ObsSquare2, int[]ObsLine2, int[] ObsSquare3, int[]ObsLine3,
    int[] ObsSquare4, int[]ObsLine4, String filePath){

        this.PosX = PosX;
        this.PosY = PosY;
        this.ObstaculesSquare1 = ObsSquare1;
        this.ObstaculesLine1 = ObsLine1;
        this.ObstaculesSquare2 = ObsSquare2;
        this.ObstaculesLine2 = ObsLine2;
        this.ObstaculesSquare3 = ObsSquare3;
        this.ObstaculesLine3 = ObsLine3;
        this.ObstaculesSquare4 = ObsSquare4;
        this.ObstaculesLine4 = ObsLine4;
        this.filePath = filePath;
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
    public void getEnemies(){}
    
    public String getfilePath(){
        return filePath;
    }

    //----------------------Getter de limite del mapa

    public int[] getObstaculesSquare1(){
        return ObstaculesSquare1;
    }
    public int[] getObstaculesLine1(){
        return ObstaculesLine1;
    }

    public int[] getObstaculesSquare2(){
        return ObstaculesSquare2;
    }
    public int[] getObstaculesLine2(){
        return ObstaculesLine2;
    }

    public int[] getObstaculesSquare3(){
        return ObstaculesSquare3;
    }
    public int[] getObstaculesLine3(){
        return ObstaculesLine3;
    }

    public int[] getObstaculesSquare4(){
        return ObstaculesSquare4;
    }
    public int[] getObstaculesLine4(){
        return ObstaculesLine4;
    }
    
}
