public class Bug3Fixed {
    public static void main(String[] args) {
        String text = null;

        if ("hello".equals(text)) {
            System.out.println("Greeting detected");
        }

        System.out.println("Done");
    }
}