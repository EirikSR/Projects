class Array:
    # Assignment 3.3

    def __init__(self, shape, *values):
        """
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        val_check = values[0]
        Array = []
        # print([shape[0], shape[1]])
        try:  # Tries to create multidimentional array
            m = shape[1]

            if len(values) != shape[0] * shape[1]:
                raise ValueError(
                    f"Number of values doesnt mach shape. Values = {len(values)}, shape = {shape[0]}"
                )

            for i in range(0, len(values)):
                if i % shape[1] == 0:  # Creates new row after columns are filled
                    Array.append([])

                if isinstance(values[i], type(val_check)):
                    Array[-1].append(values[i])
                else:
                    raise ValueError(
                        f"Not all values have same type, contains {type(values[i])} and {type(val_check)}"
                    )
        except:  # Creates 1D array
            if len(values) != shape[0]:
                raise ValueError(
                    f"Number of values doesnt mach shape. Values = {len(values)}, shape = {shape[0]}"
                )
            for i in range(0, len(values)):

                if isinstance(values[i], type(val_check)):
                    Array.append(values[i])
                else:
                    raise ValueError(
                        f"Not all values have same type, contains {type(values[i])} and {type(val_check)}"
                    )

        self.array = Array
        self.shape = shape

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        string = ""
        for x in self.array:
            string += str(x)
            string += "\n"
        return string  # + str(self.array)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if self.shape == other.shape:
            ret_array = []
            try:
                m = self.shape[1]

                for x, y in zip(self.array, other.array):
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(x[i] + y[i])
                    ret_array.append(temp)
                return ret_array
            except:
                ret_array = []
                if len(self.array) == len(other.array):
                    for i in range(0, len(self.array)):
                        ret_array.append(self.array[i] + other.array[i])
                print(ret_array)
                return ret_array

        else:
            return NotImplemented
            # raise ValueError("Array dimentions not equal; ")

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        if self.shape == other.shape:
            ret_array = []
            try:
                m = self.shape[1]

                for x, y in zip(self.array, other.array):
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(x[i] + y[i])
                    ret_array.append(temp)
                return ret_array
            except:
                ret_array = []
                if len(self.array) == len(other.array):
                    for i in range(0, len(self.array)):
                        ret_array.append(self.array[i] + other.array[i])
                print(ret_array)
                return ret_array

        else:
            return NotImplemented
            # raise ValueError("Array dimentions not equal; ")

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        if self.shape == other.shape:
            ret_array = []
            try:
                m = self.shape[1]

                for x, y in zip(self.array, other.array):
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(x[i] - y[i])
                    ret_array.append(temp)
                return ret_array
            except:
                ret_array = []
                if len(self.array) == len(other.array):
                    for i in range(0, len(self.array)):
                        ret_array.append(self.array[i] - other.array[i])
                print(ret_array)
                return ret_array

        else:
            return NotImplemented
            # raise ValueError("Array dimentions not equal; ")

    def __getitem__(self, item):
        # Returns element at int item's location
        return self.array[item]

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        if self.shape == other.shape:
            ret_array = []
            try:
                m = self.shape[1]

                for x, y in zip(self.array, other.array):
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(y[i] - x[i])  # Flipped due to right hand function
                    ret_array.append(temp)
                return ret_array
            except:
                ret_array = []
                if len(self.array) == len(other.array):
                    for i in range(0, len(self.array)):
                        ret_array.append(
                            other.array[i] - self.array[i]
                        )  # Flipped due to right hand
                print(ret_array)
                return ret_array

        else:
            return NotImplemented
            # raise ValueError("Array dimentions not equal; ")

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        ret_array = []
        try:  # Tries to multiply array with scalar
            float(other)
            try:  # Tries to multiply higher dimentional matrix with scalar
                m = self.shape[1]

                for x in self.array:
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(x[i] * other)

                    ret_array.append(temp)
                return ret_array
            except:  # Multiplies 1d array with scalar
                for i in range(0, len(self.array)):
                    ret_array.append(self.array[i] * other)
                return ret_array
        except:  # Multiplies two arrays together
            if self.shape == other.shape:  # Checks that arrays are of equal dimensions
                try:
                    m = self.shape[1]

                    for x, y in zip(self.array, other.array):
                        temp = []
                        for i in range(0, len(x)):
                            temp.append(x[i] * y[i])
                        ret_array.append(temp)
                    return ret_array
                except:  # Multiplies 1d-arrays
                    if len(self.array) == len(other.array):
                        for i in range(0, len(self.array)):
                            ret_array.append(self.array[i] * other.array[i])
                    return ret_array
            else:
                return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        ret_array = []
        try:  # Tries to multiply array with scalar
            float(other)
            try:  # Tries to multiply higher dimentional matrix with scalar
                m = self.shape[1]

                for x in self.array:
                    temp = []
                    for i in range(0, len(x)):
                        temp.append(x[i] * other)

                    ret_array.append(temp)
                return ret_array
            except:  # Multiplies 1d array with scalar
                for i in range(0, len(self.array)):
                    ret_array.append(self.array[i] * other)
                return ret_array
        except:  # Multiplies two arrays together
            if self.shape == other.shape:  # Checks that arrays are of equal dimensions
                try:
                    m = self.shape[1]

                    for x, y in zip(self.array, other.array):
                        temp = []
                        for i in range(0, len(x)):
                            temp.append(x[i] * y[i])
                        ret_array.append(temp)
                    return ret_array
                except:  # Multiplies 1d-arrays
                    if len(self.array) == len(other.array):
                        for i in range(0, len(self.array)):
                            ret_array.append(self.array[i] * other.array[i])
                    return ret_array
            else:
                return NotImplemented

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal. False otherwise.
        """

        if len(self.array) == len(other.array):
            for i in range(0, len(self.array)):
                if self.array[i] != other.array[i]:
                    return False
            return True
        else:
            raise ValueError("Array dimentions not equal")

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """

        ret_array = []
        try:
            Scalar = float(other)
            try:
                m = self.shape[1]

                for x in self.array:
                    for i in range(0, len(x)):
                        if x[i] != Scalar:
                            ret_array.append(False)
                        else:
                            ret_array.append(True)
                return ret_array

            except:
                for i in range(0, len(self.array)):
                    if self.array[i] == Scalar:
                        ret_array.append(True)
                    else:
                        ret_array.append(False)
                return ret_array

        except:
            if self.shape == other.shape:

                try:
                    m = self.shape[1]

                    for x, y in zip(self.array, other.array):

                        for i in range(0, len(x)):
                            if x[i] != y[i]:
                                ret_array.append(False)
                            else:
                                ret_array.append(True)
                    return ret_array

                except:
                    if len(self.array) == len(other.array):

                        for i in range(0, len(self.array)):
                            if self.array[i] != other.array[i]:
                                ret_array.append(False)
                            else:
                                ret_array.append(True)
                        return ret_array

            else:
                raise ValueError("Arrays of unequal dimentions")

    def mean(self):
        """Computes the mean of the array
        Only needs to work for numeric data types.
        Returns:
            float: The mean of the array values.
        """
        ret = 0
        try:
            m = self.shape[1]

            for x in self.array:
                for i in x:
                    ret += i
            return float(ret) / (self.shape[0] * m)

        except:
            for i in range(len(self.array)):
                ret += self.array[i]
            return float(ret) / len(self.array)

    def variance(self):
        """Computes the variance of the array
        Only needs to work for numeric data types.
        The variance is computed as: mean((x - x.mean())**2)
        Returns:
            float: The mean of the array values.
        """
        ret = 0
        mean = self.mean()

        try:
            m = self.shape[1]

            for x in self.array:
                for i in x:
                    ret += (i - mean) ** 2
            return float(ret / (self.shape[0] * m))
        except:
            for i in range(len(self.array)):
                ret += (self.array[i] - mean) ** 2
            return float(ret) / len(self.array)

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for numeric data types.
        Returns:
            float: The value of the smallest element in the array.
        """
        placeholder = False

        try:
            m = self.shape[1]

            for x in self.array:
                for i in x:
                    if i < placeholder or placeholder == False:
                        placeholder = i
            return placeholder
        except:
            for i in range(len(self.array)):
                if self.array[i] < placeholder or placeholder == False:
                    placeholder = self.array[i]
            return placeholder
