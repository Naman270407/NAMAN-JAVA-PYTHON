package Semester_4_files.sortingg;

import java.util.Scanner;

public class selection_sort {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter array elements:");
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Selection Sort
        for(int i = 0; i < n-1; i++) {

            int minIndex = i;   // assume current is minimum

            // minimum find karna
            for(int j = i+1; j < n; j++) {
                if(arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // ek hi baar swap
            int t = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = t;
        }

        System.out.println("Sorted array:");
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
