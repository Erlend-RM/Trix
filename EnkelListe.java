import java.util.ArrayList;

class EnkelListe {
    private Node start;

    public void settInnForan(String nyttInnhold) {
        Node ny = new Node(nyttInnhold);
        ny.neste = start;
        start = ny;
    }

    public void skrivUt() {
        skrivUtBaklengs(start);
    }

    private void skrivUtBaklengs(Node n) {
        ArrayList<String> noder = new ArrayList<>();
        while (n.neste != null) {
            noder.add(n.innhold);
            n = n.neste;
        }
        int antallNoder = noder.size() - 1;

        while (antallNoder != -1) {
            System.out.println(noder.get(antallNoder));
            antallNoder--;
        }
    }

    private class Node {
        private String innhold;
        private Node neste;

        Node(String s) {
            innhold = s;
        }
    }
}