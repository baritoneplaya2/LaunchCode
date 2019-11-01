//Class 1 Prep Exercise #1
package org.launchcode.java.demos.java4python;

import java.util.Scanner;

/**
 * From "Java for Python Programmers"
 */
public class Hello {

    public static void main(String[] args) {
        // Initiate a new Scanner for the input
        Scanner userInputScanner = new Scanner(System.in);
        // Use System.out.println to do the input question
        System.out.println("\nWhat is your name? ");
        // String name is the type and variable for the input answer
        String name = userInputScanner.nextLine();

        System.out.println("\nHello " + name);
    }
}
