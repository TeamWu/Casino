
public class Opponent extends Player {
	
	private int strategy = getStrategy();
	
	
	public int getStrategy() {
		strategy = (int)(Math.random() * 3) + 1;
		return strategy;
	}
	
	public void goForStraight(int One) {
		if (One == 1){
			d1.roll();
		}
		
		if(One == 2){
			d2.roll();
		}
		
		if(One == 3){
			d3.roll();
		}
		
		if(One == 4){
			d4.roll();
		}
		
		if(One == 5){
			d5.roll();
		}
		
	}
	
	public void goForPairs(int die1) {
		
		
		
	}
	public void goForPairs(int die1, int die2) {
		
		
		
	}

	public void goForPairs(int die1, int die2, int die3) {
		
		
		
	}
	public void goForFullHouse(int die) {
		if (die == 1){
			d1.roll();
		}
		
		if(die == 2){
			d2.roll();
		}
		
		if(die == 3){
			d3.roll();
		}
		
		if(die == 4){
			d4.roll();
		}
		
		if(die == 5){
			d5.roll();
		}
		
		
	}


}
