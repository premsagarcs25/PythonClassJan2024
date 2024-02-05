import sys

my_int = 92233720368547758099991222121212121211221
size_in_bytes = sys.getsizeof(my_int)

print(f"Size of the integer {my_int}: {size_in_bytes} bytes")
