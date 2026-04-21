import java.io.*;

public class BuggyReader {
    public void processFile(String filename) {
        try {
            // RESOURCE LEAK: BufferedReader is never closed.
            // This is a common issue in legacy Java code.
            BufferedReader br = new BufferedReader(new FileReader(filename));
            String line = br.readLine();
            System.out.println("Read: " + line);
        } catch (IOException e) {
            System.err.println("File error occurred");
        }
    }
}
