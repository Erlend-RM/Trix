import java.util.Scanner;

class Produkt{
  public static void main(String[] args) {
  Scanner myObj = new Scanner(System.in);
  System.out.println("Oppgi verdien til x: ");
  int x = myObj.nextInt();

  System.out.println("Oppgi verdien til y: ");
  int y = myObj.nextInt();

  System.out.println("Produktet av x og y er " + (x*y));

  System.out.println("Differansen mellom x og y er " + (x-y));
  }
}
