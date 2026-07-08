package Semester_4_files.Searching;

import java.util.Scanner;

public class linear_search {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        int n = sc.nextInt();

        int arr[] = new int [n];
        System.out.println("Enter array elements : ");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter tha target number : ");
        int t = sc.nextInt();

        boolean found = false;

        for(int i =0; i < n; i++){
            if(arr[i] == t){
                System.out.println("Element is found at index : " + i);
                found = true;
                break;
            }

        }

        if(found == false){
            System.out.println("Target not found ");
        }
    }

}
