
public class Opponent extends Player {
	
	private int strategy = getStrategy();
	
	
	public int getStrategy() {
		strategy = (int)(Math.random() * 3) + 1;
		return strategy;
	}
	
	public void goForStraight() {
		
		
		
	}
	
	public void goForFive() {
		
		
		
	}
	
	public void goForFullHouse() {
		
		
		
	}


}
