import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String originalString=sc.nextLine();
        String typedOutString=sc.nextLine();
        ArrayList<Character> wornOutKeys=new ArrayList<>();

        int size=originalString.length();
        int iOriginal=0;
        int iTypedOut=0;
        while(iOriginal<size){
            boolean wornOut=false;
            char originalCh=originalString.charAt(iOriginal);
            char originalUpper=Character.toUpperCase(originalCh);
            if(iTypedOut>=typedOutString.length()){
                wornOut=true;
            }else{
                char typedOutCh=typedOutString.charAt(iTypedOut);
                char typedOutUpper=Character.toUpperCase(typedOutCh);
                if(originalUpper !=typedOutUpper){
                    wornOut =true;
                }
            }
            if(wornOut){
                if(!wornOutKeys.contains(originalUpper)){
                    wornOutKeys.add(originalUpper);
                }
                iOriginal++;
            }else{
                iOriginal++;
                iTypedOut++;
            }
        }
        for (int i = 0; i < wornOutKeys.size(); i++) {
            System.out.print(wornOutKeys.get(i));
        }
        System.out.println();
    }
}
