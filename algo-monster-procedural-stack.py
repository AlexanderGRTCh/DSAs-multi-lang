def execute(program: list[str]) -> list[int]:
    # Executable stack function accept list[str], retyrn list[int]
    stack: list[int] = []
    for instruction in program: 
        if instruction == "peek":
            # Print top of stack
            print(stack[-1])
        elif instruction == "pop":
            # Pop top of stack
            stack.pop()
        else:
            # Else consider instruction is push int 
            # Get int
            data = instruction[5:] # Integer located on index [5 "Push 44123"
            # Push data ontop of stack
            stack.append(data)
    return stack
if __name__ == "__main__":
    program = [input() for _ in range(int(input))]
    result = execute(program)
    print(" ".join(map(str, result)))