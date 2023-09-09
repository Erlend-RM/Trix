import java.io.*;
import java.util.Scanner;

public class TemperaturLeser {
    
    public static void main(String[] args) {
        String[] temp;
        temp = new String[12];
        
        try {
            File fil = new File("Temperatur.txt");
            Scanner sc = new Scanner(fil);
            int i = 0;
        
            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                temp[i] = data;
                i++;
            }
            sc.close();
        
            for (int k = 0; k < temp.length; k++) {
                System.out.println(temp[k]);
            }
        }
        
        catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        } 
       
    }
    
    
}
