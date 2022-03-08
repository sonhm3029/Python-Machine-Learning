# Numpy note

# I. Vector (mảng)

## Tạo mảng:

```Python
import numpy as np

Arr = np.array([2,3,4,5,1,6,7]);
# hoac
Arr1 = np.array([2,3,4,1,2,5,],dtype="kdl");

#mảng 2 chiều
Arr2 = np.array([[1,2,3],[4,5,6]],dtype...);
```

`kdl` là kiểu dữ liệu, gồm:

- `i` - integer
- `b` - boolean
- `u` - unsigned integer
- `f` - float
- `c` - complex float
- `m` - timedelta
- `M` - datetime
- `O` - object
- `S` - string
- `U` - unicode string
- `V` - fixed chunk of memory for other type ( void )

hoặc thay `"kdl"` bằng `int`, `str`, `float`,`bool` đều được.

## Số chiều:

```Python
arr.ndim
#trả về
# 1: mảng một chièu
# 2: mảng 2 chiều
# 3: mảng 3 chiều
#...
```



## Index:

Các mảng truy cập theo index như sau:

1 chiều: như mảng bình thường

loại mảng | truy cập | giải thích
----------|----------|-----------
2 chiều|`arr[a,b]`| hàng a, cột b
3 chiều|`arr[a,b,c]`|hàng b, cột c -- phần tử index a của mảng 3 chiều

## Slicing:

1 chiều:

```Python
arr[start:end]# mặc định là 1
arr[start:end:step]
arr[:]# cả mảng
arr[::]# phần tử có index chẵn
arr[1::]# phần tử có index lẻ
arr[-1]# phần tử cuối mảng
```

2 chiều:

```Python
arr[hàng,cột]
arr[start:end,start:end]
...# tương tự như 1 chiều
```

## Copy và View

```Python
arr = np.array([1,2,3,3,4]);

x = arr.view();
y = arr.copy();
```

`x` là mảng view, tức là `x` thay đổi => `arr` thay đổi và ngược lại.

`y` là một copy, độc lập với `arr` tức là việc thay đổi hay bất cứ việc gì của `y` không liên quan đến `arr`

```Python

x.base# trả về mảng
y.base# trả về None
```

Vậy `.base` đối với `view` trả về chính nó, `.base` của `copy` trả về `None`.

## Phép toán với mảng

```Python
arr = np.array([1,2,3,4,5])

x = 2**arr# kết quả là mảng [2^1, 2^2, 2^3,...]
```

```Python
x = arr**2# kết quả là mảng [1^2, 2^2, 3^2...]
```

```Python
x = arr*2# kết quả là [1*2, 2*2, 3*2...]

```

Tương tự với các phép toán khác.

## Array Shape

```Python
arr.shape

#ví dụ
arr([1,2,3,4]) # (4,)
arr([[1,2,3],[1,2,3]]) # (2,3) - 2 hàng 3 cột
arr([[[1],[2],[3]]])
 # (1,3,1) - mảng 3 chiều có 1 phần từ - phẩn tử này có 3 mảng 2 chiều, mỗi mảng 2 chiều có một phần tử.
```

```Python
arr = np.array([[1,2],[3]])
print(arr.shape)
# (2,)
```

Đây là cách tạo không hợp lệ nhưng nếu in thì vẫn ra thế kia tức là coi như `[1,3]` =>> mảng 1 chiều 2 phần tử

## Join

Dùng hàm `.concatenate((arr1,arr2,arr3...),axis=?)`

Tham số `axis` là `0` hoặc `1`, với `0` là join theo cột, `1` là join theo hàng. Nếu không có tham số `axis` thì mặc định là `0`, join theo cột.

Với mảng một chiều thì chỉ có `axis=0`, không cần truyền gì hết.

```Python

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
# kq: [1,2,3,4,5,6]
```

```Python
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
# [
#   [1,2,5,6],
#   [3,4,7,8]
#  ]
```

Giải thích `arr1` có 2 hàng `[1,2]` và `[3,4]`, `arr2` có 2 hàng `[5,6]` và `[7,8]`. Vậy `axis=0` join theo hàng sẽ join `[1,2]` với `[5,6]` ( hàng có index 0).

join `[3,4]` và `[7,8]` (Hàng có index 1).

Nếu ví dụ trên với `axis = 0` Thì join theo cột 

Biểu diễn hình dạng ma trận:

```Python
 1 2  và 5 6
 3 4     7 8

```

Vậy join cột như sau: cột 1-3-5-7 ( lưu ý join thành 1 cột), cột 2-4-6-8

==> Kết quả:

```Python
[
    [1,2],
    [3,4],
    [5,6],
    [7,8]
]
```

Hoặc có thể nói như sau: `0` là Join theo thứ tự đi từ ma trận cha vào, `1` từ ma trận con vào.

Như vậy đối với axis `0` đi từ ma trận cha thì giống như join ma trận 1 chiều thành một ma trận cha gồm 2 chiều gồm `[1,2],[3,4],[5,6],[7,8]`

Đối với axis `1` đi từ ma trận con vào thì join các mảng 1 chiều cùng index...


## Nhân hai mảng (vector)

Hai mảng nhân với nhau cần cùng số chiều. Nhân hai mảng tương đương với việc tính tích vô hướng của 2 vecto

```Python
x = np.arange(3) # [0,1,2]
y = np.ones(3) # [1,1,1]

z = x*y #0*1 + 1*1 + 1*2 = 3

```

Hoặc

```Python
z = np.dot(x,y)
```

Hoặc

