package Semester_4_files.Stackkk;

public class StackDisplay {
    public static void main(String args[]) {

        int stack[] = {10,20,30,40,50};
        int top = 4;

        if(top == -1)
        {
            System.out.println("Stack is Empty");
        }
        else
        {
            System.out.println("Stack elements are:");

            for(int i = top; i >= 0; i--)
            {
                System.out.println(stack[i]);
            }
        }

    }
}
