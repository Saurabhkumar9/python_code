import numpy as np

# =============================================
# NUMPY 100 FUNCTIONS - Hindi + English Comments
# =============================================

# 1. List ko NumPy array me convert karna | Convert list to NumPy array
arr = np.array([1, 2, 3, 4])

# 2. 0 se 10 tak 2 step se numbers banana | Create numbers from 0 to 10 with step 2
np.arange(0, 10, 2)

# 3. 0 se 10 ke beech 5 equal values banana | Create 5 equally spaced values between 0 and 10
np.linspace(0, 10, 5)

# 4. 5 zero values ka array banana | Create array of 5 zeros
np.zeros(5)

# 5. 5 one values ka array banana | Create array of 5 ones
np.ones(5)

# 6. Sabhi values 10 se fill karna | Fill array with value 10
np.full(5, 10)

# 7. 3x3 identity matrix banana | Create 3x3 identity matrix
np.eye(3)

# 8. Random decimal values generate karna | Generate random decimal values between 0 and 1
np.random.rand(5)

# 9. Random integer values generate karna | Generate random integer values between 1 and 10
np.random.randint(1, 10, 5)

# 10. Random ek value select karna | Randomly select one value from list
np.random.choice([10, 20, 30])

# 11. Array ko random shuffle karna | Randomly shuffle array elements
a = np.array([1, 2, 3, 4])
np.random.shuffle(a)

# 12. Array ka shape dekhna | Check shape (rows, columns) of array
arr.shape

# 13. Array kitne dimension ka hai | Check how many dimensions the array has
arr.ndim

# 14. Total elements count karna | Count total number of elements in array
arr.size

# 15. Data type dekhna | Check data type of array elements
arr.dtype

# 16. Shape change karna | Reshape array to 2 rows and 3 columns
np.arange(6).reshape(2, 3)

# 17. Multi-dimensional array ko 1D banana | Flatten multi-dimensional array to 1D
np.arange(6).reshape(2, 3).flatten()

# 18. Sabhi values ka sum nikalna | Calculate sum of all elements
np.sum(arr)

# 19. Average nikalna | Calculate average (mean) of all elements
np.mean(arr)

# 20. Middle value nikalna | Find the middle (median) value
np.median(arr)

# 21. Minimum value nikalna | Find the smallest value in array
np.min(arr)

# 22. Maximum value nikalna | Find the largest value in array
np.max(arr)

# 23. Maximum value ka index nikalna | Find index position of maximum value
np.argmax(arr)

# 24. Minimum value ka index nikalna | Find index position of minimum value
np.argmin(arr)

# 25. Array ko sort karna | Sort array in ascending order
np.sort(np.array([5, 2, 8, 1]))

# 26. Variance nikalna | Calculate variance (spread) of values
np.var(arr)

# 27. Standard deviation nikalna | Calculate standard deviation of values
np.std(arr)

# 28. Square root nikalna | Calculate square root of each element
np.sqrt(arr)

# 29. Square nikalna | Calculate square of each element
np.square(arr)

# 30. Power nikalna | Raise each element to power 2
np.power(arr, 2)

# 31. Natural logarithm nikalna | Calculate natural log of each element
np.log(arr)

# 32. Exponential value nikalna | Calculate e^x for each element
np.exp(arr)

# 33. Absolute value nikalna | Convert negative values to positive
np.abs(np.array([-1, -2, 3]))

# 34. Sine value nikalna | Calculate sine of each element (in radians)
np.sin(arr)

# 35. Cosine value nikalna | Calculate cosine of each element (in radians)
np.cos(arr)

# 36. Tangent value nikalna | Calculate tangent of each element (in radians)
np.tan(arr)

# 37. Sabse badi unique value sort karke dena | Return sorted unique values (remove duplicates)
np.unique([1, 2, 2, 3, 3, 4])

# 38. Condition check karna | Find indices where condition is True
np.where(arr > 3)

# 39. True/False filter lagana | Filter elements greater than 2
arr[arr > 2]

# 40. Do arrays ko join karna | Join two arrays together
np.concatenate(([1, 2], [3, 4]))

# 41. Arrays ko vertically join karna | Stack arrays vertically (row-wise)
np.vstack(([1, 2], [3, 4]))

