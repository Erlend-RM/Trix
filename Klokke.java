import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

import java.time.LocalTime;

public class Klokke {
    KontrollKl kontrollKl;
    private JFrame vindu;
    private JButton klokke;

    Klokke(KontrollKl kontrollKl) {
        this.kontrollKl = kontrollKl;
        try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        }
        catch (Exception e) {
            System.exit(1);
        }

        vindu = new JFrame("Klokke");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        klokke = new JButton("Klokken er " + naa());

        vindu.add(klokke, BorderLayout.CENTER);

        class Stopper implements ActionListener {
            @Override
            public void actionPerformed(ActionEvent e) {
                kontrollKl.avslutt();
            }
        }
        klokke.addActionListener(new Stopper());


        vindu.pack();
        vindu.setVisible(true);

    }

    private static String naa() {
        LocalTime tid = LocalTime.now();
        return String.format("%02d:%02d:%02d",
        tid.getHour(), tid.getMinute(), tid.getSecond());
    }
    
}
