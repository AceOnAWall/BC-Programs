import java.util.Scanner;

public class ShoppingCartManager {
   public static char printMenu(ShoppingCart theCart, Scanner scnr){
      char menuOp = ' ';
      String productName;
      String productDescription;
      int productPrice = 0;
      int productQuantity = 0;
      
      System.out.println("MENU");
      System.out.println("a - Add item to cart");
      System.out.println("d - Remove item from cart");
      System.out.println("c - Change item quantity");
      System.out.println("i - Output items' descriptions");
      System.out.println("o - Output shopping cart");
      System.out.println( "q - Quit");
      System.out.println("");

      while (menuOp != 'a' && menuOp != 'd' && menuOp != 'c' &&
                menuOp != 'i' && menuOp != 'o' && menuOp != 'q') {

         System.out.println("Choose an option: ");
         menuOp = scnr.next().charAt(0);
      }
      
      
      switch (menuOp) {
         case 'a':
            scnr.nextLine(); 
            System.out.println("ADD ITEM TO CART");
            System.out.println("Enter the item name: ");
            productName = scnr.nextLine();
         
            System.out.println("Enter the item description: ");
            productDescription = scnr.nextLine();
      
            System.out.println("Enter the item price: ");
            productPrice= scnr.nextInt();
      
            System.out.println("Enter the item quantity: ");
            productQuantity = scnr.nextInt();
            
            ItemToPurchase newItem = new ItemToPurchase(productName, productDescription, productPrice, productQuantity);
            theCart.addItem(newItem);
            
            menuOp = ' ';
            System.out.println("");
            break;
         
         case 'd':
            scnr.nextLine(); 
         
            System.out.println("REMOVE ITEM FROM CART");
            System.out.println("Enter name of item to remove: ");
            productName = scnr.nextLine();
            
            theCart.removeItem(productName);
            menuOp = ' ';
            System.out.println("");
            break;
      
      case 'c':
            scnr.nextLine();    
            
            System.out.println("CHANGE ITEM QUANTITY");
            System.out.println("Enter the item name: ");
            productName = scnr.nextLine();
         
            System.out.println("Enter the new quantity: ");
            productQuantity = scnr.nextInt();
            
            ItemToPurchase modItem = new ItemToPurchase();
            modItem.setName(productName);
            modItem.setQuantity(productQuantity);
            
            theCart.modifyItem(modItem);
            
            menuOp = ' ';
            System.out.println("");
            break;
      
      case 'i':
            System.out.println("OUTPUT ITEMS' DESCRIPTIONS");
            theCart.printDescriptions();
            
            menuOp = ' ';
            System.out.println("");
            break;
      
      case 'o':
            System.out.println("OUTPUT SHOPPING CART"); 
            theCart.printTotal();
            
            menuOp = ' ';
            System.out.println("");
            break;
      }
      
      return menuOp;
   }
   
   
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      String customerName;
      String todaysDate;
      char menuChoice = ' ';
      
      System.out.println("Enter Customer's Name: ");
      customerName = scnr.nextLine();
      
      System.out.println("Enter Today's Date: ");
      todaysDate = scnr.nextLine();
   
      System.out.println("Customer Name: " + customerName);
      System.out.println("Today's Date: " + todaysDate);
      System.out.println("");
      
      ShoppingCart myCart = new ShoppingCart(customerName, todaysDate);
      
      while(menuChoice != 'q') {
         menuChoice = printMenu(myCart, scnr);
      }

      return;
   }   
}

 
public class ItemToPurchase {
   private String itemName;
   private int itemPrice;
   private int itemQuantity;
   private String itemDescription;
   
   public ItemToPurchase() {
      itemName = "none";
      itemDescription = "none";
      itemPrice = 0;
      itemQuantity = 0;

      return;
   }
   
   public ItemToPurchase(String name, String description, int price, int quantity) {
      itemName = name;
      itemPrice = price;
      itemQuantity = quantity;
      itemDescription = description;
      
      return;
   }
  
   public void setName(String name) {
      itemName = name;
      return;
   }
   
   public void setPrice(int price) {
      itemPrice = price;
      return;
   }
   
   public void setQuantity(int quantity) {
      itemQuantity = quantity;
      return;
   }
   
   public void setDescription(String description) {
      itemDescription = description;
      return;
   }

   public String getName() {
      return itemName;
   }
   
   public int getPrice() {
      return itemPrice;
   }
   
   public int getQuantity() {
      return itemQuantity;
   }

   public String getDescription() {
      return itemDescription;
   }
   
   public void printItemCost() {
      System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice + " = $" + 
                        (itemPrice * itemQuantity));
   }
   
   public void printItemDescription() {
      System.out.println(itemName + ": " + itemDescription);
   }
   
}

 
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
      boolean found = false;
      
      while ( (!found) && (i < cartItems.size()) ) {
         if (cartItems.get(i).getName().equals(name)) {
            cartItems.remove(i); 
            found = true;
         }
         
         ++i;
      }
      
      if(!found) {
         System.out.println("Item not found in cart. Nothing removed.");
      }
   }
   
   public void modifyItem(ItemToPurchase item) {
      int i = 0;
      boolean found = false;
      
      while ( (!found) && (i < cartItems.size()) ) {
         if (cartItems.get(i).getName().equals(item.getName())) {            
            found = true;

            // Update fields  
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
         
         ++i;
      }
   
      if(!found) {
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
