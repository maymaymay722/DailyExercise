import java.util.Arrays;
import java.util.Scanner;

public class Solution02 {
    public static int[] print(int[][] mat,int n,int m){
        int[] a=new int[n*m];
        int i=0,j=0,k=0;
        int startX=0;
        int startY=0;
        int endX=n-1;
        int endY=m-1;

        while((startX<=endX) && (startY<=endY)){
            if(startX==endX){
                for(;j<= endY;j++,k++){
                    a[k]=mat[startX][j];
                }
                return a;
            }

            if(startY==endY){
                for(;i<= endX;i++,k++){
                    a[k]=mat[i][startY];
                }
                return a;
            }

            for(;j<endY;j++,k++){
                a[k]=mat[i][j];
            }

            for(;i<endX;i++,k++){
                a[k]=mat[i][j];
            }

            for(;j>startY;j--,k++){
                a[k]=mat[i][j];
            }

            for(;i>startX;i--,k++){
                a[k]=mat[i][j];
            }
            i++;j++;startX++;startY++;
            endX--;endY--;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("输入m,n");
        int n=sc.nextInt();
        int m=sc.nextInt();
        System.out.println("输入数组");
        int[][] mat=new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j]=sc.nextInt();
            }
        }
        System.out.println(Arrays.toString(print(mat,n,m)));
    }
}
