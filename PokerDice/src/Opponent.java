
public class Opponent extends Player {
	
	
	
	public int oppLogic(){
		
		
			if(hasMulti() == 31){
				if(checkStraight() == 15 || checkStraight() == 20){
					return 0;
				}
				else {
					goForStraight(findOne());
				}
			}
			else if(hasMulti() == 0){
				return 0;
			}
			else {
				goForPairs(hasMulti());
			}
			return 0;
	}
	public int hasMulti() {
		// return an integer such that its binary representation would show which
		// dice to re-roll. A one represents a die that should be re-rolled. The
		// leftmost die is d1 and the rightmost die is d2.
		// if 31 is returned there are no multiples
		// if 0 is returned there is a yahtzee or full house
		
		int value=0;
		
		if(d1.getFaceValue() != d2.getFaceValue()  && d1.getFaceValue() != d3.getFaceValue() && d1.getFaceValue() != d4.getFaceValue() && d1.getFaceValue() != d5.getFaceValue()){
			value += 16;
		}
		if(d2.getFaceValue() != d1.getFaceValue()  && d2.getFaceValue() != d3.getFaceValue() && d2.getFaceValue() != d4.getFaceValue() && d2.getFaceValue() != d5.getFaceValue()){			value += 8;
			//System.out.println("d2");
		}
		if(d3.getFaceValue() != d1.getFaceValue()  && d3.getFaceValue() != d2.getFaceValue() && d3.getFaceValue() != d4.getFaceValue() && d3.getFaceValue() != d5.getFaceValue()){
			value += 4;
			//System.out.println("d3");
		}
		if(d4.getFaceValue() != d1.getFaceValue()  && d4.getFaceValue() != d2.getFaceValue() && d4.getFaceValue() != d3.getFaceValue() && d4.getFaceValue() != d5.getFaceValue()){
			value += 2;
		}
		if(d5.getFaceValue() != d1.getFaceValue()  && d5.getFaceValue() != d2.getFaceValue() && d5.getFaceValue() != d3.getFaceValue() && d5.getFaceValue() != d4.getFaceValue()){
			value += 1;
		}
		return value;
	}
	//if there are no multiples, check for a straight
	//if value is 15 or 20 then opponent has a straight
	//otherwise, find the one and re-roll it
	public int checkStraight(){
		return (d1.getFaceValue() + d2.getFaceValue() + d3.getFaceValue() + d4.getFaceValue() + d5.getFaceValue());
	}
	//find the one for goForStraight()
	//if zero is returned, there is a straight from 2-6
	public int findOne(){
		if (d1.getFaceValue() == 1)
			return 1;
		if (d2.getFaceValue() == 1)
			return 2;
		if (d3.getFaceValue() == 1)
			return 3;
		if (d4.getFaceValue() == 1)
			return 4;
		if (d5.getFaceValue() == 1)
			return 5;
		else
			return 0;

	}
	
	//if there are no pairs and opponent has a one and a six, opponent will re-roll the one.
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
	
	public void goForPairs(int value) {
		//re-roll the dice represented in the binary value
		if((value % 2) == 1){
			d5.roll();
		}
		value /= 2;
		if((value % 2) == 1){
			d4.roll();
		}
		value /= 2;
		if((value % 2) == 1){
			d3.roll();
		}
		value /= 2;
		if((value % 2) == 1){
			d2.roll();
		}
		value /= 2;
		if((value % 2) == 1){
			d1.roll();
		}
	}
	
}
