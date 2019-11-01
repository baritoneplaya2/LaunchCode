//Class 1 Prep Exercise #3
package org.launchcode.java.demos.java4python;

import java.util.Scanner;

public class MilesPerGallon {
    public static void main(String[] args) {
        double miles;
        double gallonsOfGas;
        double milesPerGallon;
        Scanner in;
        // Initiate a new Scanner for the input
        in = new Scanner(System.in);
        // Use System.out.println to do the input question
        System.out.println("\nHow many miles have you driven? ");
        miles = in.nextDouble();

        System.out.println("\nHow many gallons of gas did you consume? ");
        gallonsOfGas = in.nextDouble();

        //do the math
        milesPerGallon = miles / gallonsOfGas;
        // Use System.out.println to say Hello with the name from the input answer
        System.out.println("Your car does " + milesPerGallon + " miles per gallon.");
    }
}
