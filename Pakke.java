public class Pakke extends Post{

    public Pakke (String beskrivelse, String mottaker) {
        super(beskrivelse, mottaker);
    }

    @Override
    public String toString() {
        return "Mottaker: " + mottaker + "\nPakke - beskrivelse: " + beskrivelse;
    }
    
}
