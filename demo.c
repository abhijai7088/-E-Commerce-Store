#include<stdio.h>
#include<conio.h>
int main()
{
    int Arr[10]={};
    int i;
    

    for(i=0;i<10;i++)
    {
        printf("Enter the Array Element");
    scanf("%d",&Arr);
        printf("the index of %d is %d\n",Arr[i],i);
    }
   
    return 0;
}