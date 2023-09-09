public class Brev extends Post {
    
    Brev (String beskrivelse, String mottaker) {
        super(beskrivelse, mottaker);
    }

    @Override
    public String toString() {
        return "Mottaker: " + mottaker + "\nBrev - beskrivelse: " + beskrivelse;
    }
}
