/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to represent a car. 

public class Car
{
	// Creates variables for MPG and fuel in the tank. 
	private double milesPerGal;
	private double fuelInTank = 0.0;
	
	// Constructor takes the MPG at initialization.
	public Car(double amount)
	{
		milesPerGal = amount;
	}
	
	// Adds gas to the fuel tank. 
	public void addGas(int gallons)
	{
		fuelInTank = gallons;
	}
	
	// Removes gas from the tank with regards to MPG. 
	public void drive(int miles)
	{
		fuelInTank = fuelInTank -(miles/milesPerGal); 
	}
	
	// Returns the current amount of gas in the fuel tank. 
	public double getGasInTank()
	{
		return fuelInTank;
	}
}