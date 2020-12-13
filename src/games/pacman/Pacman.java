package games.pacman;

import games.JuegoDePrueba;

public class Pacman extends JuegoDePrueba{

	private static int square1[] = {3,3,10,4,3,10,10,3,13,3,21,10,1,16,12,8,16,19,21,1,18,23,24,1};
	private static int square2[] = {28,3,36,10,39,3,46,4,39,10,46,3,37,16,48,8,28,19,33,1,25,23,31,1};
	private static int square3[] = {18,25,24,4,3,27,15,1,7,29,15,3,1,32,2,2,1,35,4,1,7,35,21,1,3,39,15,1,11,41,15,1,3,43,15,3,18,45,21,1};
	private static int square4[] = {25,25,31,4,34,27,46,1,34,29,41,3,46,32,48,2,44,35,48,1,28,35,41,1,34,39,46,1,34,41,38,1,34,43,46,3,28,45,31,1};
	private static int line1[] = {24,1,24,13,15,16,15,24,18,16,24,16,24,16,24,20};
	private static int line2[] = {25,16,31,16,34,16,34,24,25,1,25,13,25,16,25,20};
	private static int line3[] = {1,31,4,31,18,32,24,32,24,33,24,36,18,39,24,39,24,40,24,46,16,42,21,42,21,43,21,44};
	private static int line4[] = {44,31,48,31,26,32,31,32,25,32,25,36,26,39,31,39,28,42,33,42,28,43,28,44,25,39,25,46};

	public Pacman(int PosX, int PosY, String filePath) {
		super(PosX, PosY, square1,line1, square2,line2, square3,line3, square4,line4, filePath);
	}
}
