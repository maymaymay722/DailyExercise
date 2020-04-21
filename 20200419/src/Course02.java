import java.util.Scanner;

public class Course02 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String password=sc.nextLine();
        char[] c=password.toCharArray();

        for (int i = 0; i < c.length; i++) {
            if(c[i]>='a' && c[i]<='w'){
                c[i] += 3;
            }
            if(c[i]>='x' && c[i]<='z'){
                c[i] -=23;
            }
        }
        System.out.println(c);
    }
}
