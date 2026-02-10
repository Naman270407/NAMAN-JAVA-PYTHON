package Technical_skills;

import java.util.Scanner;

public class digonal_Ele_sumOfMatrix {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("enter no of row of matrix");
        int row=sc.nextInt();
        System.out.println("enter no of col of matrix");
        int col=sc.nextInt();

        int [][]a=new int [row][col];
        System.out.println("enter matrix elements");
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                a[i][j]=sc.nextInt();
            }
        }
        int dsum=0;

        if(row==col){
            for(int i=0;i<row;i++){
                for(int j=0;j<col;j++){
                    if(i==j) {
                        dsum +=a[i][j];

                    }
                }
            }
            System.out.println("digonal element sum is: "+dsum);

        }
        else{
            System.out.println("digonal element sum is not possible");
        }


    }
}
