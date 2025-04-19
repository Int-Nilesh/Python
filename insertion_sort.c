#include <stdio.h>

void insertion_sort ( int arr[], int n){
    int key, j, i;
    for ( i=1; i < n; i++){
        key = arr[i];
        j = i;
        while( j>0){
            if ( arr[j-1]> key){
                arr[j]= arr[j-1];
                j--;
            }
            else{
                arr[j]= key;
                break;
            }
        }
        if ( arr[0]>key){
            arr[0]= key;
        }
    }
    printf("sorted array :");
    for( i =0 ; i <n; i++){
        printf ("%d ",arr[i]);
    }
}
int main(){
    int arr[10];
    int n,i;
    printf(" Enter the size of array");
    scanf( "%d", &n);
    printf( "Enter Elements of array");
    for ( i = 0; i < n; i++){
        scanf("%d",&arr[i]);
    }
    insertion_sort( arr, n);
    return 0;
}