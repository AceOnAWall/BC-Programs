/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to represent a changing roach population.

public class RoachPopulation
{
	// Creates a variable for the roach population.
	private double population;
	
	// Constructor
	public RoachPopulation(double amount)
	{
		population = amount;
	}
	
	// Doubles the roach population.
	public void breed()
	{
		population += population;
	}
	
	// Decreases the roach population by a given percent. 
	public void spray(double percent)
	{
		population = population - (population * (percent / 100));
	}
	
	// Returns the current roach population.
	public double getRoaches()
	{
		return population;
	}
}