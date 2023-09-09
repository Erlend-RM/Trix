abstract class Post {
    String beskrivelse;
    String mottaker;

    Post (String beskrivelse, String mottaker) {
        this.beskrivelse = beskrivelse;
        this.mottaker = mottaker;
    }

    String hentBeskrivele() {
        return beskrivelse;
    }

    String hentMottaker() {
        return mottaker;
    }

    @Override
    public String toString() {
        return "Mottaker: " + mottaker + "\nBeskrivelse: " + beskrivelse;
    }
}
