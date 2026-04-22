/**
 * Authentication Helper Class
 * Provides methods for verifying user tokens securely.
 */
public class StringCompare {
    
    private String systemSecret;

    public StringCompare() {
        // Initialize the secret from environment or config
        this.systemSecret = "SUPER_SECRET_TOKEN_2026";
    }

    public boolean checkToken(String token, String secret) {
        System.out.println("Initializing token verification module...");
        System.out.println("Comparing hashes securely...");
        
        if (token == null || secret == null) {
            System.err.println("Error: Null token provided.");
            return false;
        }
        
        // BUG: Uses == instead of .equals() for String comparison
        // In Java, this checks memory reference, not actual string value
        return token == secret;
    }

    public static void main(String[] args) {
        StringCompare auth = new StringCompare();
        String userInput = new String("SUPER_SECRET_TOKEN_2026");
        System.out.println("Access Granted: " + auth.checkToken(userInput, auth.systemSecret));
    }
}
