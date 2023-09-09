import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class EnkeltRutenett {
    private Kontroll kontroll;
    private JFrame vindu;
    private JPanel rutenett;
    private JLabel[][] ruter = new JLabel[3][3];

    EnkeltRutenett (Kontroll kontroll) {
        this.kontroll = kontroll;
        try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        }
        catch (Exception e) {
            System.exit(1);
        }

        vindu = new JFrame("EnkeltRutenett");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        rutenett = new JPanel();

        vindu.add(rutenett, BorderLayout.CENTER);

        rutenett.setLayout(new GridLayout(3, 3));
        for (int rad = 0 ; rad < 3 ; rad++) {
            for (int kol = 0 ; kol < 3 ; kol++) {
                JLabel rute = new JLabel(""+(rad + kol));
                ruter[rad][kol] = rute;
                rute.setOpaque(true);
                rute.setForeground(Color.BLACK);
                rute.setBackground(Color.WHITE);
                rute.setBorder(BorderFactory.createLineBorder(Color.BLACK));
                rutenett.add(rute);
            }
        }

        vindu.pack();
        vindu.setVisible(true);
    }

}