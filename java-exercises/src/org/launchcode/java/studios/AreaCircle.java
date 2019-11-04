package org.launchcode.java.studios;

import java.util.Scanner;

//area of a circle is A = pi * r * r where pi is 3.14 and r is the radius
public class AreaCircle {
    public static void main(String[] args) {
        double radius;
        double areaOfCircle;
        Scanner in;
        // Initiate a new Scanner for the input
        in = new Scanner(System.in);

        // Use System.out.println to do the input question
        System.out.println("\nEnter the radius of the circle: ");
        radius = in.nextDouble();
        if (radius < 1) {
            System.out.println("Please enter an acceptable value");
        }

        //do the math
        areaOfCircle = 3.14 * radius * radius;

        // Use System.out.println to say Hello with the name from the input answer
        System.out.println("The area of your circle of radius " + radius + " is: " + areaOfCircle);
    }
}
