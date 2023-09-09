public class Student {
    String navn;
    int quizScore;
    int antallQuizer;


    public Student(String navn, int quizScore, int antallQuizer){
        this.navn = navn;
        this.quizScore = quizScore;
        this.antallQuizer = antallQuizer;
    }

    public String hentNavn(){
        return navn;
    }

    public void lettTilQuizScore(int score){
        quizScore += score;
        antallQuizer ++;
    }

    public int hentTotalScore(){
        return quizScore;
    }

    public int hentGjennomsnitteligScore(){
        return quizScore/antallQuizer;
    }
}
