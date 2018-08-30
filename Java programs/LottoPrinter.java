/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to represent a lotto ticket creator. 

// Imports the Random class from the Java API. 
import java.util.Random;

public class LotteryPrinter
{
	// Constructor
	public LotteryPrinter()
	{
	}
	
	// Generates a random number from 1 to 49, then returns the value. 
	public int getLottoNum()
	{
		Random rand = new Random();
		int randNum = rand.nextInt(49) + 1;
		return randNum;
	}
}