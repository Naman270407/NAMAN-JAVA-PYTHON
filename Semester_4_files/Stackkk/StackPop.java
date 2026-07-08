package Semester_4_files.Stackkk;

class StackPop {
    public static void main(String args[]) {

        int stack[] = {10,20,30,40,50};
        int top = 4;

        System.out.println("Top element before pop: " + stack[top]);

        if(top == -1)
        {
            System.out.println("Stack Underflow");
        }
        else
        {
            System.out.println("Deleted element: " + stack[top]);
            top = top - 1;
        }

        System.out.println("New top element: " + stack[top]);

    }
}
