package Technical_skills;
import java.util.Scanner;

public class every_row_sum {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows : ");
        int r = sc.nextInt();
        System.out.print("Enter columns : ");
        int c = sc.nextInt();

        int[][] a = new int[r][c];
        System.out.println("Enter matrix elemnts : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        System.out.println("Matrix is:");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < r; i++) {
            int sum = 0;
            for (int j = 0; j < c; j++) {
                    sum = sum + a[i][j];
            }
            System.out.println("Sum of row number : " + sum);
        }
    }
}
