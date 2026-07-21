import java.util.Scanner;

public class switch_case_statements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a shape: ");
        String shape = sc.nextLine();

        switch(shape){
            case "square":
                System.out.println("You inserted a square.");
                break;
            case "triangle":
                System.out.println("You inserted a triangle.");
                break;
            default:
                System.out.println("I do not know that shape.");
                break;
        }
    }
}
