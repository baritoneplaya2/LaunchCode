//Class 2 Prep Exercise #4
package org.launchcode.java.demos;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class GradebookHashMap {
    public static void main(String[] args) {
        //declare and initialize variables needed for student name and student IDs
        HashMap<Integer, String> students = new HashMap<>();
        Scanner in = new Scanner(System.in);
        String newStudent;

        // Get students' names
        System.out.println("Enter your students (or ENTER to finish):");
        do {

            System.out.print("Student: ");
            newStudent = in.nextLine();

            if (!newStudent.equals("")) {
                System.out.print("Student ID: ");
                Integer studentID = Integer.parseInt(in.nextLine());
                students.put(studentID, newStudent);

                // Read in the newline before looping back
                in.nextLine();
            }
        } while(!newStudent.equals(""));


        // Print class roster
        System.out.println("\nClass roster:");
        for (Map.Entry<Integer, String> student : students.entrySet()) {
            System.out.println(student.getKey() + " (" + student.getValue() + ")");
        }
    }
}