/* 
Author: Wallace, Ryan
Assignment: Programming Assignment One
Course: COMP B12
Section: CRN: 31051
Instructor: Richard Miles
Date submitted: 2017/ 02/ 12
*/

#include <iostream> 
#include <vector>
#include <cstdlib>
using namespace std;

vector<int> jerseyNumbers();
vector<int> playerRatings();
char MenuSelection(); 

char userChoice; 
int playerNum;
int playerRating;
int numToDelete;
int minRateToShow;

int main() {
	
	userChoice = MenuSelection();
	
	while (userChoice != 'q') {
		
		if (userChoice == 'a') {
			
			cout << "Please enter the jersey number: ";
			cin >> playerNum;
			jerseyNumbers.push_back(playerNum);
		}
		
		else if (userChoice == 'd') {
			
			int i = 0;
			cout << "Please enter the jersey to delete: ";
			cin >> numToDelete;
			for (i = 0; i < jerseyNumbers.size(); ++i){
				if (jerseyNumbers.at(i) == numToDelete) {
					jerseyNumbers.erase(jerseyNumbers.begin() + i);
					playerRatings.erase(playerRatings.begin() + i);
				}
			}
		}
			
		else if (userChoice == 'u') {
			
			int i = 0;
			cout << "Please enter the jersey number to update: ";
			cin >> playerNum;
			cout << "Please enter the player's rating: ";
			cin >> playerRating;
			for (i = 0; i < jerseyNumbers.size(); ++i) {
				if (jerseyNumbers.at(i) == playerNum) {
					playerRatings.push_back(playerRating);
				}
			}
		}
		
		else if (userChoice == 'r') {
			
			int i = 1;
			cout << "Please enter minimum rating to be shown";
			cin >> minRateToShow;
			for (i = 1; i <= playerRatings.at(i); ++i) {
				if (playerRatings.at(i) >= minRateToShow) {
					cout << "Players rated above " << minRateToShow << endl;
					cout << "Player " << i << "-- Jersey number: " << jerseyNumbers.at(i) << ", ";
					cout << "Rating: " << playerRatings.at(i) << endl; 
				}
			}
		}
		
		else if (userChoice == 'o') {
			
			int i = 1;
			for (i = 1; i <= jerseyNumbers.size(); ++i) {
				cout << "Player " << i <<" -- Jersey number: " <<  jerseyNumbers.at(i) << ", ";
				cout << "Rating: " << playerRatings.at(i) << endl;
			}
		}
		
		else {
			cout << "Invalid option please select again.";
			userChoice = MenuSelection();
		}
		
	userChoice = MenuSelection();
	}
}

// FUNCTION DEFINITIONS

char MenuSelection() {
	
	char userSelection;
	
	cout << "MENU" << endl;
	cout << "a - Add player's jersey number" << endl;
	cout << "d - Remove player's information" << endl;
	cout << "u - Update player's rating" << endl;
	cout << "r - Output players above a certain rating" << endl;
	cout << "o - Output roster" << endl;
	cout << "q - Quit\n" << endl;

	cout << "Choose an option: ";
	cin >> userSelection;
	return userSelection;
}