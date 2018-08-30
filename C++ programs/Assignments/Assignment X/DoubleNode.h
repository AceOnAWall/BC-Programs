//  @file DoubleNode.h 
 
#ifndef NODE_
#define NODE_

template<class ItemType>
class Node
{
private:
   ItemType        item; // A data item
   Node<ItemType>* next; // Pointer to next node
   Node<ItemType>* previous; // Pointer to previous node
   
public:
   Node();
   Node(const ItemType& anItem);
   Node(const ItemType& anItem, Node<ItemType>* nextNodePtr, Node<ItemType>* previousNodePtr); // Not implemented
   void setItem(const ItemType& anItem);
   void setNext(Node<ItemType>* nextNodePtr);
   void setPrevious(Node<ItemType>* previousNodePtr); // Not implemented
   ItemType getItem() const ;
   Node<ItemType>* getNext() const ;
   Node<ItemType>* getPrevious() const ; // Not implemented
}; // end Node

#include "DoubleNode.cpp"
#endif