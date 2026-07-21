public class if_statements {
    public static void main(String[] args) {
        int n1 = 4;
        int n2 = 3;

        if(n1 == n2){
            System.out.println(n1 + " is equal to " + n2);
        }
        else if(n1 > n2){
            System.out.println(n1 + " is greater than " + n2);
        }
        else if(n1 < n2){
            System.out.println(n1 + " is lesser than " + n2);
        }
        else{
            System.out.println(n1 + " is not equal to " + n2);
        }
    }
}
