import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Sjakkbrett {
    private JFrame vindu;
    private JLabel[][] ruter = new JLabel[8][8];
    private JPanel sjakkbrett;

    Sjakkbrett() {
        try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        }
        catch (Exception e) {
            System.exit(1);
        }

        vindu = new JFrame("Sjakkbrett");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        sjakkbrett = new JPanel();

        vindu.add(sjakkbrett, BorderLayout.CENTER);

        sjakkbrett.setLayout(new GridLayout(8, 8));
        for (int rad = 0 ; rad < 8 ; rad++) {
            for (int kol = 0 ; kol < 8 ; kol++) {
                JLabel rute = new JLabel(" ");
                ruter[rad][kol] = rute;

                if ((rad + kol) % 2 == 0){
                    rute.setBackground(Color.WHITE);
                    rute.setPreferredSize(new Dimension(50, 50));
                    rute.setOpaque(true);
                }
                else {
                    rute.setBackground(Color.BLACK);
                    rute.setPreferredSize(new Dimension(50, 50));
                    rute.setOpaque(true);
                }
                sjakkbrett.add(rute);
            }
        }
        vindu.pack();
        vindu.setVisible(true);
    }
}
