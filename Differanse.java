import java.util.Scanner;

class Differanse{
  public static void main(String[] args){
  Scanner sc = new Scanner(System.in);
  System.out.println("Oppgi verdien til x: ");
  int x = sc.nextInt();
  System.out.println("Oppgi verdien til y: ");
  int y = sc.nextInt();
  int dif = x - y;
  System.out.println("Differansen mellom x og y er " + dif + ".");
  }
}
