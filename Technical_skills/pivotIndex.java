package Technical_skills;

public class pivotIndex {
    public static void main(String[] args) {
        int a[]={5,5,1,6,4};
        int sum=0;
        int cur_sum=a[0];
        for(int i=0;i<a.length;i++){
            sum+=a[i];
        }

        for(int j=1;j<a.length;j++){
            cur_sum=cur_sum+a[j];
            if(sum-cur_sum==cur_sum-a[j]){
                System.out.println(j);
            }

        }
    }
}
