import java.io.*;

public class FileProcessor {
    public void processLegacyFile(String filename) {
        // Method to process text files.
        // Needs careful resource management.
        try {
            File myFile = new File(filename);
            // BUG: BufferedReader is created but NOT closed.
            // This causes a memory/resource leak.
            BufferedReader br = new BufferedReader(new FileReader(myFile));
            
            String content = br.readLine();
            System.out.println("Line: " + content);
            
            // Should have called br.close() here.
        } catch (FileNotFoundException e) {
            System.out.println("File not found error.");
        } catch (IOException e) {
            System.out.println("Reading error.");
        }
    }
}
