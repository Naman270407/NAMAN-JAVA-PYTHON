// check if a number is divisible by 3 and last digit is 4.

package leet_code.CP.Control_Statment;


import java.util.Scanner;

public class div_by_3_and_ld_is_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number : ");
        int n = sc.nextInt();

        if (n % 10 == 4 && n % 3 == 0) {
            System.out.println("Number is satisfied with query");
        } else {
            System.out.println("No number is not satisfied with query");
        }
    }
}
