public class casting_and_conversions {
    public static void main(String[] args) {
        System.out.println(2.5 + 2.5);
        System.out.println(2.5 + (int)2.5);
        System.out.println((int)2.5 + (int)2.5);
        System.out.println((int)(2.5 + 2.5));
        
        // Converting a `String` into a primitive type
        int number1 = Integer.parseInt("5");
        float number2 = Float.parseFloat("3.14");

        // Converting a primitive type into a `String`
        String number3 = String.valueOf(3);
        String number4 = String.valueOf(3.3);
    }
}
