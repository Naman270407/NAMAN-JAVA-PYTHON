// A sparse matrix is a matrix where most elements are zero
// [ 1, 0, 0 ]
// [ 0, 0, 5 ]
// [ 0, 0, 0 ]
// more than half eleemnts are 0

package Semester_4_files.two_d_array;

import java.util.Scanner;

public class sparse_matrix_or_not {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows: ");
        int r = sc.nextInt();
        System.out.print("Enter columns: ");
        int c = sc.nextInt();

        int[][] a = new int[r][c];
        int count = 0;
        System.out.println("Enter matrix:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
                if(a[i][j] == 0){
                    count = count + 1;
                }
            }
        }
        if((r*c)/2 < count){
            System.out.println("It is sparse matrix....");
        }
        else{
            System.out.println("It is not a sparse matrix...");
        }
        
        System.out.println("Matrix is:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }

    }
}
