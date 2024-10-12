class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers.split("\n", 1)[1]

        numbers = numbers.replace("\n", delimiter)

        nums = [num.strip() for num in numbers.split(delimiter) if num.strip()]

        nums = list(map(int, nums))

        nums = [n for n in nums if n <= 1000000]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")

        return sum(nums)
