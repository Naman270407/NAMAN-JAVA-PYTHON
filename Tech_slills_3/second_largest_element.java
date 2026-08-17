// Given an integer array, find the second largest distinct element.

// Example:

// Input:  [10, 5, 20, 8, 20, 15]

// Output: 15

package Tech_slills_3;
import java.util.Scanner;

public class second_largest_element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        int n = sc.nextInt();
        int arr [] = new int [n];
        System.out.println("Enter elements : ");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int max1 = arr[0];
        for(int i = 1; i < n; i++){
            if (arr [i] > max1){
                max1 = arr[i];
            }
        }

        int max2 = arr[0];
        for(int i = 0; i < n; i++){
            if (arr[i] > max2 && arr[i] < max1){
                max2 = arr[i];
            }
        }

        System.out.println("largest : "  + max1);
        System.out.println("Second largest : " + max2);
    }
}
