/**
 * Authentication and Token validation
 */
public class bug3_fixed {
    private String secret = "SUPER_SECRET_TOKEN";

    public boolean validateToken(String token) {
        System.out.println("Initializing token validation...");
        
        if (token == null) {
            System.out.println("Token cannot be null.");
            return false;
        }
        
        // FIXED: Uses .equals() for proper string value comparison
        boolean isValid = token.equals(secret);
        
        System.out.println("Token validity: " + isValid);
        return isValid;
    }

    public static void main(String[] args) {
        bug3_fixed auth = new bug3_fixed();
        String input = new String("SUPER_SECRET_TOKEN");
        auth.validateToken(input); // Now correctly returns true
    }
}
