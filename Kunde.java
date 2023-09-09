public class Kunde implements Runnable {
    String navn;
    Postkontor postkontor;

    Kunde (String navn, Postkontor postkontor) {
        this.navn = navn;
        this.postkontor = postkontor;
    }

    @Override
    public void run () {
        while (true) {
            Post post = postkontor.hentPost(navn);
            if (post != null) {
                System.out.println(post);
            }
        }
    }
}
