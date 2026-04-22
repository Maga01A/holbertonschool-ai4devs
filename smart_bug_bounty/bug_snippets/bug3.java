public class StringCompare {
    public boolean checkToken(String token, String secret) {
        // BUG: Uses == instead of .equals() for String comparison
        return token == secret;
    }
}
