import java.util.Scanner;

public class Course01 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        int count=0;
        for (int i = 1; i < n; i++) {
            if(i%a!=0){
                if(i%b!=0){
                    if(i%c!=0){
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }
}