# 42. Arrays ko horizontally join karna | Stack arrays horizontally (column-wise)
np.hstack(([1, 2], [3, 4]))

# 43. Array ko do parts me split karna | Split array into 2 equal parts
np.split(np.array([1, 2, 3, 4]), 2)

# 44. Array copy banana | Create an independent copy of array
arr.copy()

# 45. Array view banana (original se linked) | Create a view that shares data with original
arr.view()

# 46. Values repeat karna | Repeat each element 2 times
np.repeat(arr, 2)

# 47. Tile karke pattern banana | Repeat whole array 2 times side by side
np.tile(arr, 2)

# 48. Elements count karna | Count non-zero elements in array
np.count_nonzero(arr)

# 49. Array reverse karna | Reverse the order of array elements
arr[::-1]

# 50. Array ko ascending order me sort karna | Sort array from smallest to largest
np.sort(arr)

# 51. Specific value ka index dhundhna | Find index of specific value (30) in array
np.where(arr == 30)

# 52. Array me value exist karti hai ya nahi | Check if value 30 exists in array
np.isin(30, arr)

# 53. Maximum value ko clip karna | Limit values between minimum 15 and maximum 35
np.clip(arr, 15, 35)

# 54. Array ko ascending order ke index dena | Get indices that would sort the array
np.argsort(arr)

# 55. Search insert position | Find position where 35 should be inserted to keep order
np.searchsorted(arr, 35)

# 56. Difference between consecutive elements | Calculate difference between neighboring elements
np.diff(arr)

# 57. Cumulative sum | Running total of all elements
np.cumsum(arr)

# 58. Cumulative product | Running product of all elements
np.cumprod(arr)

# 59. Product of all values | Multiply all elements together
np.prod(arr)

# 60. Round values | Round numbers to 2 decimal places
np.round([1.234, 5.678], 2)

# 61. Floor value | Round down to nearest whole number
np.floor([1.9, 2.8])

# 62. Ceil value | Round up to nearest whole number
np.ceil([1.2, 2.3])

# 63. Truncate decimal part | Remove decimal part (just cut it off)
np.trunc([1.9, 2.8])

# 64. Check NaN | Check if a value is Not a Number (NaN)
np.isnan(np.nan)

# 65. Check Infinite value | Check if a value is infinite
np.isinf(np.inf)

# 66. Replace NaN with number | Replace NaN values with 0
np.nan_to_num([1, np.nan])

# 67. Mean ignoring NaN | Calculate average while skipping NaN values
np.nanmean([1, 2, np.nan])

# 68. Sum ignoring NaN | Calculate sum while skipping NaN values
np.nansum([1, 2, np.nan])

# 69. Maximum ignoring NaN | Find max value while skipping NaN values
np.nanmax([1, np.nan, 5])

# 70. Minimum ignoring NaN | Find min value while skipping NaN values
np.nanmin([1, np.nan, 5])

# 71. Logical AND | Element-wise AND operation on two boolean arrays
np.logical_and([True, False], [True, True])

# 72. Logical OR | Element-wise OR operation on two boolean arrays
np.logical_or([True, False], [True, True])

# 73. Logical NOT | Flip True to False and False to True
np.logical_not([True, False])

# 74. Check all values true | Returns True only if ALL elements are True
np.all([True, True])

# 75. Check any value true | Returns True if AT LEAST ONE element is True
np.any([False, True])

# 76. Transpose matrix | Swap rows and columns of matrix
np.array([[1, 2], [3, 4]]).T

# 77. Matrix multiplication | Multiply two arrays element-wise and sum (dot product)
np.dot([1, 2], [3, 4])

# 78. Alternative matrix multiplication | Matrix multiplication using matmul
np.matmul([[1, 2]], [[3], [4]])

# 79. Inner product | Calculate inner product of two arrays
np.inner([1, 2], [3, 4])

# 80. Outer product | Calculate outer product (all combinations multiplied)
np.outer([1, 2], [3, 4])

# 81. Determinant of matrix | Calculate determinant of a 2x2 matrix
np.linalg.det([[1, 2], [3, 4]])

# 82. Inverse matrix | Calculate inverse of a matrix
np.linalg.inv([[1, 2], [3, 4]])

