class methods{
    // With overladed methods, the name of the function must be the same
    // and the signature (parameters) must be either unique in amount 
    // or unique in placement of data types
    public static int add(int n1, int n2){
        System.out.println("add with two ints was called");
        return n1 + n2;
    }
    public static int add(int n1){
        System.out.println("add with one int was called");
        return add(n1, 2);
    }
    public static double add(double n1, double n2){
        System.out.println("add with two doubles was called");
        return n1 + n2;
    }
    public static void add(int n1, double n2){
        System.out.println("add with int and double was called");
    }
    public static void add(double n1, int n2){
        System.out.println("add with double and int was called");
    }
    public static void print_message(){
        System.out.println("Hello World");
    }
    public static void main(String[] args) {
        int addition_result = add(3, 4);

        System.out.println(addition_result);

        print_message();

        // System.out.println("Add method with two integers: " + add(3, 4));
        // System.out.println("Add method with one integers: " + add(3));
        // System.out.println("Add method with two doubles: " + add(3.0, 4.0));

        add(3, 4.5);
        add(3.0, 4);
    }
}