import pyro
import pyro.distributions as dist


def marks():
    # 60% chance of completion
    lab_complete = pyro.sample("lab_complete", dist.Bernoulli(0.6))
    completed = "complete" if lab_complete.item() == 1.0 else "not complete"

    mean = {"complete": 70.0, "not complete": 55.0}[completed]
    sd = {"complete": 5.0, "not complete": 10.0}[completed]
    mark = pyro.sample("exam_mark", dist.Normal(mean, sd))
    return completed, mark.item()


for _ in range(30):
    print(marks())
