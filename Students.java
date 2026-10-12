
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Students {
    public static void main(String[] args) throws FileNotFoundException {

        // Store each student's major and GPA
        HashMap<String, String> majors = new HashMap<>();
        HashMap<String, Double> gpas = new HashMap<>();

        // Read data from the CSV file
        Scanner file = new Scanner(new File("students.csv"));

        // Skip the header row
        file.nextLine();

        while (file.hasNextLine()) {
            String line = file.nextLine();
            String[] data = line.split(",");

            String name = data[0];
            String major = data[1];
            double gpa = Double.parseDouble(data[2]);

            // Only accept GPAs between 0.0 and 4.0
            if (gpa >= 0.0 && gpa <= 4.0) {
                majors.put(name, major);
                gpas.put(name, gpa);
            }
        }

        file.close();

        // Calculate the average GPA
        double totalGpa = 0.0;

        for (double gpa : gpas.values()) {
            totalGpa += gpa;
        }

        double averageGpa = totalGpa / gpas.size();

        System.out.printf("Average GPA: %.2f%n", averageGpa);

        // Print students above average
        System.out.println("\nStudents above average:");

        for (String name : gpas.keySet()) {
            double gpa = gpas.get(name);

            if (gpa > averageGpa) {
                System.out.printf(
                    "%s - %s - GPA: %.2f%n",
                    name, majors.get(name), gpa
                );
            }
        }

        // Predict scholarship eligibility
        System.out.println("\nScholarship predictions:");

        for (String name : gpas.keySet()) {
            double gpa = gpas.get(name);
            String major = majors.get(name);

            // Simple prediction rule
            if (major.equals("Biology") || gpa >= 3.5) {
                System.out.println(
                    name + " - " + major + " - GPA: "
                    + String.format("%.2f", gpa)
                    + " - Earns a scholarship"
                );
            } else {
                System.out.println(
                    name + " - " + major + " - GPA: "
                    + String.format("%.2f", gpa)
                    + " - Does not earn a scholarship"
                );
            }
        }
    }
}
