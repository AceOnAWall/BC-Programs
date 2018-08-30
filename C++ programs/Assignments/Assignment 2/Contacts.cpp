#include <iostream>
#include "Contacts.h"
using namespace std;


ContactNode::ContactNode() {
    nextNodePtr = 0;
}
ContactNode::ContactNode(string initName, string initPhoneNum) {
    contactName = initName;
    contactPhoneNum = initPhoneNum;
    nextNodePtr = 0;
}
void ContactNode::InsertAfter(ContactNode *nextNode) {

    ContactNode *temp;
    if(nextNodePtr == 0) {
        nextNodePtr = nextNode;
    }

    else {
        temp = nextNodePtr;

        while(temp != 0)
        {
            temp = temp-> GetNext();
        }
        temp = nextNode;
    }
}
string ContactNode::GetName() const{
    return contactName;
}

string ContactNode::GetPhoneNumber() const{
    return contactPhoneNum;
}

ContactNode* ContactNode::GetNext() {
    return nextNodePtr;
}

void ContactNode::PrintContactNode() {

    ContactNode *temp;

    cout << "Contact Name: " << GetName() << endl;
    cout << "Phone number: " << GetPhoneNumber() << endl << endl;
    if(nextNodePtr!= 0)
        GetNext()-> PrintContactNode();
}