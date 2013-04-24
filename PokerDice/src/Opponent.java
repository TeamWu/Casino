
public class Opponent extends Player {
	
	
	
	
	public int hasMulti() {
		// return an integer such that its binary representation would show which
		// dice to re-roll. A one represents a die that should be re-rolled. The
		// leftmost die is d1 and the rightmost die is d2.
		
		int value=0;
		
		if(!d1.equals(d2) && !d1.equals(d3) && !d1.equals(d4) && !d1.equals(d5))
			value += 16;
		if(!d2.equals(d1) && !d2.equals(d3) && !d2.equals(d4) && !d2.equals(d5))
			value += 8;
		if(!d3.equals(d1) && !d3.equals(d2) && !d3.equals(d4) && !d3.equals(d5))
			value += 4;
		if(!d4.equals(d1) && !d4.equals(d2) && !d4.equals(d3) && !d4.equals(d5))
			value += 2;
		if(!d5.equals(d1) && !d5.equals(d2) && !d5.equals(d3) && !d5.equals(d4))
			value += 1;
		return value;
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
		//roll just the die that was passed in
		if (die1 == 1){
			d1.roll();
		}
		
		if(die1 == 2){
			d2.roll();
		}
		
		if(die1 == 3){
			d3.roll();
		}
		
		if(die1 == 4){
			d4.roll();
		}
		
		if(die1 == 5){
			d5.roll();
		}
		
		
	}
	public void goForPairs(int die1, int die2) {
		//roll the first die
		if (die1 == 1){
			d1.roll();
		}
		
		if(die1 == 2){
			d2.roll();
		}
		
		if(die1 == 3){
			d3.roll();
		}
		
		if(die1 == 4){
			d4.roll();
		}
		
		if(die1 == 5){
			d5.roll();
		}
		//roll the second die
		if (die2 == 1){
			d1.roll();
		}
		
		if(die2 == 2){
			d2.roll();
		}
		
		if(die2 == 3){
			d3.roll();
		}
		
		if(die2 == 4){
			d4.roll();
		}
		
		if(die2 == 5){
			d5.roll();
		}
		
		
	}

	public void goForPairs(int die1, int die2, int die3) {
		//roll the first die
				if (die1 == 1){
					d1.roll();
				}
				
				if(die1 == 2){
					d2.roll();
				}
				
				if(die1 == 3){
					d3.roll();
				}
				
				if(die1 == 4){
					d4.roll();
				}
				
				if(die1 == 5){
					d5.roll();
				}
				//roll the second die
				if (die2 == 1){
					d1.roll();
				}
				
				if(die2 == 2){
					d2.roll();
				}
				
				if(die2 == 3){
					d3.roll();
				}
				
				if(die2 == 4){
					d4.roll();
				}
				
				if(die2 == 5){
					d5.roll();
				}
				//roll the third die
				if (die3 == 1){
					d1.roll();
				}
				
				if(die3 == 2){
					d2.roll();
				}
				
				if(die3 == 3){
					d3.roll();
				}
				
				if(die3 == 4){
					d4.roll();
				}
				
				if(die3 == 5){
					d5.roll();
				}
		
		
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
