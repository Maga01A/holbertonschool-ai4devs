import java.io.*;

public class FileProcessor {
    public void readFile(String path) {
        // FIX: Using try-with-resources for automatic closure
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line = reader.readLine();
            System.out.println(line);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
