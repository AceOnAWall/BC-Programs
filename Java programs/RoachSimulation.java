/* 
Author: Wallace, Ryan
Group members: Leiva, Zaira; Eason, Tyrus; Enger, Robert; Wallace, Ryan
Assignment: Programming Assignment Two
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/09/22
*/

// A class to test a RoachPopulation object.

public class RoachSimulation
{
	public static void main(String[] args)
	{
		RoachPopulation testRoachPopulation = new RoachPopulation(10.0);
		
		// Uses the RoachPopulation methods to change the population value, then prints results. 
		testRoachPopulation.breed();
		testRoachPopulation.spray(10);
		System.out.printf("Current population: %.2f\n", testRoachPopulation.getRoaches());
		
		testRoachPopulation.breed();
		testRoachPopulation.spray(10);
		System.out.printf("Current population: %.2f\n", testRoachPopulation.getRoaches());
		
		testRoachPopulation.breed();
		testRoachPopulation.spray(10);
		System.out.printf("Current population: %.2f\n", testRoachPopulation.getRoaches());
	}
}