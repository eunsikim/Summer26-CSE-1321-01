public class arrays_2 {
    public static void print_array(int[] array){
        for(int x : array){
            System.out.print(x + ", ");
        }
        System.out.println();
    }
    public static int[] double_size(int[] array){
        int[] temp_array = new int[2 * array.length];

        for(int i = 0; i < array.length; i++){
            temp_array[i] = array[i];
        }

        return temp_array;
    }
    public static void main(String[] args) {
        int[] array_1 = {0, 1, 2, 3};

        print_array(array_1);

        array_1 = double_size(array_1);

        print_array(array_1);

        array_1 = double_size(array_1);

        print_array(array_1);

        array_1 = double_size(array_1);

        print_array(array_1);
    }
}
