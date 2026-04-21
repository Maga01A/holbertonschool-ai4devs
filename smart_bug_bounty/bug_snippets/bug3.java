import java.io.*;

public class FileProcessor {
    public void readFile(String path) {
        try {
            // Intended: Read file content and close resource.
            // BUG: BufferedReader is never closed, causing resource leak.
            BufferedReader reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();
            System.out.println(line);
        } catch (IOException e) {
            System.out.println("Error reading file");
        }
    }
}
