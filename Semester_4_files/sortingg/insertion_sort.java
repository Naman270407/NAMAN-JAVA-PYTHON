package Semester_4_files.sortingg;

import java.util.Scanner;

public class insertion_sort {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter array size: ");
        int n = sc.nextInt();

        int arr[] = new int[n];

        System.out.println("Enter array elements:");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        // Insertion Sort
        for(int i = 1; i < n; i++) {

            int key = arr[i];   // current element
            int j = i - 1;

            // bigger elements shift karna
            while(j >= 0 && arr[j] > key){
                arr[j + 1] = arr[j];
                j--;
            }

            // key ko correct place pe insert
            arr[j + 1] = key;
        }

        System.out.println("Sorted array:");
        for(int i = 0; i < n; i++){
            System.out.print(arr[i] + " ");
        }

        sc.close();
    }
}
