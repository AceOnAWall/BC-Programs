/* 
Author: Wallace, Ryan
Assignment: Programming Assignment Three
Course: COMP B12
Section: CRN: 31051 (MoWe)
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

	cout << "Please enter the first number :";
	cin >> x;
  
	cout << "Please enter the second number :";
	cin >> y;
  
	number = gcd(x, y);

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