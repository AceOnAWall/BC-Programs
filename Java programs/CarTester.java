/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to test a Car object. 
  
public class CarTester
{ 
	public static void main(String[] args)
	{ 
		// Makes changes to the Car object then prints the final values. 
		Car myHybrid = new Car(50); // 50 miles per gallon 
		myHybrid.addGas(20); 
		myHybrid.drive(100); // consumes 2 gallons   
		double gasLeft = myHybrid.getGasInTank(); 
		System.out.print("You have " + gasLeft + " gallons left in your tank.");
	} 
}