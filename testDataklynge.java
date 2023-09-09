public class testDataklynge {
    

    class DataKlynge {

        private ArrayList<Rack> rackList = new ArrayList<Rack>();
        private int rackStoerrelse;
      
        // Constructor for DataKlynge-klassen
        public DataKlynge(String filnavn) {
          File f = new File(filnavn);
          Scanner fil = null;
          // Proever aa lage en scanner for fil-objektet og gir feilmelding om den ikke finner filen.
          try {
            fil = new Scanner(f);
          } catch (FileNotFoundException e) {
            System.out.println("File '" + filnavn + "' not found!");
          }
          rackStoerrelse = Integer.parseInt(fil.nextLine());
          System.out.println(rackStoerrelse);
          String[] tempArr;
          // Genererer dataklyngen utifra informasjonen i filen
          while (fil.hasNextLine()) {
            tempArr = fil.nextLine().split(" ");
            this.leggTilNoder(Integer.parseInt(tempArr[0]), // Antall noder
                              Integer.parseInt(tempArr[1]), // Minne
                              Integer.parseInt(tempArr[2])); // Antall prosessorer
          }
          fil.close();
        }
      
        // Legger til et objekt av typen Rack til rackList
        public void leggTilRack(Rack rack) {
          rackList.add(rack);
        }
      
        // Henter rackList
        public ArrayList<Rack> hentRackList() {
          return rackList;
        }
      
        // Henter antall racks
        public int hentAntRack() {
          return rackList.size();
        }
      
        // henter noder med like mye eller mer minne som paakrevdMinne
        public int noderMedNokMinne(int paakrevdMinne) {
          int total = 0;
          for (Rack r : rackList) {
            total += r.noderMedNokMinne(paakrevdMinne);
          }
          return total;
        }
      
        // Henter antall prosessorer i hele dataklyngen
        public int hentAntProsessorer() {
          int total = 0;
          for (Rack r : rackList) {
            total += r.hentAntProsessorer();
          }
          return total;
        }
      
        // Jeg saa det som en god ting aa legge til denne metoden for aa ikke ha et altfor
        // stort testprogram.
        // Lager nye rack og noder med spesifikasjoner gitt som argumenter.
        public void leggTilNoder(int antallNoder, int minne, int antProsessorer) {
      
          // Lager et nytt rack hvis racklisten er tom.
          if (rackList.size() == 0) {
            // Her trengs det ikke aa bruke this, men det gjoer det tydeligere hva jeg proever aa gjoere
            this.leggTilRack(new Rack(rackStoerrelse));
          }
      
          // Definerer en variabel rack som peker paa et rackobjekt for aa ikke
          // maatte definere at det er en rack hver gang jeg skal flytte pekeren.
          Rack rack;
          for (int i = 0; i < antallNoder ;i++) {
            // henter siste element i rackList og sjekker om det er ikke fullt
            rack = rackList.get(rackList.size()-1);
      
            if (rack.erFull()) {
              this.leggTilRack(new Rack(rackStoerrelse));
              rack = rackList.get(rackList.size()-1);
              rack.leggTilNode(new Node(antProsessorer, minne), 0);
            } else { // hvis rack er full, saa lager vi et nytt rack.
              rack.leggTilNode(new Node(antProsessorer, minne), rack.foersteLedigePlass());
            }
          }
        }
      }
}
