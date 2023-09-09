public class Postmann implements Runnable {
    Postkontor postkontor;

    Postmann (Postkontor postkontor) {
        this.postkontor = postkontor;
    }
    
    
    @Override
    public void run () {
        for (int i = 0 ; i < 100 ; i ++) {
            if (i % 2 == 0) {
                Post pakke = new Pakke("Hey dude", "Eskild");
                postkontor.leverPost(pakke);
            }
            else {
                Post brev = new Brev("Hey sup man?", "Eirik");
                postkontor.leverPost(brev);
            }
        }
    }

}
