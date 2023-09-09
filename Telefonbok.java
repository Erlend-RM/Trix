import java.util.*;

class Telefonbok {
    
    public static void main(String[] args) {
        Person person1 = new Person("Erlend", "69696969", "Ja 12");
        Person person2 = new Person("Eskild", "42042071", "Nei 15");
        Person person3 = new Person("Anders", "42069692", "Nope 27");
    

        Person[] telefonbok = new Person[10];
        
        telefonbok[0] = person1;
        telefonbok[1] = person2;
        telefonbok[2] = person3;

        for (int i = 0; i < telefonbok.length; i++){
            if (telefonbok[i] != null){
                telefonbok[i].skrivInfo();
            }
        }
        ArrayList<Person> telefonListe = new ArrayList<>();
        telefonListe.add(person1);
        telefonListe.add(person2);
        telefonListe.add(person3);

        //For each loop (kan kun brukes på liste)
        for (Person t : telefonListe){
            t.skrivInfo();
        }

        HashMap<String, Person> telefonBok = new HashMap<>();

            telefonBok.put(person1.hentNavn(), person1);
            telefonBok.put(person2.hentNavn(), person2);
            telefonBok.put(person3.hentNavn(), person3);

        for (Person k : telefonBok.values()) {
            k.skrivInfo();
        }
    }
}
