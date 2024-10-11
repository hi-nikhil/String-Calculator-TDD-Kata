class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        nums = map(int, numbers.split(","))
        return sum(nums)
