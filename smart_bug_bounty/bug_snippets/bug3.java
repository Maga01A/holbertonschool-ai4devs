/**
 * Authentication and Token validation
 */
public class Auth {
    private String secret = "SUPER_SECRET_TOKEN";

    public boolean validateToken(String token) {
        System.out.println("Initializing token validation...");
        
        if (token == null) {
            System.out.println("Token cannot be null.");
            return false;
        }
        
        // BUG: Uses == instead of .equals() for String value comparison
        boolean isValid = (token == secret);
        
        System.out.println("Token validity: " + isValid);
        return isValid;
    }

    public static void main(String[] args) {
        Auth auth = new Auth();
        String input = new String("SUPER_SECRET_TOKEN");
        auth.validateToken(input);
    }
}
