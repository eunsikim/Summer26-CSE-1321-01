public class arrays_1 {
    public static void main(String[] args) {
        // You can initialize arrays without any value
        int[] my_numbers;

        // You can initalize arrays with initial values
        int[] my_numbers_2 = {1, 2, 3};

        // You can intialize an "empty" arrays with x amount of values  
        int[] my_numbers_3 = new int[10];

        // Arrays in Java have a fixed size/length. 

        System.out.println(my_numbers_3[0]);
        
        my_numbers_3[0] = 10;

        System.out.println(my_numbers_3[0]);

        for(int i = 0; i < my_numbers_3.length + 1; i++){
            my_numbers_3[i] = i;
        }

        for(int i : my_numbers_3){
            System.out.print(i + ", ");
        }
    }
}
