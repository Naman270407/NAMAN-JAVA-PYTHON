// works for unsorted array
package Tech_slills_3;

import java.util.Scanner;

public class missing_num_unsorted {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter N:");
        int n = sc.nextInt();

        // N-1 elements honge
        int arr[] = new int[n - 1];

        System.out.println("Enter elements:");

        for (int i = 0; i < n - 1; i++) {
            arr[i] = sc.nextInt();
        }

        // Expected sum: 1 + 2 + 3 + ... + N
        int expectedSum = n * (n + 1) / 2;

        // Array ka actual sum
        int actualSum = 0;

        for (int i = 0; i < arr.length; i++) {
            actualSum = actualSum + arr[i];
        }

        // Expected - Actual = Missing
        int missing = expectedSum - actualSum;

        System.out.println("Missing number: " + missing);
    }
}
