import hashlib
import timeit

# 1 KB of data
data = b"A" * 1024  # 1024 bytes = 1 KB

def hash_md5():
    hashlib.md5(data).digest()

def hash_sha1():
    hashlib.sha1(data).digest()

# Number of iterations for timing
iterations = 100_000

# Measure MD5
md5_time = timeit.timeit(hash_md5, number=iterations)
# Measure SHA1
sha1_time = timeit.timeit(hash_sha1, number=iterations)

print(f"SHA1 average time per hash: {md5_time / iterations * 1e6:.3f} µs")
print(f"MD5 average time per hash: {sha1_time / iterations * 1e6:.3f} µs")