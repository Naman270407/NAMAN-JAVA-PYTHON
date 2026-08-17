package Tech_slills_3;

import java.util.Scanner;
public class String_palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = new String();
        System.out.println("Enter String : ");
        str = sc.nextLine();
        int i = 0;
        int j = str.length() - 1;
        boolean ispalindrom = true;
        while(i<j && ispalindrom == true)
            {
            if(str.charAt(i)!=str.charAt(j))
            {
                ispalindrom = false;
                break;
            }
            i = i+1;
            j = j-1;
        }
            if(ispalindrom == true){
                System.out.println("Palindrom");
            }
            else{
                System.out.println("Not Palindrom");
            }
    }
}
