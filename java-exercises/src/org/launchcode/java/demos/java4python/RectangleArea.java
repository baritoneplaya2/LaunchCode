//Class 1 Prep Exercise #2
package org.launchcode.java.demos.java4python;

import java.util.Scanner;

public class RectangleArea {
    public static void main(String[] args) {
        double side1;
        double side2;
        double areaOfRectangle;
        Scanner in;
        // Initiate a new Scanner for the input
        in = new Scanner(System.in);
        // Use System.out.println to do the input question
        System.out.println("\nWhat is one of the dimensions of the rectangle? ");

        side1 = in.nextDouble();

        System.out.println("\nWhat is the other dimension of the rectangle? ");

        side2 = in.nextDouble();
        //do the math
        areaOfRectangle = side1 * side2;
        // Use System.out.println to say Hello with the name from the input answer
        System.out.println("The area of your rectangle is: " + areaOfRectangle);
    }
}
