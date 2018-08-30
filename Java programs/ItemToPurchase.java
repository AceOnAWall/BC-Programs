/* 
Author: Wallace, Ryan
Assignment: Programming Assignment Four-Five
Course: COMP B11
Instructor: Richard Miles
Date submitted: 2016/11/21
*/


public class ItemToPurchase {

	private String itemDescription;
    private String itemName;
    private int itemQuantity;
    private int itemPrice;
   
    public ItemToPurchase() {
      
        itemDescription = "none";
	    itemName = "none";
        itemQuantity = 0;
	    itemPrice = 0;
    }
   
    public ItemToPurchase(String name, String description, int quantity, int price) {
	  
	    itemDescription = description;
        itemName = name;
        itemQuantity = quantity;
        itemPrice = price;
    }
  
    public void setDescription(String description) {
		
		itemDescription = description;
    }
   
	public String getDescription() {
		
        return itemDescription;
    }
  
    public void setName(String name) {
	   
        itemName = name;
    }
   
    public String getName() {
		
        return itemName;
    }
   
    public void setPrice(int price) {
	   
        itemPrice = price;
    }
   
    public int getPrice() {
		
        return itemPrice;
    }
   
    public void setQuantity(int quantity) {
	   
        itemQuantity = quantity;
    }
 
    public int getQuantity() {
		
        return itemQuantity;
    }

    public void printItemCost() {
		
        System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice + " = $" + itemQuantity * itemPrice);
    }
   
    public void printItemDescription() {
		
        System.out.println(itemName + ": " + itemDescription);
    }
}