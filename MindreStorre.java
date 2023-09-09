import java.util.Scanner;

class MindreStorre {
    public static void main(String[] args) {
        Scanner mittObjekt = new Scanner(System.in);
        
        System.out.println("Tast in tall: ");
        int tall1 = mittObjekt.nextInt();
        if (tall1 > 10) {
            System.out.println("Tallet er stoerre enn 10.");
        }
        else {
            System.out.println("Tallet er mindre enn 10.");
        }
        
        System.out.println("Tast inn et tall: ");
        int tall2 = mittObjekt.nextInt();
        if (20 > tall2 && tall2 > 10) {
            System.out.println("Tallet er mellom 10 og 20.");
        }
        else {
            System.out.println("Tallet er ikke mellom 10 og 20.");
        }
        
        System.out.println("Tast inn et tall: ");
        int tall3 = mittObjekt.nextInt();
        if (tall3 > 20) {
            System.out.println("Tallet er stoerre enn 20.");
        }
        else {
            System.out.println("Tallet er mindre enn 20.");
        }

    }   
}

