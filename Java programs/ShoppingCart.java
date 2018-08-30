import java.util.ArrayList;

public class ShoppingCart {
   
   private String customerName;
   private String currentDate;
   private ArrayList<ItemToPurchase> cartItems = new ArrayList<ItemToPurchase> ();
   
   
   public ShoppingCart() {
	   
      customerName = "none";
      currentDate = "January 1, 2016";
   }

   public ShoppingCart(String name, String date) {
	   
      customerName = name;
      currentDate = date;
   }

   public String getCustomerName()  {
	   
      return customerName;
   }

   public String getDate() {
	   
      return currentDate;
   }
   
   public void addItem(ItemToPurchase item) {
	   
      cartItems.add(item);
   }

   public void removeItem(String name) {
	   
      int i = 0;
      boolean inCart = false;
      
      while ((i < cartItems.size()) && (!inCart)) {
		  
         if (cartItems.get(i).getName().equals(name)) {
            inCart = true;
			cartItems.remove(i); 
         }
         i++;
      }
      
      if(!inCart) {
         System.out.println("Item not found in cart. Nothing removed.");
      }
   }
   
   public void modifyItem(ItemToPurchase item) {
	   
      int i = 0;
      boolean inCart = false;
      
      while ( (!inCart) && (i < cartItems.size()) ) {
		  
         if (cartItems.get(i).getName().equals(item.getName())) {            
            inCart = true;
 
            if (!item.getDescription().equals("none")) {
               cartItems.get(i).setDescription(item.getDescription());
            }
            
            if (item.getPrice() != 0) {
               cartItems.get(i).setPrice(item.getPrice());
            }
            
            if (item.getQuantity() != 0) {
               cartItems.get(i).setQuantity(item.getQuantity());
            }
         }
         i++;
      }
   
      if(!inCart) {
         System.out.println("Item not found in cart. Nothing modified.");
      }
   }
   
   public int getNumItemsInCart() {
	   
      int i = 0;
      int totalItems = 0;
      
      for (i = 0; i < cartItems.size(); ++i) {
         totalItems += cartItems.get(i).getQuantity();
      }
      
      return totalItems;
   }
   
   public int getCostOfCart() {
	   
      int i = 0;
      int totalCost = 0;
      
      for (i = 0; i < cartItems.size(); ++i) {
         totalCost += (cartItems.get(i).getPrice() * cartItems.get(i).getQuantity());
      }
      
      return totalCost;
   }
   
   public void printTotal() {
	   
      int i = 0;
      int totalCost = 0;
      
      System.out.println(customerName + "'s Shopping Cart - " + currentDate);
      System.out.println("Number of Items: " + getNumItemsInCart());
      System.out.println("");
      
      if (cartItems.size() > 0) {
         for (i = 0; i < cartItems.size(); ++i) {
            cartItems.get(i).printItemCost();
         }
      }
	  
      else {
         System.out.println("SHOPPING CART IS EMPTY");
      }
      
      totalCost = getCostOfCart();
      System.out.println("");
      System.out.println("Total: $" + totalCost);
   }
   
   public void printDescriptions() {
	   
      int i = 0;
      
      System.out.println(customerName + "'s Shopping Cart - " + currentDate);
      System.out.println("");
      System.out.println("Item Descriptions");
      
      if(cartItems.size() > 0) {
         for(i = 0; i < cartItems.size(); ++i) {
            cartItems.get(i).printItemDescription();
         }
      }
      else {
         System.out.println("SHOPPING CART IS EMPTY");
      }
   }
}