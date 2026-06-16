class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores (temperature, index)

        for i, t in enumerate(temperatures):
            print(f"\n--- Iteration {i} ---")
            print(f"Current temperature: {t}")
            print(f"Stack before processing: {stack}")
            print(f"Result before processing: {res}")

            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()

                days_waited = i - stackInd
                res[stackInd] = days_waited

                print(
                    f"  {t} is warmer than {stackT} "
                    f"from index {stackInd}"
                )
                print(f"  Popped: ({stackT}, {stackInd})")
                print(
                    f"  res[{stackInd}] = "
                    f"{i} - {stackInd} = {days_waited}"
                )
                print(f"  Stack after pop: {stack}")
                print(f"  Result after update: {res}")

            stack.append((t, i))

            print(f"Pushed ({t}, {i})")
            print(f"Stack after iteration: {stack}")
            print(f"Result after iteration: {res}")

        print("\nFinal unresolved stack:", stack)
        print("Final result:", res)

        return res


# temperatures=[30,38,30,36,35,40,28]


