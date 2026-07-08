package Semester_4_files.Searching;

import java.util.Scanner;

public class binary_search {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        int n = sc.nextInt();
        
        int arr [] = new int [n];

        System.out.println("Enter sorted array elements : ");
        for(int i =0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter target element : ");
        int target = sc.nextInt();

        int i =0;
        int j = n-1;
        int mid = 0;
        boolean found = false;

        while(i <= j && found == false){
            mid = (i + j ) / 2;

            if(arr[mid] == target ){
                found = true;
                System.out.println("Element found at index " + mid);
            }

            else if(arr[mid] < target){
                i = mid + 1;
            }

            else{                                                           //   (arr[mid] > target )
                j = mid - 1;
            }
        }

        if(found == false ){
            System.out.println("Element not found ");
        }

    }
}
