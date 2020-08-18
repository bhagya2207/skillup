package pack2;
import java.util.*;
public class array_5 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter row size");
		int r = sc.nextInt();
		System.out.println("Enter column size");
		int c = sc.nextInt();
		
		int a[][]=new int[r][c];
		int b[][]=new int[r][c];
		int s[][]=new int[r][c];
		System.out.println("Enter"+r+"x"+c+"Matrix-A value");
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				a[i][j]=sc.nextInt();
			}
		}
		System.out.println("Enter"+r+"x"+c+"Matrix-B value");
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<r;j++)
			{
				b[i][j]=sc.nextInt();
			}
		}
		System.out.println("Sum of 2 Matrices");
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				s[i][j]=a[i][j]+b[i][j];
				System.out.print(s[i][j]+" ");
			}
			System.out.println();
		}
	}
}
