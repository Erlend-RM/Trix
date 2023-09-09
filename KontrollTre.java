public class KontrollTre {
    private TreBegreOgEnBall treBegreOgEnBall;
    private ModellTre modellTre;

    KontrollTre() {
        treBegreOgEnBall = new TreBegreOgEnBall(this);
        modellTre = new ModellTre(treBegreOgEnBall, this);
    }

    public static void main(String[] args) {
        KontrollTre kontrollTre = new KontrollTre();
    }
}
