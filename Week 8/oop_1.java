class Dog{
    private boolean rabbid;
    private String name;
    private double weight;
    private int id;
    static int id_count = 1;

    public Dog(){
        name = "While";
        weight = 1.0;
        this.id = id_count;
        rabbid = true;

        id_count++;
    }

    public Dog(String name, double weight){
        this.name = name;
        this.weight = weight;
        this.id = id_count;
        rabbid = false;

        id_count++;
    }

    public String get_name(){
        return name;
    }

    public void set_name(String name){
        if(name.equals("Alice")){
            System.out.println("That name is not valid");
        }
        else{
            this.name = name;
        }
    }

    public int get_id(){
        return id;
    }
}

public class oop_1 {
    public static void print_message(){
        System.out.println("Hello World");
    }
    public static void main(String[] args) {
        Dog d1 = new Dog("Bob", 14);
        Dog d2 = new Dog("None", 20);
        Dog d3 = new Dog("For Loop", 10);
        Dog d4 = new Dog();

        System.out.println(d1.get_name() + ", ID: " + d1.get_id());
        
        d1.set_name("Alice");
        
        System.out.println(d1.get_name() + ", ID: " + d1.get_id());
        
        d1.set_name("Null");

        System.out.println(d1.get_name() + ", ID: " + d1.get_id());

        print_message();

        System.out.println("Printing out the dogs...");
        System.out.println(d1.get_name() + ", ID: " + d1.get_id());
        System.out.println(d2.get_name() + ", ID: " + d2.get_id());
        System.out.println(d3.get_name() + ", ID: " + d3.get_id());
        System.out.println(d4.get_name() + ", ID: " + d4.get_id());
    }
}
