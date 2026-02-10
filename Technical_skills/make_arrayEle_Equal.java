package Technical_skills;


public class make_arrayEle_Equal {
    public static void main(String[] args) {
        int []a={2,4,1,3};
        int max=a[0];
        int time=0;
        for(int i=1;i<a.length;i++){
            if(max<a[i]){
                max=a[i];
            }
        }

        for(int i=0;i<a.length;i++){
            time+=max-a[i];

        }
        System.out.println(time);
    }

}

// observations-------->
// find max
//and make all element equal to the max
// for every element calculate how much it needs to increased to reach the max
// sum all those differences
