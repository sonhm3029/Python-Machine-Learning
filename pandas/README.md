# Pandas note

```Python
import pandas as pd
```

# Series:

Series của pandas là dạng cột của bảng với dữ liệu tạo bởi mảng một chiều

Ví dụ:

```Python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
```

Kết quả:

![series](../img/series.png)

Nếu như không truyền thêm tham số gì vào thì kết quả trả ra sẽ có dạng như trên với `0,1,2` chính là label. Có thể dùng label để truy cập đến phần tử của series:

```Python
print(myvar[0])
```

Ta có thể define label của series thông qua tham số `index` truyền vào hàm

```Python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

Kết quả:

![pandas_2](../img/pandas_2.png)

Ta có thể truy cập phần tử của series thông qua label:

```Python
print(myvar["y"])
#hoặc
print(myvar[1])
```

dùng cả 2 đều được.

## Có thể khởi tạo series bằng dictionary. Khi đó các key của dictionary chính là label:

```Python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
```

Để truy cập thì vẫn dùng `myvar["key"]` hoặc `myvar[0], myvar[1]...`

Có thể specify items nào từ dict để cho vào Series bằng cách thêm index:

```Python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```

Như vậy chỉ có 2 phần tử key `day1, day2` được cho vào trong Series.