package Technical_skills;

public class divide_product_by_ith_element {
    public static void main(String[] args) {
        int []a={1,2,3,4,5};
        int[]b=new int [a.length];
        int prod=1;
        for(int i=0;i<a.length;i++){
            prod*=a[i];

        }

        for(int i=0;i<a.length;i++){
            b[i]=prod/a[i];

        }
        for(int i:b){
            System.out.print(i+" ");
        }


    }
}

