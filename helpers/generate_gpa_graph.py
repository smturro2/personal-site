import matplotlib.pyplot as plt
import numpy as np

# EDIT HERE
gpa_each_sem = np.array([3.31, 3.02, 3.82, 3.90, 3.91, 4, 3.923076923])

semester_in_college = np.arange(1,len(gpa_each_sem)+1)
gpa_cum = np.cumsum(gpa_each_sem) / semester_in_college

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
plt.plot(semester_in_college,gpa_each_sem,".-",
         markersize=12,
         color="#FF552E",
         label="Semester GPA")
plt.plot(semester_in_college,gpa_cum,"--",
         color="#13294B",
         label="Cumulative GPA")
for i in [1,2]:
    ax.annotate(str(round(gpa_each_sem[i-1],2)),xy=(i+.1,gpa_each_sem[i-1]),fontsize=18)
for i in [3,4,5]:
    ax.annotate(str(round(gpa_each_sem[i-1],2)),xy=(i-.17,gpa_each_sem[i-1]+.05),fontsize=18)
for i in [6,7]:
    ax.annotate(str(round(gpa_each_sem[i-1],2)),xy=(i-.17,gpa_each_sem[i-1]-.1),fontsize=18)
plt.xlabel("Semester in College", fontsize=18)
plt.ylabel("GPA", fontsize=18)
plt.title("GPA over Time", fontsize=24)
plt.xticks(fontsize= 18)
plt.yticks(fontsize= 18)
plt.tight_layout()
plt.legend(fontsize=18)
plt.grid()
plt.savefig("../src/static/img/gpa_by_sem")


