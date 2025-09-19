T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    def bubble_sort(a, N):
        for i in range(N-1, 0, -1):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
    bubble_sort(a, N)
    print(f"#{tc + 1}", *a)