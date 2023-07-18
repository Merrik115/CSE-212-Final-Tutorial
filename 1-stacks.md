# Stack

A stack, as a data structure, is called "Last In, First Out", which, as the name suggests, is how things are added and removed. If you need to visualize it, you can think of a stack of plates. When you wash a plate you normally place it on top of the stack. Then, when you need to use a plate, you also take it from the top of the stack. The bottom plate is the last one used.

## How to use a Stack

A stack has two main operations: `push` and `pop`. `push` adds the item to the top, also known as the back, of the stack. `pop` removes an item and returns it from the back of the stack.

In python we use `.append()` to `push` and `.pop()` to `pop`. It might look like this:

```python
stack = []
value = 15
stack.append(value)
second = 21
stack.append(second)
removed_value = stack.pop()
print(removed_value)
```

In this example, the value of `second` would be printed.

A stack has one other common operation, `len`. This is used to determin the size of the stack. In python it is found with `len()`. If we add `len` to the above code, it might look like this:

```python
stack = []
value = 15
stack.append(value)
second = 21
stack.append(second)
removed_value = stack.pop()
print(removed_value)
length = len(stack)
print(len)
```

The second printed value would be 1 as there would only be one item in the stack, `value`.

## Why use a Stack?

Stack data structures are most useful when the order is important. For example, a stack can be used to see if all the parentheses in a math problem are closed. A stack can also be used when you want a given sequence to return in reverse order.

A Benefit to using a stack is that all of the standard stack operations run at O(1).

## Example problem solved with a Stack

In this example we want to determin if a word is a palindrome. A palindrome is a word that is spelled forwards the same as it is backwards. We will solve this problem using a stack.

```python

def palindrome(word):

    stored_word = []

    for letter in word:
        stored_word.append(letter)


    for letter in word:
        if stored_word.pop() != letter:
            print(word + " is NOT a palindrome.")
            return
            
            

    print(word + " is a palindrome!")
    return

palindrome("racecar")
palindrome("start")
```

The output for this should be:

```
racecar is a palindrome!
start is NOT a palindrome.
```

## Clothing for You

Mike and Susan are running a business where they sell beds called Sleep Right. They notice that the newest beds tend to sell the best at their store. Because of this, they buy a new shipment of beds each month. Each month they sell the new beds for more. This table shows the price to sell, amount bought, and amount sold for each month. 

|   Month   | # Bought |      Price      | # Sold  |
| --------- | -------- | --------------- | ------- |
| January   |    5     |     $100 per    |    3    |
| February  |    10    |     $125 per    |    6    |
| March     |    6     |     $150 per    |    9    |
| April     |    4     |     $175 per    |    5    |
| May       |    8     |     $200 per    |    5    |
| June      |    6     |     $225 per    |    7    |

Assuming they sold their newest stock first, how much did they make total? Solve this using a stack.


You can check your code with the solution here: [Solution](problem1.py)

[Back to Welcome Page](0-welcome.md)
