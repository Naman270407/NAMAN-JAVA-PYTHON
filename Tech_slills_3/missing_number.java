// Question 2 — Missing Number in 1 to N

// Array:

// [1, 2, 3, 5, 6] only works for sorted 

// Numbers 1 to 6 hone chahiye, but ek missing hai.

// Output:

// 4

package Tech_slills_3;
import java.util.Scanner;

public class missing_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size : ");
        int n  = sc.nextInt();

        int arr[] = new int[n];

        System.out.println("Enter elements :" );
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int num = 1;
        for(int i = 0; i < n; i++){

            if(arr[i] == num){
                num ++;
            }
            else{
                System.out.println("Missinng number found : " + num);
                break;
            }
        }

    }
}
