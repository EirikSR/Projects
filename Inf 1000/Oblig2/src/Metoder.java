import java.util.Scanner;
public class Metoder {

	public static void main(String[] args) {
		skrivUt();
		skrivUt();
		skrivUt();
		//Oppgave a ville v�rt � flutte metoden skrivUt inn hit.
	}
	
	static void skrivUt(){
		Scanner input = new Scanner(System.in);
		System.out.println("Hva heter du?");
		String navn = input.nextLine();
		System.out.println("Hvor bor du?");
		String bosted = input.nextLine();
		System.out.println("Hei " + navn + "! Du er fra " + bosted + "!");
		
	}
}
