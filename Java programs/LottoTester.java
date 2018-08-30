/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to test a LotteryPrinter object. 

public class LottoTester
{
	public static void main(String[] args)
	{
		// Generates 6 random numbers. 
		LotteryPrinter ticket = new LotteryPrinter();
		int num1 = ticket.getLottoNum();
		int num2 = ticket.getLottoNum();
		int num3 = ticket.getLottoNum();
		int num4 = ticket.getLottoNum();
		int num5 = ticket.getLottoNum();
		int num6 = ticket.getLottoNum();
		
		// Prints the previously generates numbers. 
		System.out.println("Play this combination, " +
			num1 + " " + num2 + " " + num3 + " " +
			num4 + " " + num5 + " " + num6 + " " +
			"it'll make you rich!");	
	}
}