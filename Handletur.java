import java.util.Scanner;

class Handletur{
    public static void main(String[] args) {
        System.out.println("Hei! Velkommen til IFI-butikken.");
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Hvor mange broed vil du ha?");
        int antallBrod = sc.nextInt();
        int brod = 20;
        int totBrod = antallBrod * brod;
        
        System.out.println("Hvor mange melk vil du ha?");
        int antallMelk = sc.nextInt();
        int melk = 15;
        int totMelk = antallMelk * melk;

        System.out.println("Hvor mange ost vil du ha?");
        int antallOst = sc.nextInt();
        int ost = 40;
        int totOst = antallOst * ost;
        
        System.out.println("Hvor mange yoghurt vil du ha?");
        int antallYoghurt = sc.nextInt();
        int yoghurt = 20;
        int totYoghurt = antallYoghurt * yoghurt;

        System.out.println("Du skal betale: " + (totBrod+totMelk+totOst+totYoghurt));
    }
}

