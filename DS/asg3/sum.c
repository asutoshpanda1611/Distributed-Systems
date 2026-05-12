#include<stdio.h>
#include<omp.h>

int main()
{
    int N, t, sum = 0;

    printf("Enter array size: ");
    scanf("%d", &N);

    int a[N];

    printf("Enter elements:\n");
    for(int i=0; i<N; i++)
        scanf("%d", &a[i]);

    printf("Enter number of processors/threads: ");
    scanf("%d", &t);

    int part[t];

    #pragma omp parallel num_threads(t)
    {
        int id = omp_get_thread_num();
        part[id] = 0;

        for(int i=id; i<N; i+=t)
            part[id] += a[i];

        printf("Processor %d sum = %d\n", id, part[id]);
    }

    for(int i=0; i<t; i++)
        sum += part[i];

    printf("Final Sum = %d\n", sum);

    return 0;
}