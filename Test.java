import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class GUI {
    private Kontroll kontroll;
    private JFrame vindu;
    private JPanel panel;
    private JLabel antall;
    private JButton tell, resett, slutt;

    GUI (Kontroll k) {
        kontroll = k;
        try {
            UIManager.getCrossPlatformLookAndFeelClassName();
        } catch (Exception e) {
            System.exit(1);
        }

        vindu = new JFrame("Teller");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        panel = new JPanel();
        vindu.add(panel);

        antall = new JLabel(" 0 ");

        tell = new JButton(" +1 ");
        class OekTeller implements ActionListener {
            @Override
            public void actionPerformed (ActionEvent e) {
                kontroll.oekTeller();
            }
        }
        tell.addActionListener(new OekTeller());

        resett = new JButton(" =0 ");
        class Nuller implements ActionListener {
            @Override
            public void actionPerformed (ActionEvent e) {
                kontroll.nullstillTeller();
            }
        }
        resett.addActionListener(new Nuller());

        slutt = new JButton("Exit");
        class Stopper implements ActionListener {
            @Override
            public void actionPerformed (ActionEvent e) {
                kontroll.avslutt();
            }
        }
        slutt.addActionListener(new Stopper());

        panel.add(antall);
        panel.add(tell);
        panel.add(resett);
        panel.add(slutt);

        vindu.pack();
        vindu.setVisible(true);
    }   
}

