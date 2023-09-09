import java.util.Scanner;

class Returtyper{
  public static void main(String[] args) {

  }

  public void jegReturnereIngenting(){

  }

  public int summenAvToHeltall(){
    int a = 2;
    int b = 3;
    return a + b;
  }

  public double summenAvToFlyttall(){
    double a = 2.0;
    double b = 3.0;
    return a + b;
  }

  public String navnetTilBrukeren(){
    Scanner tastatur = new Scanner(System.in);
    String navn = tastatur.nextLine();
    return navn;
  }
}
