import java.util.Scanner;

public class Solution01 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=sc.nextInt();
        }
        int res=result(arr,n);
        System.out.println(res);
    }

    private static int result(int[] arr, int n) {
        int max=0;
        for (int i = 0; i < n; i++) {
            if(arr[i]>max){
                max=arr[i];
            }
        }
        int ans1=max-arr[0];
        int ans2=max-arr[n-1];
        if(ans1>ans2){
            return ans1;
        }else{
            return ans2;
        }
    }
}
