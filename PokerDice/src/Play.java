import java.util.Scanner;

public class Play {
	
	static Scanner keyboard = new Scanner(System.in);

	
	public static void main(String[] args) {
		Player player1 = new Player();
		int numberOf = NumberOfOpponents();
		int nOpps = numberOf - 1;
		//System.out.println(nOpps);
		
		Player[] opponent = new Player[numberOf];
		for (int j = 0; j < opponent.length; j++){
				opponent[j] = new Player();
		}
		
		firstRoll(nOpps, player1, opponent);
		secondThirdRolls(nOpps, player1, opponent);
		secondThirdRolls(nOpps, player1, opponent);
		
	}
	
	public static int NumberOfOpponents() {
		int nPlayers;
		System.out.println("How many opponents? (1-3) ");
		while(!keyboard.hasNextInt()){
			System.out.println("Please try again.");
			System.out.println("How many opponents? (1-3) ");
			keyboard.nextLine();
		}
		nPlayers = keyboard.nextInt();
		while(nPlayers != 1 && nPlayers != 2 && nPlayers != 3){
			System.out.println("Please try again.");
			System.out.println("How many opponents? (1-3)");
			nPlayers = keyboard.nextInt();
			keyboard.nextLine();
		}
		
		return nPlayers;
	}
	public static void firstRoll(int nOpps, Player player1, Player opponent[]) {
		
		//player1.d1.roll();
		//player1.d2.roll();
		//player1.d3.roll();
		//player1.d4.roll();
		//player1.d5.roll();
		System.out.println("  Player 1: " + player1.d1.roll() + player1.d2.roll() + player1.d3.roll() + player1.d4.roll() + player1.d5.roll());
		//System.out.println("Player 1: " + player1.d1.roll() + player1.d2.roll() + player1.d3.roll() + player1.d4.roll() + player1.d5.roll());
		//System.out.println("Player 1: " + player1.d1.getFaceValue() + player1.d2.getFaceValue() + player1.d3.getFaceValue() + player1.d4.getFaceValue() + player1.d5.getFaceValue());
		//System.out.println("Player 1: " + player1.d1.getFaceValue() + player1.d2.getFaceValue() + player1.d3.getFaceValue() + player1.d4.getFaceValue() + player1.d5.getFaceValue());
		
		
		for(int x = 0; x <= nOpps; x++) {
			int number = x + 1;
			System.out.println("Opponent " + number + ": "  + opponent[nOpps].d1.roll() + opponent[nOpps].d2.roll() + opponent[nOpps].d3.roll() + opponent[nOpps].d4.roll() + opponent[nOpps].d5.roll());
			
			}
	}
	public static void secondThirdRolls(int nOpps, Player player1, Player opponent[]) {
		
		String reRollCheck = "";
		
		System.out.println("Would you like to re-roll any of your dice? (y/n) ");
		reRollCheck = keyboard.next();
		keyboard.nextLine();
		while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
			System.out.println("Please press 'y' for yes or 'n' for no: ");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
		}
		if(reRollCheck.equalsIgnoreCase("y")){
			//check die 1
			System.out.println("Would you like to re-roll die #1? (y/n)");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
			while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
				System.out.println("Please press 'y' for yes or 'n' for no: ");
				reRollCheck = keyboard.next();
				keyboard.nextLine();
			}
			if(reRollCheck.equalsIgnoreCase("y")){
				player1.d1.roll();
			}
			//check die 2
			System.out.println("Would you like to re-roll die #2? (y/n)");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
			while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
				System.out.println("Please press 'y' for yes or 'n' for no: ");
				reRollCheck = keyboard.next();
				keyboard.nextLine();
			}
			if(reRollCheck.equalsIgnoreCase("y")){
				player1.d2.roll();
			}
			//check die 3
			System.out.println("Would you like to re-roll die #3? (y/n)");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
			while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
				System.out.println("Please press 'y' for yes or 'n' for no: ");
				reRollCheck = keyboard.next();
				keyboard.nextLine();
			}
			if(reRollCheck.equalsIgnoreCase("y")){
				player1.d3.roll();
			}
			//check die 4
			System.out.println("Would you like to re-roll die #4? (y/n)");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
			while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
				System.out.println("Please press 'y' for yes or 'n' for no: ");
				reRollCheck = keyboard.next();
				keyboard.nextLine();
			}
			if(reRollCheck.equalsIgnoreCase("y")){
				player1.d4.roll();
			}
			//check die 5
			System.out.println("Would you like to re-roll die #5? (y/n)");
			reRollCheck = keyboard.next();
			keyboard.nextLine();
			while (!reRollCheck.equalsIgnoreCase("y") && !reRollCheck.equalsIgnoreCase("n")){
				System.out.println("Please press 'y' for yes or 'n' for no: ");
				reRollCheck = keyboard.next();
				keyboard.nextLine();
			}
			if(reRollCheck.equalsIgnoreCase("y")){
				player1.d5.roll();
			}
		}
	
		
		
		System.out.println("  Player 1: " + player1.d1.getFaceValue() + player1.d2.getFaceValue() + player1.d3.getFaceValue() + player1.d4.getFaceValue() + player1.d5.getFaceValue());
		
		
		/*for(int x = 0; x <= nOpps; x++) {
			int number = x + 1;
			System.out.println("Opponent " + number + ": "  + opponent[nOpps].d1.roll() + opponent[nOpps].d2.roll() + opponent[nOpps].d3.roll() + opponent[nOpps].d4.roll() + opponent[nOpps].d5.roll());
			
			}*/
	}

}
