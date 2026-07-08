package Semester_4_files.sortingg;
import java.util.Scanner;
public class bubble_sort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        int n = sc.nextInt();

        int arr[] = new int[n];

        System.out.println("Enter array elements : ");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int tom;
        for(int i = 0; i < n-1; i++){
            for(int j = 0; j < n-1-i; j++){
                if(arr[j] > arr[j + 1]){
                    tom  = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = tom;
                }
            }
        }

        System.out.println("Sorted array : ");
        for(int i = 0; i < n; i ++){
            System.out.print(arr[i] + " ");
        }
    }
}
