public class MinOppgave2 {
	
	//Oppgavetekst:
	//Lag et program som skriver ut de 25 f�rste tallene i Fibonaccis tallrekke ved hjelp av flere metoder og ingen l�kker.
	
	public static void main(String[] args) {
		
		int ant = 1;
		int tall2 = 0;
		int tall3 = 1;
		int tall4 = 1;
		
		System.out.println("1"); //Litt juks her, men programmet skiver ikke 1 to ganger
		
		regnNeste(ant, tall2, tall3, tall4);
	}
	
	static void kjor(int ant, int t2, int t3, int t4 ){
		ant ++;
		
		if (ant <= 25){
			System.out.println(t3);
			regnNeste(ant, t2, t3, t4);
		}
		
		else {
			System.out.println("Og det var det.");
		}
	}
	
		
	static void regnNeste(int ant, int t2, int t3, int t4){
		t4 = t3;
		t3 = t3 + t2;
		t2 = t4;
		
		kjor(ant, t2, t3, t4);
	}
}
