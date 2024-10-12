class StringCalculator:
    def add(self, numbers: str) -> int:
        # If the input string is empty, return 0
        if numbers == "":
            return 0

        # Set the default delimiter to a comma
        delimiter = ","

        # Check if the input starts with a custom delimiter declaration
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers.split("\n", 1)[1]

        # Replace any newline characters in the input with the chosen delimiter
        numbers = numbers.replace("\n", delimiter)


        # Split the string into parts based on the delimiter
        parts = numbers.split(delimiter)

        # Cleaning the input
        nums = []
        for num in parts:
            cleaned_num = num.strip()
            if cleaned_num:
                nums.append(cleaned_num)

        # Convert the filtered string numbers to integers
        nums = list(map(int, nums))

        # Filter out numbers that are greater than 1,000,000
        nums = [n for n in nums if n <= 1000000]

        # Collect negative numbers
        negatives = [n for n in nums if n < 0]

        # If there are negative numbers, raise an exception with a message
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(nums)
