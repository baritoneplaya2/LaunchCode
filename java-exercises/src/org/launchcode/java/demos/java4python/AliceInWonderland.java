//Class 1 Prep Exercise #4
package org.launchcode.java.demos.java4python;

import java.util.Scanner;

public class AliceInWonderland {
    public static void main(String[] args) {
        String story = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'";
        // Initiate a new Scanner for the input
        Scanner userInputScanner = new Scanner(System.in);
        // Use System.out.println to do the input question
        System.out.println("\nWhat word would you like to search for? ");
        String word = userInputScanner.nextLine();
        String searchTerm = word.toLowerCase();
        String newStory = story.toLowerCase();

        System.out.println(newStory.contains(searchTerm));
    }
}
