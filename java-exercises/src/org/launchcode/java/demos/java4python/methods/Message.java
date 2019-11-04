package org.launchcode.java.demos.java4python.methods;

/**
 * Created by LaunchCode
 */
public class Message {
// right click, down to refactor, click rename and changing all of the instances at once
    public static String getMessage(String language) {

        if (language.equals("sp")) {
            return "Hola Mundo";
        } else if (language.equals("fr")) {
            return "Bonjour le monde";
        } else {
            return "Hello World";
        }
    }
}
