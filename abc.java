import java.util.Scanner;

public class abc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter rows for first matrix : ");
        int r = sc.nextInt();
        System.out.println("Enter columns for second matrix : ");
        int c = sc.nextInt();
        System.out.println("Enter columns for second matrix : ");
        int y = sc.nextInt();

        int[][] a = new int[r][c];
        int[][] b = new int[c][y];
        int[][] m = new int[r][y];

        System.out.println("Enter first matrix elements: ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter second matrix elements : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                b[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < y; j++) {
                m[i][j] = 0;
                for (int k = 0; k < c; k++) {
                    m[i][j] = m[i][j] + a[i][k] * b[k][j];
                }
            }
        }

        System.out.println("Multiplication matrix : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < y; j++) {
                System.out.print(m[i][j] + " ");
            }
            System.out.println();
        }

    }
}
