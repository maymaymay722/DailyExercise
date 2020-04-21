import java.util.Scanner;

public class Solution01 {
    public static int findMaxGap(int[] A,int n){
        int max=0;
        for(int i=0;i<A.length;i++){
            if(A[i]>max){
                max=A[i];
            }
        }
        int ans1=max-A[0];
        int ans2=max-A[n-1];
        if(ans1>ans2){
            return ans1;
        }else{
            return ans2;
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] A=new int[n];
        for (int i = 0; i < n; i++) {
            A[i]=sc.nextInt();
        }
        int result=findMaxGap(A,5);
        System.out.println(result);
    }
}
