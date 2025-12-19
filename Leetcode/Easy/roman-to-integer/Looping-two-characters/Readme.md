## Approach

The description includes the example of **27**.  
If the values are written from left to right in descending order, we can simply add each number one by one to get the result.

### Examples

**XXVII**
```

10 (X) + 10 (X) + 5 (V) + 1 (I) + 1 (I) = 27

```

**LVIII**
```

50 (L) + 5 (V) + 1 (I) + 1 (I) + 1 (I) = 58

```

However, numbers like **4** and **9** are represented using **two Roman numerals**.

```

IV = 4
IX = 9

```

---

## ⭐ Key Idea

A single number can be formed using **one or two Roman characters**.  
Therefore, we need to determine whether to **add** or **subtract** a value.

---

## How do we decide?

We iterate through the string and compare the **current character** with the **next character**.

### Example

**Input:** `s = "XIV"`

#### Step 1: Compare `X` and `I`
- `X = 10`, `I = 1`
- Since `X > I`, the values are in descending order
- We simply add `X`

```

res = 10

```

#### Step 2: Compare `I` and `V`
- `I = 1`, `V = 5`
- Since `I < V`, this is a subtraction case

---

## Subtraction Cases

There are **six cases** where subtraction is used:

```

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900

```

In all of these cases, the **first value is smaller than the second value**.

```

I (1) + V (5) = 4
I (1) + X (10) = 9
X (10) + L (50) = 40
X (10) + C (100) = 90
C (100) + D (500) = 400
C (100) + M (1000) = 900

```

For `IV`, since `I < V`, we subtract `I` now, because `V` will be added in the next step.

```

res = 10 - 1 = 9

````

---

## Final Step

When we reach the last character, there is no next character to compare with.  
So we **add the last Roman numeral** before returning the result.

```python
return res + roman[s[-1]]
````

---

## HashMap

Before looping, we use a **HashMap** to convert Roman numerals to integers efficiently.

* `s` → input string
* `roman` → HashMap of Roman → Integer values

```
