def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods),max(likelihoods)

def run():
    falling = likelihood()
    print(f"Minimum likelihood of falling {min(likelihood())}%")
    print(f"Maximum likelihood of falling {max(likelihood())}%")

if __name__ == "__main__":
    run()


