# Define the sets
A = {'a', 'b', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'h', 'i', 'j', 'k', 'd', 'f'}

# a. Elements in both A and B
A_intersect_B = A & B
print("Elements in A and B:", len(A_intersect_B))

# b. Elements in B that are not in A or C
B_not_A_C = B - (A | C)
print("Elements in B that are not in A or C:", len(B_not_A_C))

# c. Showing given elements using set operations
# i. [h, i, j, k]
i = C - {'c', 'd', 'f'}  # Elements in C excluding c, d, and f
print("i:", i)

# ii. [c, d, f]
ii = C & {'c', 'd', 'f'}  # Intersection of C with given elements
print("ii:", ii)

# iii. [b, c, h]
iii = (A | B | C) & {'b', 'c', 'h'}  # Union of all sets, then intersection with given elements
print("iii:", iii)

# iv. [d, f]
iv = A & C  # Intersection of A and C
print("iv:", iv)

# v. [c]
v = C & {'c'}  # Intersection of C with {'c'}
print("v:", v)

# vi. [l, m, o]
vi = B & {'l', 'm', 'o'}  # Intersection of B with {'l', 'm', 'o'}
print("vi:", vi)
