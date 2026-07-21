public class for_loop {
    public static void main(String[] args) {
        // For loops in java are called Counting Loops
        // 1. Initialize integer variable `i` with value of 0 (int i = 0)
        // 2. Check if `i` is less than 10 => if true, execute instruction 3 (i < 10), else execute instruction 6
        // 3. Print Iteration #i
        // 4. Increment `i` by 1 (i++)
        // 5. Jump into instruction 2
        // 6. Stop
        for(int i = 0; i < 10; i++){
            System.out.println("Iteration #" + (i + 1));
        }

        System.out.println();

        String message = "Hello World";

        // In Java, we call this type of For loop a For Each loop
        for(char c : message.toCharArray()){
            System.out.print(c + ", ");
        }
    }
}
