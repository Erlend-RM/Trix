//class Test {
//   public static void main(String[] args) {
//       int jens;
//       int siv = Jens * 3;
//       System.out.println("Svar: " siv);
//       erna = siv - jens;
//       System.out.printn(erna);
//}

class Test {
   public static void main(String[] args) {
       int jens;
       jens = 2;
       int siv = jens * 3;
       int erna;
       System.out.println("Svar: " + siv);
       erna = siv - jens;
       System.out.println(erna);
     }
}

//a) Test.java:8: reached end of file while parsing
//   }

//Betyr at det manlger en {}.
//som vil si at en av {} ikke har en ende


//b) Test.java:4: cannot find symbol
//symbol : variable Jens
//location: class Test
//int siv = Jens * 3;

//Er det at det er Stor bokstav i Jens isteden for
//liten som det skal være (jens) og finner den derfor ikke


//c) Test.java:4: variable Jens might not have been initialized
//  int siv = Jens * 3;

// her handler feilmelding om at jens ikke er satt til noen verdi


//d) Test.java:5: ’)’ expected
//  System.out.println("Svar: " siv);
//                             ^
//   Test.java:5: illegal start of expression
//    System.out.println("Svar: " siv);

//Får feilmelding fordi det mangler + mellom Stringen og variabelen
//så derfor sier den at det er feil med parantesene


//e) Test.java:6: cannot find symbol
//   symbol : variable erna
//   location: class Test
//    erna = siv - jens;

//erna er ikke initializert så derfor får man feilmelding på denne

//f) Test.java:7: cannot find symbol
//   symbol : method printn(int)
//   location: class java.io.PrintStream
//    System.out.printn(erna);

//Det mangler en l i println som lager feilmeldingingen


//g)Test.java:2: ’;’ expected
//    public static void main(String[] args)
//                                          ^
//   Test.java:5: <identifier> expected
//    System.out.println("Svar: " + siv);
//                      ^
//   Test.java:5: illegal start of type
//    System.out.println("Svar: " + siv);
//                        ^

//Grunne til dette er at java da ikke vet at det er main funksjonen
//og vil derfor at du skal ha ; på slutten av parantesene selv om dette er feil.
