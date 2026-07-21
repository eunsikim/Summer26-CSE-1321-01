import java.util.Scanner;

public class io_example {
    public static void main(String[] args) {
        // print("Hello CSE 1321", end="")
        System.out.print("Hello CSE 1321");
        System.out.println("Hello World");
        System.out.println("Hello KSU");

        // We use double-quotes to represent strings
        // We use single-quotes to represent characters
        // System.out.println('Hello KSU');

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        // String name = sc.next(); this will read up to the first blank or new line
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.println("Your name is " + name);
        System.out.println("You are " + age + " years old");
        
        System.out.println("After 10 years...");
        
        age = age + 10;
        
        System.out.println("You are " + age + " years old");
    }
}
