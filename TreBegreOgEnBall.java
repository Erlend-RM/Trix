import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

import java.util.Random;

public class TreBegreOgEnBall {
    private KontrollTre kontrollTre;
    private JFrame vindu;
    private JPanel panelKnapper;
    static boolean ferdig = false;
    static Beger[] beger = new Beger[1+3];

    TreBegreOgEnBall(KontrollTre kontrollTre) {
        this.kontrollTre = kontrollTre;
        try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        }
        catch (Exception e) {
            System.exit(1);
        }

        vindu = new JFrame("TreBegreOgEnBall");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        panelKnapper = new JPanel();
        
        vindu.add(panelKnapper);        

        for (int i = 1 ; i <= 3 ; i++) {
            beger[i] = new Beger(i);
            beger[i].initGUI();
            panelKnapper.add(beger[i]);
        }
        beger[new Random().nextInt(3)+1].harBall = true;


        vindu.pack();
        vindu.setVisible(true);
    }

    class Beger extends JButton {
        int nr;
        boolean harBall = false;

        Beger (int nr) {
            super("" + nr);
            this.nr = nr;
        }

        class Velger implements ActionListener {
            @Override
            public void actionPerformed (ActionEvent e) {
                if (TreBegreOgEnBall.ferdig) {
                    return;
                }

                Beger beger = (Beger)e.getSource();
                if (beger.harBall) {
                    beger.setForeground(Color.GREEN);
                    beger.setText("OK");
                }
                else {
                    beger.setForeground(Color.RED);
                    beger.setText("X");
                }
                TreBegreOgEnBall.ferdig = true;
            }
        }

        void initGUI () {
            addActionListener(new Velger());
        }
    }

    
}
