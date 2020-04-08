//三分搜索算法

#include <cstdio>
int a[1000], n;

bool flag;
 
int T_search(int l, int r, int x)
{
    if(l <= r)
    {
        int mid1 = l + (r - l) / 3;
        int mid2 = l + (r - l) * 2 / 3;
        if(a[mid2] < x)
            return T_search(mid2 + 1, r, x);
        else if(a[mid1] < x && a[mid2] > x)
            return T_search(mid1 + 1, mid2 - 1, x);
        else if(a[mid1] > x)
            return T_search(l, mid1 - 1, x);
        else if(a[mid1] == x)
            return mid1;
        else if(a[mid2] == x)
            return mid2;
    }
    return -1;
}

int main()
{
    int x;
    flag = false;
    printf("��������Ҫ���ҵ������ܳ��ȣ�");
    scanf("%d", &n);
    printf("��������Ӧ�����飺\n");
    for(int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("��������Ҫ���ҵ����֣�"); 
	scanf("%d", &x);
    if(T_search(0, n - 1, x) != -1)
        printf("Find\n");
    else
        printf("Not Find\n");
}

