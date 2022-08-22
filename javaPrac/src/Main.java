import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String [] args){
        // primitive data structures
//        int x = 15;
//        short y = 12;
//        byte s = 12;
//        long z = 12132123L;
//        char c = 'a';

        String [] arr = new String[50];
        int [] arr2 = new int[]{1,2,3,4,5,6,7,1};

        Set<Integer> test = new HashSet<>();
        for(int i = 0 ; i<6; i++){
            test.add(i);
        }
        test.add(5);

//        System.out.println(arr);
//        Arrays.stream(arr2).forEach(System.out::println)
        System.out.println(test);
    }

}
