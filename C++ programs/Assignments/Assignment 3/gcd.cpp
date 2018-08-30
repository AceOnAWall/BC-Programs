/* 
Author: Wallace, Ryan
Assignment: Programming Assignment Three
Course: COMP B12
Section: CRN: 31051
Instructor: Richard Miles
Date submitted: 2017/04/16
*/


class gcd {
	int num1;
	int num2;
	
	public:
		int getGCD(int,int);
};

gcd::gcd(){
	x = 0;
	y = 0;
}

gcd::getGCD(int x, int y){
	
	if(y == 0){
	   return x;
    }
   
	else if(y != 0){
	   return gcd(y, x % y);
    }
}