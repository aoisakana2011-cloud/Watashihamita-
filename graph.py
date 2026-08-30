import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Yu Gothic"

d = pd.read_csv("result.csv")
n = {"p":"パー","r":"グー","s":"チョキ"}
d["過去2手"] = d.p2.map(n) + "→" + d.p1.map(n)
x = d[["p","r","s"]] * 100

ax = x.plot.barh(stacked=True, figsize=(10,6))
ax.set(yticklabels=d["過去2手"], xlim=(0,100),
       xlabel="確率", title="過去2手からの3手目それぞれの確率")
ax.legend(["パー","グー","チョキ"], loc="upper center",
          bbox_to_anchor=(.5,-.12), ncol=3)

for i,r in x.iterrows():
    l = 0
    for v in r:
        ax.text(l+v/2, i, f"{v:.1f}%", ha="center", va="center")
        l += v

plt.subplots_adjust(bottom=.18)
plt.savefig("graph.png", dpi=300)
plt.show()