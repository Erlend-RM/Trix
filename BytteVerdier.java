public class BytteVerdier {
    public static void main(String[] args) {
        int x = 3;
        int y = 4;
        variabelBytte(x, y);
        System.out.println(x + " " + y);
    }
    // returnerer ikke a og b slik at x og y bytter plass.
    public static void variabelBytte(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }
}