```Python
z = x.dot(y)
```

Nói chung, các phép toán cho mảng 2 chiều với nhau là element wise, tức là từng cặp phần tử cùng vị trí với nhau.

# II. Ma trận

![np-1](../img/np-1.png)

## Chú ý truy cập ma trận

```Python
A >> array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

```Python
>>> A[[0, 2], -1] # the first and the third elements in the last column
## A[0,-1] và A[2,-1]
array([ 4, 12])
```

```Python
>>> A[[1, 2]][:, [0,3]]
array([[ 5,  8],
       [ 9, 12]])
```

Được hiểu như sau: lấy ra 2 hàng có chỉ số `1` và `2` của A. Ví dụ là ma trận B

```Python
B = [
    [1,2,3,4]
    [5,6,7,8]
]
```

==> Kết quả cuối cùng là `B[:,[0,3]]` tức là lấy ra các phần tử ở cột `0` và `3` của B.

**Cặp tọa độ:**

Nếu như lấy như sau:

```Python
>>> A[[1, 2], [0, 3]]
array([ 5, 12])
```

Lấy như trên thì ta sẽ được là `A[1,0]` và `A[2,3]`

```Python
>>> A[[1, 2], [0]] # equivalent to A[[1, 2], [0, 0]]
array([5, 9])
```


# Các phép toán trên ma trận (mảng nhiều chiều)

Ví dụ với các hàm `np.sum, np.min,np.max, np.mean`

```Python
import numpy as np
A = np.array([[1., 2, 3, 2], [4, 3, 7, 4], [1, 4, 2, 3]])
A
array([[ 1.,  2.,  3.,  2.],
       [ 4.,  3.,  7.,  4.],
       [ 1.,  4.,  2.,  3.]])
```

Các hàm liệt kê trên sẽ tác động lên ma trận mặc  theo `axis = 0` tức là theo cột hoặc `axis=1` theo hàng. Nếu không đề cập tới `axis` thì sẽ tác động lên toàn bộ ma trận.

```Python
>>> np.sum(A, axis = 0)
array([  6.,   9.,  12.,   9.])

"""
1+4+1 = 6
2+3+4 = 9
3+7+2 = 12
2+4+3 = 9
"""


>>> np.min(A, axis = 0)
array([ 1.,  2.,  2.,  2.])

"""
min(1,4,1) = 1
min(2,3,4) = 2
...
"""


>>> np.max(A, axis = 0)
array([ 4.,  4.,  7.,  4.])
>>> np.mean(A, axis = 0)
array([ 2.,  3.,  4.,  3.])

"""
tính trung bình cộng theo cột
"""
```

Theo `axis = 1`, theo hàng:

```Python
>>> np.sum(A, axis = 1)
array([  8.,  18.,  10.])
>>> np.min(A, axis = 1)
array([ 1.,  3.,  1.])
>>> np.max(A, axis = 1)
array([ 3.,  7.,  4.])
>>> np.mean(A, axis = 1)
array([ 2. ,  4.5,  2.5])
```

Khi không đề cập đến `axis` thì tính theo cả ma trận:

```Python
>>> np.sum(A)
36.0
>>> np.min(A)
1.0
>>> np.max(A)
7.0
>>> np.mean(A)
3.0
```

**Chú ý**

### keepdims = True

Đôi khi, để thuận tiện cho việc tính toán về sau, chúng ta muốn kết quả trả về khi `axis = 0` là các vector hàng thực sự, khi `axis = 1` là các vector cột thực sự. Để làm được việc đó, Numpy cung cấp thuộc tính `keepdims = True` (mặc định là `False`). Khi `keepdims = True`, nếu sử dụng `axis = 0`, kết quả sẽ là một mảng hai chiều có chiều thứ nhất bằng 1 (coi như ma trận một hàng). Tương tự, nếu sử dụng `axis = 1`, kết quả sẽ là một mảng hai chiều có chiều thứ hai bằng 1 (một ma trận có số cột bằng 1). Việc này, về sau chúng ta sẽ thấy, quan trọng trong nhiều trường hợp đặc biệt:

```Python
>>> np.sum(A, axis = 0, keepdims = True)
array([[  6.,   9.,  12.,   9.]])
>>> np.mean(A, axis = 1, keepdims = True)
array([[ 2. ],
       [ 4.5],
       [ 2.5]])
```

## Các phép toán của ma trận với một số vô hướng tác động lên từng phần tử của ma trận giống như đối với mảng một chiều;

```Python
>>> import numpy as np 
>>> A = np.array([[1, 3], [2, 5]])
>>> A
array([[1, 3],
       [2, 5]])
>>> A + 2
array([[3, 5],
       [4, 7]])
>>> A*2
array([[ 2,  6],
       [ 4, 10]])
>>> 2**A
array([[ 2,  8],
       [ 4, 32]])
```

## Các phép toán giữa hai ma trận cũng giống như với mảng 1 chiều,là element wise, thực hiện trên từng cặp phần tử và kết quả là một ma trận cùng kích thước.

```Python
>>> import numpy as np 
>>> A = np.array([[1., 5], [2, 3]])
>>> B = np.array([[5., 8], [7, 3]])
>>> A*B
array([[  5.,  40.],
       [ 14.,   9.]])
>>> A**B
array([[  1.00000000e+00,   3.90625000e+05],
       [  1.28000000e+02,   2.70000000e+01]])
```

**Chú ý:** `A*B` không phải là tích giữa 2 ma trận như trong đại số mà là tích theo `element wise` như đã nói ở trên.