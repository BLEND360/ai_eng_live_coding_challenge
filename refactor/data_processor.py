def process(df):
    df["full_name"] = df["first"] + " " + df["last"]
    df = df[df["age"] > 18]
    df["income"] = df["income"].fillna(0)
    df["status"] = "minor"
    df.loc[df["age"] >= 65, "status"] = "senior"
    df.loc[(df["age"] >= 30) & (df["age"] < 65), "status"] = "adult"
    df = df[["full_name", "age", "income", "status"]]
    df = df.sort_values(by="income", ascending=False)
    return df
