class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        nums = map(int, numbers.split(","))
        return sum(nums)