# 83. Eigen values | Calculate eigenvalues and eigenvectors of matrix
np.linalg.eig([[1, 2], [3, 4]])

# 84. Matrix rank | Find the rank (number of independent rows/cols) of matrix
np.linalg.matrix_rank([[1, 2], [3, 4]])

# 85. Solve linear equation | Solve system of linear equations Ax = b
np.linalg.solve([[2, 1], [1, 1]], [5, 3])

# 86. Identity matrix | Create 3x3 identity matrix (1s on diagonal)
np.identity(3)

# 87. Diagonal values create | Create matrix with given values on diagonal
np.diag([1, 2, 3])

# 88. Extract diagonal | Extract diagonal elements from a matrix
np.diag([[1, 2], [3, 4]])

# 89. Lower triangle | Keep only lower triangle, set upper to 0
np.tril([[1, 2], [3, 4]])

# 90. Upper triangle | Keep only upper triangle, set lower to 0
np.triu([[1, 2], [3, 4]])

# 91. Create mesh grid | Create coordinate grids from two 1D arrays
x, y = np.meshgrid([1, 2], [3, 4])

# 92. Flatten array | Flatten any shape array into 1D (like flatten but returns view)
np.ravel([[1, 2], [3, 4]])

# 93. Convert to list | Convert NumPy array to Python list
arr.tolist()

# 94. Convert datatype | Change data type of array elements to float
arr.astype(float)

# 95. Save array file | Save array to binary .npy file on disk
np.save("data.npy", arr)

# 96. Load array file | Load array from saved .npy file
np.load("data.npy")

# 97. Save text file | Save array to readable .txt file
np.savetxt("data.txt", arr)

# 98. Load text file | Load array from .txt file
np.loadtxt("data.txt")

# 99. Memory bytes used | Check how many bytes the array uses in memory
arr.nbytes

# 100. Create copy of array | Create a complete independent copy of array
np.copy(arr)


# =============================================
# ADVANCED NUMPY FUNCTIONS (101 onwards)
# =============================================

# 101. Cross product | Calculate cross product of two vectors
np.cross([1, 0, 0], [0, 1, 0])

# 102. Gradient nikalna | Calculate gradient (rate of change) of array
np.gradient([1, 4, 9, 16, 25])

# 103. Linear interpolation | Find value between known data points
np.interp(2.5, [1, 2, 3], [10, 20, 30])

# 104. Convolution | Combine two arrays using convolution (used in signal/image processing)
np.convolve([1, 2, 3], [0, 1, 0])

# 105. Fast Fourier Transform | Convert signal from time domain to frequency domain
np.fft.fft([1, 2, 3, 4])

# 106. Inverse FFT | Convert frequency domain back to time domain
np.fft.ifft([1, 2, 3, 4])

# 107. FFT frequencies | Return frequency values for FFT output
np.fft.fftfreq(4, d=1.0)

# 108. Vector/Matrix norm | Calculate length/magnitude of vector or matrix
np.linalg.norm([3, 4])

# 109. Singular Value Decomposition | Decompose matrix into 3 parts (used in ML)
np.linalg.svd([[1, 2], [3, 4]])

# 110. QR decomposition | Decompose matrix into Q and R matrices
np.linalg.qr([[1, 2], [3, 4]])

# 111. Cholesky decomposition | Decompose positive definite matrix (used in stats)
np.linalg.cholesky([[4, 2], [2, 3]])

# 112. Matrix power | Raise a matrix to the power of n
np.linalg.matrix_power([[1, 2], [3, 4]], 2)

# 113. Trace of matrix | Sum of diagonal elements of matrix
np.trace([[1, 2], [3, 4]])

# 114. Pad array | Add extra values around the edges of an array
np.pad([1, 2, 3], pad_width=2, mode='constant', constant_values=0)

# 115. Squeeze | Remove dimensions of size 1 from array shape
np.squeeze(np.array([[[1, 2, 3]]]))

# 116. Expand dims | Add a new dimension to array at given position
np.expand_dims(np.array([1, 2, 3]), axis=0)

# 117. Broadcast arrays | Make two arrays same shape for operations
a, b = np.broadcast_arrays([1, 2, 3], [[1], [2], [3]])

# 118. Apply function along axis | Apply a function along rows or columns
np.apply_along_axis(np.sum, axis=0, arr=[[1, 2], [3, 4]])

