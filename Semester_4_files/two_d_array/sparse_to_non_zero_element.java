package Semester_4_files.two_d_array;

import java.util.Scanner;

public class sparse_to_non_zero_element {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter rows: ");
        int r = sc.nextInt();
        System.out.print("Enter columns: ");
        int c = sc.nextInt();

        int[][] a = new int[r][c];

        System.out.println("Enter matrix elements:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        int count = 0;

        System.out.println("Matrix is:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(a[i][j] + " ");
                if(a[i][j] != 0){
                    count = count +1;
                }
            }
            System.out.println();
        }

        int [][] y = new int [count + 1][3];

        System.out.println("New matrix is : ");

        System.out.println(r + " " + c + " " + count);

        for(int i = 0; i < (count + 1); i++){
            for(int j =0; j < 3; j++){
                if(a[i][j] != 0){
                    System.out.print(i + " " + j + " " + a[i][j]);
                }
            }
            System.out.println();
        }
    }
}

//                   total row   total column     total non zero                  3 3 3
// 0 0 1             row no.       col no.         non zero element       --->    0 2 1
// 0 2 0     --->     ,,              ,,               ,,                         1 1 2
// 3 0 0               ,,             ,,                 ,,                       2 0 3
