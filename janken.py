import pyreadr

d = next(iter(pyreadr.read_r("data.WXZ2014.rda").values()))
d = d.sort_values(["id", "game", "period"])

d["p1"] = d.groupby(["id", "game"])["choice"].shift(1)
d["p2"] = d.groupby(["id", "game"])["choice"].shift(2)

p = d.dropna().groupby(["p2", "p1"])["choice"].value_counts(normalize=True).unstack()

print(p)
p.to_csv("result.csv")