import java.util.Scanner;

public class Course04 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int m=sc.nextInt();
        int n=sc.nextInt();
        int[][] dp = new int[m+2][n+2];
        for (int i = 1; i <=n; i++) {
            dp[1][i]=n-i+1;
        }
        for(int i = 2; i <= m; i++)
            if((i&1)==1){
                for(int j = n; j >= 1; j--){
                    dp[i][j] = (dp[i-1][j-1] + dp[i][j+1]) % 10000;
                }
            }
            else{
                for(int j = 1; j <= n; j++){
                    dp[i][j] = (dp[i-1][j+1] + dp[i][j-1]) % 10000;
                }
            }
        int result = (m & 1)==1 ? dp[m][1] : dp[m][n];
        System.out.println(result);
    }
}
