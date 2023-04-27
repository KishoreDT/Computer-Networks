#include<stdio.h>
#include<math.h>

int sender(int arr[10],int n)
{
    int checksum,sum=0,i;
    printf("\n***SENDER SIDE***\n");
    for(i=0;i<n;i++)
    sum+=arr[i];
    printf("Sum : %d",sum);
    checksum=~sum; //1's complement of sum
    printf("\nChecksum:%d",checksum);
    return checksum;
}
void receiver(int arr[10],int n,int sch)
{
    int checksum,sum=0,i;
    printf("\n\n***RECEIVER SIDE***\n");
    for(i=0;i<n;i++)
    sum+=arr[i];
    printf("Sum:%d",sum);
    sum=sum+sch;
    checksum=~sum; //1's complement of sum
    printf("\nChecksum:%d",checksum);
}
void main()
{
    int n,sch,rch;
    printf("\nEnter size of String:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements of the array to calculate checksum:\n");
    for(int i=0;i<n;i++)
    {
    scanf("%d",&arr[i]);
    }
    sch=sender(arr,n);
    receiver(arr,n,sch);
}