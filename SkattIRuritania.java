import java.util.Scanner;
class SkattIRutitania{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Skriv inn din inntekt: ");

        float inntekt = sc.nextFloat();
        if(inntekt < 10000){
            System.out.println("Du skal betale " + String.format("%.2f", (inntekt * 0.10)) + " i skatt.");
        }
        else{
            System.out.println("Du skal betale " + String.format("%.2f", ((10000 * 0.10) + ((inntekt-10000)*0.30))) + " i skatt.");
        }
    }
}
