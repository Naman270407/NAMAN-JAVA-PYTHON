// read a number check if a number is divisible by 7 or large digit is 5.

package leet_code.CP.Control_Statment;

import java.util.Scanner;

public class div_by_7_or_ld_is_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number : ");
        int n = sc.nextInt();

        if (n % 10 == 5 || n % 7 == 0) {
            System.out.println("Number is divisible by 7 and last digit is 4");
        } else {
            System.out.println("Number is not satisfied with query");
        }
    }
}
