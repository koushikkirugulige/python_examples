"""
This is a intro on using map function which avoid the use of for loop
"""
import time
def check_even(num):
    """Calculates if the given number is even or not.

        Args:
            number: to check even or odd

        Returns:
            The even number (add 1 if not even).
        """
    if num%2 == 1:
        return num+1
    return num

i_p = [122,426,421,401,500,825,865,766,742]

start_time = time.time()

out = list(map(check_even, i_p))

end_time = time.time()
execution_time = end_time - start_time

print(out)
print(f"time taken for map method is :{execution_time:.6f} seconds")

start_time = time.time()
y = []
for x in i_p:
    y.append(check_even(x))
end_time = time.time()
execution_time = end_time - start_time

print(y)
print(f"time taken for loop method is :{execution_time:.6f} seconds")

"""looks like for loop performs better but map is easy to understand"""

