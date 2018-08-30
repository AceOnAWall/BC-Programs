/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to test a Balloon object.

public class BalloonTester 
{

	public static void main(String[] args) 
    { 
		Balloon balloon = new Balloon();
		
		//Uses Balloon methods to calculate spherical volume, then prints results.
		System.out.println("Volume: " + balloon.getVolume());
		System.out.println("Expected: 0.0");

		balloon.inflate(2.0);
		System.out.println("Volume: " + balloon.getVolume());
		System.out.println("Expected: 33.510321638291124");

		balloon.inflate(4.0);
		System.out.println("Volume: " + balloon.getVolume());
		System.out.println("Expected: 904.7786842338604");
    }
}