# 119. Vectorize a function | Convert a regular Python function to work on arrays
f = np.vectorize(lambda x: x ** 2 + 1)
f(np.array([1, 2, 3]))

# 120. Piecewise function | Apply different functions based on conditions
np.piecewise(np.array([1, 2, 3, 4]),
             [np.array([1, 2, 3, 4]) < 3, np.array([1, 2, 3, 4]) >= 3],
             [lambda x: x * 2, lambda x: x * 10])

# 121. Select from choices | Choose values based on multiple conditions
np.select([arr < 2, arr >= 2], [arr * 10, arr * 100])

# 122. Histogram | Count how many values fall in each bin/range
np.histogram([1, 2, 1, 3, 4, 2, 1], bins=4)

# 123. Histogram 2D | 2D frequency count of two arrays
np.histogram2d([1, 2, 3], [4, 5, 6], bins=2)

# 124. Bincount | Count occurrences of each integer value
np.bincount([0, 1, 1, 2, 2, 2, 3])

# 125. Digitize | Find which bin each value belongs to
np.digitize([1.5, 2.5, 3.5], bins=[1, 2, 3, 4])

# 126. Percentile | Find value at given percentile (e.g., 50th = median)
np.percentile([1, 2, 3, 4, 5], 50)

# 127. Quantile | Find value at given quantile (0 to 1 scale)
np.quantile([1, 2, 3, 4, 5], 0.25)

# 128. Correlation coefficient | Measure how strongly two arrays are related
np.corrcoef([1, 2, 3], [4, 5, 6])

# 129. Covariance matrix | Measure how two arrays vary together
np.cov([1, 2, 3], [4, 5, 6])

# 130. Polynomial fit | Fit a polynomial curve to data points
np.polyfit([1, 2, 3], [1, 4, 9], deg=2)

# 131. Polynomial evaluate | Calculate polynomial value at given points
np.polyval([1, 0, 0], [1, 2, 3])

# 132. Polynomial roots | Find roots (zeros) of a polynomial
np.roots([1, -3, 2])

# 133. Flip array left-right | Mirror array horizontally
np.fliplr([[1, 2, 3], [4, 5, 6]])

# 134. Flip array up-down | Mirror array vertically
np.flipud([[1, 2, 3], [4, 5, 6]])

# 135. Rotate 90 degrees | Rotate matrix by 90 degrees
np.rot90([[1, 2], [3, 4]])

# 136. Roll array | Shift elements in array by given number of positions
np.roll([1, 2, 3, 4, 5], shift=2)

# 137. Insert elements | Insert values at specific positions in array
np.insert([1, 2, 3], obj=1, values=99)

# 138. Delete elements | Remove elements at specific positions
np.delete([1, 2, 3, 4], obj=1)

# 139. Append to array | Add values at end of array
np.append([1, 2, 3], [4, 5])

# 140. Set difference | Elements in first array but not in second
np.setdiff1d([1, 2, 3, 4], [2, 4])

# 141. Set intersection | Common elements in both arrays
np.intersect1d([1, 2, 3], [2, 3, 4])

# 142. Set union | All unique elements from both arrays combined
np.union1d([1, 2, 3], [3, 4, 5])

# 143. Check sorted | Check if array is already sorted
np.all(np.diff([1, 2, 3, 4]) >= 0)

# 144. Partition array | Partially sort array around a pivot index
np.partition([3, 1, 4, 1, 5, 9], kth=3)

# 145. Argpartition | Get indices for partially sorted array
np.argpartition([3, 1, 4, 1, 5, 9], kth=3)

# 146. Lexsort | Sort by multiple keys (like sorting by column in table)
np.lexsort(([1, 2, 1], [3, 1, 2]))

# 147. Unravel index | Convert flat index to multi-dimensional index
np.unravel_index(5, shape=(3, 3))

# 148. Ravel multi index | Convert multi-dimensional index to flat index
np.ravel_multi_index((1, 2), dims=(3, 3))

# 149. Indices of array | Return index arrays for each dimension
np.indices((3, 3))

# 150. Moving window view | Create overlapping windows of array (for sliding window ops)
np.lib.stride_tricks.sliding_window_view(np.array([1, 2, 3, 4, 5]), window_shape=3)