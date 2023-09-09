import java.util.HashMap;
import java.util.Scanner;

public class EnkelTelefonbok {
    public static void main(String[] args) {
        HashMap<String, String> telefonBok = new HashMap<String, String>();
        
        telefonBok.put("Arne", "22334455");
        telefonBok.put("Lisa", "95959595");
        telefonBok.put("Jonas", "97959795");
        telefonBok.put("Peder", "12345678");
        
        int start = 1;
        while (start != 0) {
            Scanner mittObj = new Scanner(System.in);
            System.out.println("Soek etter nr (Skriv inn navn): ");
            String navn = mittObj.nextLine();
            System.out.println("Nr til " + navn + " er: " + telefonBok.get(navn));

            System.out.println("Tast 1 om du vil soeke på nytt navn eller tast 0 for aa avslutte: ");
            start = mittObj.nextInt();
        }
        
        for (String i : telefonBok.keySet()) {
            System.out.println("Navn: " + i + "\nNr: " + telefonBok.get(i) + "\n");
        }


    }
}
