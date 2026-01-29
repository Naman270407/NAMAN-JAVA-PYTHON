package Semester_4_files.two_d_array;

import java.util.Scanner;

public class multiplication_of_a_matrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter rows: ");
        int r = sc.nextInt();
        System.out.print("Enter columns: ");
        int c = sc.nextInt();
        System.out.println("Emter colums for second matrix: ");
        int d = sc.nextInt();

        int a[][] = new int[r][c];
        int b[][] = new int[c][d];
        int mul[][] = new int[r][d];

        System.out.println("Enter First Matrix : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter second matrix: ");
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < d; j++) {
                b[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < d; j++) {
                mul[i][j] = 0;
                for (int k = 0; k < c; k++) {
                    mul[i][j] = mul[i][j] + a[i][k] * b[k][j];
                }
            }
        }

        System.out.println("Multiplication matrix : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < d; j++) {
                System.out.print(mul[i][j] + " ");
            }
            System.out.println();
        }
    }
}
