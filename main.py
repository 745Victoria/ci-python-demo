def main():
    print("Hello from CI!")
    with open("result.txt", "w") as f:
        f.write("This is the generated artifact from the successful build.\n")
        f.write("Your Surname: [Підставте своє прізвище]\n")
    return 0

if __name__ == "__main__":
    exit(main())
