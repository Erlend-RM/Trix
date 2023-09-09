public class KontrollKl {
    private Klokke klokke;
    private ModellKl modellKl;

    KontrollKl () {
        klokke = new Klokke(this);
        modellKl = new ModellKl(klokke, this);
    }

    void avslutt () {
        System.exit(0);
    }

    public static void main(String[] args) {
        KontrollKl kontrollKl = new KontrollKl();  
    }
}
