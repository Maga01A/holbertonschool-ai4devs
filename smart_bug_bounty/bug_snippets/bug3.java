public class Auth {
    public boolean checkToken(String input, String secret) {
        if (input == secret) { // Wrong: reference comparison
            return true;
        }
        return false;
    }
}
