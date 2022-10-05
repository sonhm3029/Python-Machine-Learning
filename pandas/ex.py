import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
df = df.sub(s, axis='index')
print(df)

# Apply
# apply function to data - apply following columns
df = df.apply(np.cumsum)
print(df)

df = df.apply(lambda x: x.max() - x.min())
print(df)


# Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))

print(s)
print(s.value_counts())

# String methods
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat", 1, 2, 3])
print(s)
print(s.str.lower())


# Merge
df = pd.DataFrame(np.random.randn(10 ,4))
print(df)
pieces = [df[:3], df[3:7], df[7:]]

print(pd.concat(pieces))

# JOIn
left = pd.DataFrame({"key":["foo", "foo"], "lval":[1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

print(pd.merge(left, right, on="key"))


# Grouping
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df)
print(df.groupby("A").sum())
print(df.groupby(["A", "B"]).sum())


# Reshaping

# Stack
tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
print(tuples)