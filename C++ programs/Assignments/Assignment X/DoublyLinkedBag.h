
/** ADT bag: Doubly Link-based implementation.
    @file Doubly LinkedBag.h 
    Listing 4-3 */
#ifndef LINKED_BAG_
#define LINKED_BAG_

#include "DoubleBagInterface.h"
#include "DoubleNode.h"

template<class ItemType>
class LinkedBag : public BagInterface<ItemType>
{
private:
   Node<ItemType>* headPtr; // Pointer to first node
   Node<ItemType>* tailPtr; // Pointer to last node
   int itemCount;           // Current count of bag items
   
   // Returns either a pointer to the node containing a given entry
   // or the null pointer if the entry is not in the bag.
   Node<ItemType>* getPointerTo(const ItemType& target) const;
   
public:
   LinkedBag();
   LinkedBag(const LinkedBag<ItemType>& aBag); // Copy constructor
   virtual ~LinkedBag();                       // Destructor should be virtual
   int getCurrentSize() const;
   bool isEmpty() const;
   bool add(const ItemType& newEntry);
   bool remove(const ItemType& anEntry);
   void clear();
   bool contains(const ItemType& anEntry) const;
   int getFrequencyOf(const ItemType& anEntry) const;
   std::vector<ItemType> toVector() const;
}; // end LinkedBag

#include "DoublyLinkedBag.cpp"
#endif