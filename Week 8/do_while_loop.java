import java.util.Scanner;

public class do_while_loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int selection = 0;

        int iteration_counter = 1;

        do{
            System.out.println("Iteration #" + iteration_counter);
            System.out.println("1. Loop again");
            System.out.println("2. Stop");
            selection = sc.nextInt();

            iteration_counter++;

            if(selection == 1){
                continue;
            }
        }
        while(selection != 2);
    }
}
