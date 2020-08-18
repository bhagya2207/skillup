package pack2;
import java.util.*;
public class array_2 {
	public static void main(String[] args) {
		Scanner obj = new Scanner (System.in);
		System.out.println("Enter array size ");
		int n=obj.nextInt();
		int a[]=new int[n];
		System.out.println("Enter "+n+" array values ");
		for(int i=0;i<n;i++)  //i is a local variable
		{
			a[i]=obj.nextInt();
		}
		System.out.println("Array values \t Index");
		for(int i=0;i<n;i++)
		{
			if(a[i]%2==0)
			{
				System.out.println(a[i]+"\t"+i);
			}
		}
	}
}
