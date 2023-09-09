class RektangelHovedprogram{
  public static void main(String[] args){

  Rektangel en = new Rektangel(5,9);
  Rektangel to = new Rektangel(10, 2);

  System.out.println("Areal: " + en.areal());
  System.out.println("Areal: " + to.areal());

  en.oekBredde(5);
  to.oekLengde(2);
  en.reduserBredde(2);
  to.reduserLengde(5);

  System.out.println("Omkrets: " + en.omkrets());
  System.out.println("Omkrets: " + to.omkrets());
  }
}


class Rektangel {

  double bredde;
  double lengde;

  public Rektangel (double l, double b) {   // Konstruktør
    lengde = l;
    bredde = b;
  }

  public void oekLengde (int okning) {    // Oek lengden som angitt
    lengde = lengde + okning;
    //lengde += okning;
  }

  public void oekBredde (int okning) {    // Oek bredden som angitt
    bredde = bredde + okning;
    //bredde += okning;
  }

  public double areal () {     // Beregn mitt areal
    return bredde * lengde;
  }

  public double omkrets () {   // Beregn min omkrets
    return bredde * 2 + lengde * 2;
  }

  public void reduserBredde(int reduser){
    if (bredde - lengde < 1){
        System.out.println("Bredden kan ikke reduseres så mye.");
    }
    else{
      bredde = bredde - reduser;
    }
  }

  public void reduserLengde(int reduser){
    if (lengde - reduser < 1){
      System.out.println("Lengde kan ikke reduseres så mye");
    }
    else{
      lengde = lengde - reduser;
    }
  }
}
