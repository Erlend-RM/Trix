class Heltallsarray {
    public static void main(String[] args) {
        int tall1 = 0;
        int tall2 = 1;
        int tall3 = 2;
        int tall4 = 3;
        int tall5 = 4;

        System.out.println("Tall 1: " + tall1);
        System.out.println("Tall 2: " + tall2);
        System.out.println("Tall 3: " + tall3);
        System.out.println("Tall 4: " + tall4);
        System.out.println("Tall 5: " + tall5);

        int tall[]= new int [5];
        
        int lengdePaaArray = tall.length;
        int teller = 0;
        while (teller < lengdePaaArray) {
            tall[teller] = teller;
            teller ++; 
        }

        for (int i : tall) {
            System.out.println("Tall " + (i+1) +": " + i);
        }




    }
}
