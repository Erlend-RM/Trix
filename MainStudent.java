class MainStudent {

    public static void main(String[] args) {
        Student student1 = new Student("Joakim", 0, 0);
        Student student2 = new Student("Kristin", 0, 0);
        Student student3 = new Student("Dag", 0, 0);

        student1.lettTilQuizScore(23);
        student1.lettTilQuizScore(23);

        student2.lettTilQuizScore(15);
        student2.lettTilQuizScore(32);

        student3.lettTilQuizScore(26);
        student3.lettTilQuizScore(14);

        System.out.println(student1.hentTotalScore());
        System.out.println(student1.hentGjennomsnitteligScore());

        System.out.println(student2.hentTotalScore()); 
        System.out.println(student2.hentGjennomsnitteligScore());

        System.out.println(student3.hentTotalScore());
        System.out.println(student3.hentGjennomsnitteligScore());
    }
}
