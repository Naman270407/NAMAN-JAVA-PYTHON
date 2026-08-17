
import java.util.Scanner;

public class shopping_mall_discount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int i = 1; i < 6; i++){
            System.out.println("Enter purchase amount for customer" + i + " : " );
            int PA = sc.nextInt();
            int DA , FA;
            if(PA >= 10000){
                DA = (PA*20)/100;
                FA = PA - DA;
            }
            else if (PA >= 5000 && PA < 10000){
                DA = (PA*10)/100;
                FA = PA - DA;
            }
            else if (PA >= 2000 && PA < 5000){
                DA = (PA * 5)/100;
                FA = PA - DA;
            }
            else{
                DA = 0;
                FA = PA;
            }
            System.out.println("Discount amount : " + DA);
            System.out.println("Final Amount : " + FA);
        }
    }
}
