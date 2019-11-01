package org.launchcode.java.demos;
import java.util.stream.*;

/**
 * Created by LaunchCode
 */
public class Arrays {

    public static void main(String[] args) {

        System.out.println("printArrayOfNumbers :: ");
        printArrayOfNumbers();

        System.out.println("arrayCreation :: ");
        arrayCreation();
        //Class 2 Prep Exercise #1
        System.out.println("evenNumsAdded :: ");
        evenNumsAdded();
        //Class 2 Prep Exercise #2
        System.out.println("fiveLetterWords :: ");
        fiveLetterWords();
        //Class 2 Prep Exercise #3
        System.out.println("someValues :: ");
        someValues();

    }

    public static void printArrayOfNumbers() {

        // Declare and initialize an array of integers
        int[] numbers = {1, 2, 6, 9, 10, 14, 17, 20, 24, 42, 45, 85};

        // Loop over the array and print each number
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }

    public static void arrayCreation() {

        // Declare and initialize an empty array of 10 Integers
        int[] someInts = new int[10];

        // Declare and initialize an array using an array literal
        int[] someOtherInts = {1, 1, 2, 3, 5, 8};

        // We can use a for-in loop with arrays
        for (int i : someInts) {
            System.out.println(i);
        }

        // We can loop through an array with an iterator var as well
        for (int j : someOtherInts) {
            System.out.println(j);
        }

    }

    //Class 2 Prep Exercise #1
    public static void evenNumsAdded() {
        int numbers[] = {86, 51, 62, 12, 13, 55, 82, 66, 69, 49, 21, 79};
        int sum = 0;
        for (int x : numbers) {
            if (x % 2 == 0) {
                sum = sum + x;
            }
        }
        System.out.println(sum);
    }

    //Class 2 Prep Exercise #2
    public static void fiveLetterWords() {
        String words[] = {"transport", "wider", "part", "notes", "guttural", "next", "superficial", "sincere", "grab", "squeak", "berry", "notebook", "strap", "muddled", "lively", "wheel", "stew", "trousers", "number", "changeable"};
        for (String x : words) {
            if (x.length() == 5) {
                System.out.println(x);
            }
        }
    }

    //Class 2 Prep Exercise #3
    public static void someValues() {
        int randNums[] = {1, 1, 2, 3, 5, 8};
        for (int x : randNums) {
            System.out.println(x);
        }
    }
}