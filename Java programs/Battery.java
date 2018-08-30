/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to represent a rechargable battery.

public class Battery
{
	// Creates two variables to hold charges.
	private double startingCapacity;
	private double workingCapacity;
	
	// Constructor
	public Battery(double capacity)
	{
		startingCapacity = capacity;
		workingCapacity = capacity;
	}
	
	// Lowers the battery capacity.
	public void drain(double amount)
	{
		workingCapacity = workingCapacity - amount;
	}
	
	// Increases the battery capacity. 
	public void charge()
	{
		workingCapacity = startingCapacity;
	}
	
	// Returns the original battery capacity.
	public double getRemainingCapacity()
	{
		return workingCapacity;
	}
}