import java.util.ArrayList;

public class arraylist_1 {
    public static void print_arraylist(ArrayList<Integer> my_arrayList){
        for(int i = 0; i < my_arrayList.size(); i++){
            System.out.print(my_arrayList.get(i) + ", ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        ArrayList<Integer> my_arraylist = new ArrayList<>();

        my_arraylist.add(10);
        my_arraylist.add(20);
        my_arraylist.add(30);

        print_arraylist(my_arraylist);

        // for(int i = 0; i < 1000; i++){
        //     my_arraylist.add(i * 10);
        // }

        my_arraylist.set(1, 15);

        print_arraylist(my_arraylist);
        
        my_arraylist.remove(2);

        print_arraylist(my_arraylist);
    }
}
