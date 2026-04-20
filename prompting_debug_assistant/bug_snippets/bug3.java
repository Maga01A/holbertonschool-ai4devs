public class Bug3 {
    public static void main(String[] args) {
        String text = null;

        if (text.equals("hello")) {
            System.out.println("Greeting detected");
        }

        System.out.println("Done");
    }
}