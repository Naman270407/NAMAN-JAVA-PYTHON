package Semester_4_files.Stackkk;


import java.util.Scanner;

public class StackPush {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        int stack[] = new int[5];
        int top = -1;

        System.out.println("Enter element to push:");

        int value = sc.nextInt();

        if (top == 4) {
            System.out.println("Stack Overflow");
        }
        else {
            top = top + 1;
            stack[top] = value;
            System.out.println("Element pushed: " + stack[top]);
        }

    }
}
