class Sanhetsverdier{
  boolean b;
  b = false;
  int x;
  x = 0;

  // 1. false
  public static void main(Int, boolean[] args) {
    System.out.println(b && x == 0);
  }


  // 2. true
  b || x == 0;

  // 3. true
  !b && x == 0;

  // 4.true
  !b || x == 0;

  // 5. false
  b && x != 0;

  // 6. false
  b || x != 0;

  // 7. false
  !b && x != 0;

  // 8. true
  !b || x != 0;

}
