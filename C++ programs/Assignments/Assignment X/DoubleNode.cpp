//@file DoubleNode.cpp 

#include "DoubleNode.h"
//#include <cstddef>

template<class ItemType>
Node<ItemType>::Node() : next(nullptr) , previous(nullptr)
{
} // end default constructor

template<class ItemType>
Node<ItemType>::Node(const ItemType& anItem) : item(anItem), next(nullptr), previous(nullptr)
{
} // end constructor

template<class ItemType>
Node<ItemType>::Node(const ItemType& anItem, Node<ItemType>* nextNodePtr, Node<ItemType>* previousNodePtr) :
                item(anItem), next(nextNodePtr), previous(previousNodePtr)
{
} // end constructor
// new constructor with additional argument, previous node ptr.

template<class ItemType>
void Node<ItemType>::setItem(const ItemType& anItem)
{
   item = anItem;
} // end setItem

template<class ItemType>
void Node<ItemType>::setNext(Node<ItemType>* nextNodePtr)
{
   next = nextNodePtr;
} // end setNext

template<class ItemType>
void Node<ItemType>::setPrevious(Node<ItemType>* previousNodePtr)
{
   previous = previousNodePtr;
} // end setPrevious
// New method, sets previous node ptr

template<class ItemType>
ItemType Node<ItemType>::getItem() const
{
   return item;
} // end getItem

template<class ItemType>
Node<ItemType>* Node<ItemType>::getNext() const
{
   return next;
} // end getNext

template<class ItemType>
Node<ItemType>* Node<ItemType>::getPrevious() const
{
   return previous;
} // end getPrevious
// New method, returns the previous node location
