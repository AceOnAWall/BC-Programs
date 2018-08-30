/* 
Author: Wallace, Ryan
Assignment: Programming Assignment Three
Course: COMP B12
Section: CRN: 31051
Instructor: Richard Miles
Date submitted: 2017/04/16
*/


#include <iostream>
using namespace std;

int gcd(int x, int y);

int main(){
	int x;
	int y;
	int number;

	//cout << "Please enter the first number :";
	//cin >> x;
	//cout << "Please enter the second number :";
	//cin >> y;
	//number = gcd(x, y);
	//cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	

	//Testing two large numbers
	x = 999999;
	y = 123456;
	number = gcd(x,y);
	cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	
	//Testing 0 and a prime number
	x = 17;
	y = 0;
	number = gcd(x,y);
	cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	
	//Testing a large and small number
	x = 50;
	y = 15;
	number = gcd(x,y);
	cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	
	//Testing a number that is the gcd
	x = 8;
	y = 16;
	number = gcd(x,y);
	cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	
	//Testing two of the same numbers
	x = 3;
	y = 3;
	number = gcd(x,y);
	cout << "The greatest common denominator of " << x << " and " << y << " is " << number << endl;
	
	return 0;
}

int gcd(int x, int y){
	
   if(y == 0){
	   return x;
   }
   
   else if(y != 0){
	   return gcd(y, x % y);
   }
}