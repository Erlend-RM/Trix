import java.util.concurrent.locks.*;

public class Postkontor {
    Post[] postListe = new Post[10];

    Lock laas = new ReentrantLock();
    Condition ikkeFull = laas.newCondition();
    Condition ikkeTom = laas.newCondition();

    public int storrelse() {
        int storrelse = 0;
        
        for (int i = 0 ; i < postListe.length ; i ++) {
            if (postListe[i] != null) {
                storrelse ++;
            }
        }
        return storrelse;
    }


    void leverPost(Post post) {
        laas.lock();

        try {
            if (storrelse() == 10) {
                ikkeFull.await();
            }

            for (int i = 0 ; i < postListe.length ; i++) {
                if (postListe[i] == null) {
                    postListe[i] = post;
                    ikkeTom.signal();
                    return;
                }
            }
        }
        catch (InterruptedException e) {
            System.out.println(e);
        }
        finally {
            laas.unlock();
        }
    }

    Post hentPost(String mottaker) {
        laas.lock();

        try {
            if (storrelse() == 0) {
                ikkeTom.await();
            }
            for (int i = 0 ; i < postListe.length ; i++) {
                if (postListe[i] != null) {
                    if (postListe[i].hentMottaker().equals(mottaker)) {
                        Post post = postListe[i];
                        postListe[i] = null;
                        ikkeFull.signal();
                        return post;
                    }
                }
            }
            ikkeTom.await();
        }
        catch (InterruptedException e) {
            System.out.println(e);
        }
        finally {
            laas.unlock();
        }
        return null;
    }
}