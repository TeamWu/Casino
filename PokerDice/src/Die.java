public class Die {
	
	private int faceValue;
	
	public Die() {
		faceValue = 1;
	}
	
	public int roll() {
		faceValue = (int)(Math.random() * 6) + 1;
		return faceValue;
	}

	public void setFaceValue (int value) {
		faceValue = value;
	}

	public int getFaceValue() {
		return faceValue;
	}

	public String toString() {
		String result = Integer.toString(faceValue);
		return result;
		}
}
