import java.util.Scanner;

public class Bondegard {

	
	public static void main(String[] args) {
		Gris[] grisebinge = new Gris[10];
		Hest[] stall = new Hest[5];
		Ku[] fjos = new Ku[30];
		String type = null;
		int antall = 0;
		
		
		
		settInnGris(grisebinge, 5);
		settInnHest(stall, 2);
		settInnKu(fjos, 8);
		
		
		
		type = "gris";
		antall = 3;
		selgDyr(type, antall, grisebinge, stall, fjos);
		
		type = "hest";
		antall = 1;
		selgDyr(type, antall, grisebinge, stall, fjos);
		
		type = "ku";
		antall = 5;
		selgDyr(type, antall, grisebinge, stall, fjos);
		
		// skrivUt(grisebinge, stall, fjos);
		
		printValg();
		Scanner input = new Scanner(System.in);
		int action = Integer.parseInt(input.nextLine());
		
		while (action != 0){
			
			if (action == 1){
				settInnGris(grisebinge, 1);
				System.out.println("gjort");
				action = Integer.parseInt(input.nextLine());
			}
			
			if (action == 2){
				settInnHest(stall, 1);
				System.out.println("gjort");
				action = Integer.parseInt(input.nextLine());
			}
			
			if (action == 3){
				settInnKu(fjos, 1);
				System.out.println("gjort");
				action = Integer.parseInt(input.nextLine());
			}
			
			if (action == 4){
				printValg1();
				int action2 = Integer.parseInt(input.nextLine());
				
				while (action2 != 0){
					
					if (action2 == 1){
						selgDyr("gris", 1, grisebinge, stall, fjos);
						System.out.println("gjort");
						action2 = Integer.parseInt(input.nextLine());
					}
					
					if (action2 == 2){
						selgDyr("hest", 1, grisebinge, stall, fjos);
						System.out.println("gjort");
						action2 = Integer.parseInt(input.nextLine());
					}
					
					if (action2 == 3){
						selgDyr("ku", 1, grisebinge, stall, fjos);
						System.out.println("gjort");
						action2 = Integer.parseInt(input.nextLine());
					}
					
					else {
						action2 = Integer.parseInt(input.nextLine());
					}
				}
				
				printValg();
			}
			
			if (action == 5){
				skrivUt(grisebinge, stall, fjos);
				printValg();
				action = Integer.parseInt(input.nextLine());
			}
			else {
				action = Integer.parseInt(input.nextLine());
			}
			
		}
	}
	
	static void settInnGris(Gris[] grisebinge, int antall) {
		
		for(int i = 0; antall != 0; i++){
			if(grisebinge[i] == null){
				grisebinge[i] = new Gris();
				antall--;
			}
		}
		
	}
	
	static void settInnHest(Hest[] stall, int antall){
		for(int i = 0; antall != 0; i++){
			if(stall[i] == null){
				stall[i] = new Hest();
				antall--;
			}
			
		}		
	}
	
	static void settInnKu(Ku[] fjos, int antall){
		for(int i = 0; antall != 0; i++){
			if(fjos[i] == null){
				fjos[i] = new Ku();
				antall--;
			}
		}
	}
	
	static void selgDyr(String type, int antall, Gris[] g, Hest[] h, Ku[] k){
		
		if(type.equals("gris")){
			for(int i = g.length-1; antall != 0; i--){
				if(i == -1){
					System.out.println("Ingen flere griser");
					antall = 0;
				}
				else if(g[i] != null){
					g[i] = null;
					antall--;
				}
			}
		}
		
		if(type.equals("hest")){
			for(int i = h.length-1; antall != 0; i--){
				if(i == -1){
					System.out.println("Ingen flere hester");
					antall = 0;
				}
				else if(h[i] != null){
					h[i] = null;
					antall--;
				}
			}
		}
		
		if(type.equals("ku")){
			for(int i = k.length-1; antall != 0; i--){
				if(i == 0){
					System.out.println("Ingen flere kuer");
					antall = 0;
				}
				else if(k[i] != null){
					k[i] = null;
					antall--;
				}
			}
		}
	}
	
	static void skrivUt(Gris[] g, Hest[] h, Ku[] k){
		
		for(int i = 0; i < g.length; i++){
			if(g[i] != null){ System.out.println(g[i]);}
		}
		
		for(int i = 0; i < h.length; i++){
			if(h[i] != null){ System.out.println(h[i]);}
		}
		
		for(int i = 0; i < k.length; i++){
			if(k[i] != null){ System.out.println(k[i]);}
		}
	}	
	
	static void printValg(){
		System.out.println("Velg en kommando:");
		System.out.println("0: Avslutt");
		System.out.println("1: Sett inn en gris");
		System.out.println("2: Sett inn en hest");
		System.out.println("3: Sett inn en ku");
		System.out.println("4: Selg et dyr");
		System.out.println("5: Skriv ut bondeg?rden");
	}
	
	static void printValg1(){
		System.out.println("Velg hvilket dyr som skal selges:");
		System.out.println("0: Ingen");
		System.out.println("1: Gris");
		System.out.println("2: Hest");
		System.out.println("3: Ku");
	}
}
