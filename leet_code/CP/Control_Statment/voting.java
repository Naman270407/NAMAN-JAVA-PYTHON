package leet_code.CP.Control_Statment;

import java.util.Scanner;

public class voting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int age = sc.nextInt();
        if (age >= 18) {
            System.out.println("You can vote");
        } else {
            System.out.println("You can not vote");
        }
    }
}
