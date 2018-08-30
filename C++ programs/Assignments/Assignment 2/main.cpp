  cin >> name;

    cout << "Enter phone number: " << endl;
    cin >> phoneNum;

    cout << "You entered: " << name << ", " << phoneNum << endl;
    node1 = new ContactNode(name, phoneNum);
    headContact->InsertAfter(node1);

    cout << "Person 2" << endl;
    cout << "Enter name: " << endl;
    cin >> name;

    cout << "Enter phone number: " << endl;
    cin >> phoneNum;

    cout << "You entered: " << name << ", " << phoneNum << endl;
    node2 = new ContactNode(name, phoneNum);
    node1->InsertAfter(node2);

    cout << "Person 3" << endl;
    cout << "Enter name: " << endl;
    cin >> name;

    cout << "Enter phone number: " << endl;
    cin >> phoneNum;

    cout << "You entered: " << name << ", " << phoneNum << endl;
    node3 = new ContactNode(name, phoneNum);
    node2->InsertAfter(node3);


    cout << "CONTACT LIST" << endl;
    currentContact = headContact;
    while(currentContact != 0) {
        currentContact->PrintContactNode();
        currentContact = currentContact->GetNext();
    }

    return 0;
}