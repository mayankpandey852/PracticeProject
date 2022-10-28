import java.util.Scanner;

public class Main{
public static void main(String []args) 
{

	System.out.println("enter two num to add");	
Scanner s=new Scanner(System.in);
int a =s.nextInt();
int b =s.nextInt();
s.close();
int c=a+b;
System.out.println("sum is: "+c);
}
}