/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to represent an inflatable spherical balloon.


public class Balloon
{
	// Sets the radius of the balloon to 0. 
	private double radius;
	
	// Constructor 
	public Balloon()
	{
		radius = 0.0;
	}
	
	// Changes radius to whatever amount is given by user.
	public void inflate(double amount)
	{
		radius += amount;
	}
	
	// Evaluates and returns the volume of the balloon.
	public double getVolume()
	{
		double volume = (4 * Math.PI * Math.pow(radius, 3)) / 3;
		return volume;
	}
}