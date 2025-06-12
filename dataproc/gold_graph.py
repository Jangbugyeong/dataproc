import json

from match_data2 import to_extract

with open("match_0.json","r",encoding="utf-8")as f:
    data_match = json.load(f)
with open("timeline_0.json","r",encoding="utf-8")as f:
    data_timeline = json.load(f)

timeline = data_timeline[0]['info']
match = data_match[0]['info']

players = match['participants']
blue_team = {}
red_team = {}
for p in players:
    teamId = p['teamId']
    teamPosition = p['teamPosition']
    pid = p['participantId']
    if teamId == 100:
        blue_team[pid] = teamPosition
    else:
        red_team[pid] = teamPosition
    print(f"teamId = {teamId}, teamPosition = {teamPosition}, pid = {pid}")
print(f"blue_team : {blue_team}")
print(f"red_team : {red_team}")

minutes =  []
blue_score = []
red_score = []
to_extract = 'totalGold'
position = 'MIDDLE'
frames = timeline['frames']
for frame in frames:
    time = frame['timestamp']//60000
    minutes.append(time)
    blue_score_1min, red_score_1min = 0,0
    for pid, item in frame['participantFrames'].items():
        if int(pid) in blue_team:
            if blue_team[int(pid)] == position:
                blue_score_1min += item[to_extract]

            print(f"time : {time:2d}, pid : {pid:.2s}, score : {item[to_extract]} team : blue")
        else:
            if red_team[int(pid)] == position:
                red_score_1min +=item[to_extract]
            print(f"time : {time:2d}, pid : {pid:.2s}, score : {item[to_extract]} team : red")
    print(f"blue : {blue_score_1min}, red : {red_score_1min}\n")
    blue_score.append(blue_score_1min)
    red_score.append(red_score_1min)
if minutes[-1] == minutes[-2]:
    minutes[-1] = minutes[-2]+1
print(minutes)
print(blue_score)
print(red_score)

import matplotlib.pyplot as plt

plt.plot(minutes, blue_score, label=f"Blue : {to_extract}", linewidth = 2,marker = 'o')
plt.plot(minutes, red_score, label=f"Red : {to_extract}", linewidth = 2,marker = 'o')


plt.xlabel('Minutes (m)')
plt.ylabel(F"{to_extract}")
plt.title(f"Feature {to_extract} Graph")
plt.legend()
plt.grid(True)
plt.show()

diff = []
for j in range(len(minutes)):
    diff.append(blue_score[j] - red_score[j])
print(diff)
plt.plot(minutes,diff,linewidth = 2,marker = 'o')
plt.show()
