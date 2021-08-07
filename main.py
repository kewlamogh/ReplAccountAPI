from flask import Flask, render_template, redirect
import repluser
app = Flask('app', template_folder = "t")

@app.route("/")
def home():
  return render_template("home.html");

@app.route("/module_src")
def src():
  return redirect("https://replit.com/@AmoghTheCool/ReplAccountAPI#repluser.py");

@app.route('/@<yeet>')
def hello_world(yeet):
  try:
    replapi = repluser.ReplAPI(yeet)
  except:
    return render_template("404.html")
  repls = replapi.getRepls()
  re = []
  for i in repls:
    re.append("".join(i.keys()))
  return render_template("account.html", uname = yeet, cycles = replapi.getCycles(), name = replapi.getName(), bio = replapi.getBio(), org = replapi.getOrg(), hacker = replapi.getIsHacker(), pfp = replapi.getPfp(), toplangs = replapi.getTopLangs(), inLeaderboard = replapi.isInLeaderboard(), repls = str(re))

@app.route("/leaderboard")
def leaders():
  r = repluser.ReplAPI("AmoghTheCool");
  l = repluser.getLeaderboard(r.l);
  return render_template("leaders.html", lo = l)

@app.route("/nopfp")
def no_profile_img():
  return render_template("default-pfp.html")
app.run(host='0.0.0.0', port=8080)