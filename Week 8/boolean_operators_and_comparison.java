public class boolean_operators_and_comparison {
    public static void main(String[] args) {
        int n1 = 4;
        int n2 = 3;

        // Double equal operator or == only works when comparing primitive types
        System.out.println(n1 + " == " + n2 + " = " + (n1 == n2));
        System.out.println(n1 + " != " + n2 + " = " + (n1 != n2));
        System.out.println(n1 + " > " + n2 + " = " + (n1 > n2));
        System.out.println(n1 + " < " + n2 + " = " + (n1 < n2));
        System.out.println(n1 + " >= " + n2 + " = " + (n1 >= n2));
        System.out.println(n1 + " <= " + n2 + " = " + (n1 <= n2));

        System.out.println("AND");
        System.out.println(n1 + " != " + n2 + " && " + n1 + " != " + n2 + " = " + (n1 != n2 && n1 != n2));
        System.out.println(n1 + " != " + n2 + " && " + n1 + " == " + n2 + " = " + (n1 != n2 && n1 == n2));
        System.out.println("OR");
        System.out.println(n1 + " != " + n2 + " || " + n1 + " == " + n2 + " = " + (n1 != n2 || n1 == n2));
        System.out.println(n1 + " == " + n2 + " || " + n1 + " == " + n2 + " = " + (n1 == n2 || n1 == n2));
        System.out.println("NOT");
        System.out.println("!(" + n1 + " == " + n2 + ") = " + !(n1 == n2));

        String s1 = "Hello";
        String s2 = "World";

        System.out.println(s1.equals(s2));
    }
}
