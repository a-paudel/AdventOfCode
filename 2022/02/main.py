import pandas as pd

df = pd.read_csv("data.txt", sep=" ", header=None)
df.columns = ["other", "me"]

df["other"].replace("A", "rock", inplace=True)
df["other"].replace("B", "paper", inplace=True)
df["other"].replace("C", "scissors", inplace=True)

df["me"].replace("X", "rock", inplace=True)
df["me"].replace("Y", "paper", inplace=True)
df["me"].replace("Z", "scissors", inplace=True)


def shape_score(me):
    if me == "rock":
        return 1
    elif me == "paper":
        return 2
    elif me == "scissors":
        return 3


def outcome_score(other, me):
    # draw
    if other == me:
        return 3

    # win
    if other == "rock" and me == "paper":
        return 6
    elif other == "paper" and me == "scissors":
        return 6
    elif other == "scissors" and me == "rock":
        return 6

    # lose
    return 0


df["shape_score"] = df["me"].apply(shape_score)

df["outcome_score"] = df.apply(lambda x: outcome_score(x["other"], x["me"]), axis=1)


df["total_score"] = df["shape_score"] + df["outcome_score"]
print("Part 1:", df["total_score"].sum())


# rename column me to outcome
df.rename(columns={"me": "outcome"}, inplace=True)

df["outcome"] = (
    df["outcome"]
    .replace("rock", "lose")
    .replace("paper", "draw")
    .replace("scissors", "win")
)


def get_me_from_outcome(other, outcome):
    if outcome == "win":
        if other == "rock":
            return "paper"
        elif other == "paper":
            return "scissors"
        elif other == "scissors":
            return "rock"
    elif outcome == "draw":
        if other == "rock":
            return "rock"
        elif other == "paper":
            return "paper"
        elif other == "scissors":
            return "scissors"
    elif outcome == "lose":
        if other == "rock":
            return "scissors"
        elif other == "paper":
            return "rock"
        elif other == "scissors":
            return "paper"


df["me"] = df.apply(lambda x: get_me_from_outcome(x["other"], x["outcome"]), axis=1)

df["shape_score"] = df["me"].apply(shape_score)
df["outcome_score"] = df.apply(lambda x: outcome_score(x["other"], x["me"]), axis=1)
df["total_score"] = df["shape_score"] + df["outcome_score"]
print("Part 2:", df["total_score"].sum())
