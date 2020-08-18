//accept n rows& columns
package pack2;
import java.util.*;
public class array_4 {
	public static void main(String[] args) {
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter Row Size ");
		int r = obj.nextInt();
		System.out.println("Enter Column Size ");
		int c = obj.nextInt();
		int a[][]= new int[r][c];
		System.out.println("Enter"+r+"x"+c+"Array values ");
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				 a[i][j] = obj.nextInt();
			}
		}
		System.out.println("Matrix Array values");
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				 System.out.print(a[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("Transpose Matrix Array Values");
		for(int i=0;i<c;i++)
		{
			for(int j=0;j<r;j++)
			{
				 System.out.print(a[i][j]+" ");
			}
			System.out.println();
		}
	}
}
