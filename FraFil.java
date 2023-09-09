import java.io.*;
import java.util.Scanner;

class FraFil {
    public static void main(String[] args) {
        try {
            File fil = new File("tekst.txt");
            Scanner sc = new Scanner(fil);
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                System.out.println(data);
            }
            sc.close();
        }

        catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }        
    }
}
