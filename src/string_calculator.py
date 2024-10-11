class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers.split("\n", 1)[1]

        numbers = numbers.replace("\n", delimiter)
        nums = map(int, numbers.split(delimiter))
        return sum(nums)
