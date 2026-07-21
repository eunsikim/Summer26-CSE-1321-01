import java.lang.Math;

public class arithmetic_operators {
    public static void main(String[] args) {
        int n1 = 4;
        int n2 = 3;

        System.out.println(n1 + " + " + n2 + " = " + (n1 + n2));
        System.out.println(n1 + " - " + n2 + " = " + (n1 - n2));
        // Notice that the division was an integer division
        System.out.println(n1 + " / " + n2 + " = " + (n1 / n2));
        System.out.println(n1 + " / " + n2 + " = " + ((double)n1 / (double)n2));
        System.out.println(n1 + " * " + n2 + " = " + (n1 * n2));

        System.out.println(20 + " % " + 2 + " = " + (20 % 2));
        System.out.println(21 + " % " + 2 + " = " + (21 % 2));

        System.out.println(n1 + "^" + n2 + " = " + (Math.pow(n1, n2)));
    }
}
