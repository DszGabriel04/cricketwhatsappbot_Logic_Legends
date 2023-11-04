import config
import json
import requests
import pywhatkit
import pprint

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
	"X-RapidAPI-Key": config.api_key,
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

#print(type(data))
#print(type(response.text))

#print(response.)
"""

lem = pprint.pprint(data["typeMatches"][0]["seriesMatches"])
print(type(lem))

pywhatkit.sendwhatmsg_instantly(phone_num, msg, 15, True, 3)
pywhatkit.sendwhatmsg_instantly(phone_num, msg, 15, True, 3)
"""




phone_num = "+919527867744"
#msg = json.dumps(data["typeMatches"][0]["seriesMatches"])
seriesName = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["seriesName"]
#matchesList = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["seriesName"][0]
msg = seriesName #json.dumps(seriesName)

for i in range(2):
    #matchesList = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]
    seriesName = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["seriesName"]
    team1 = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchInfo"]["team1"]["teamName"]
    team2 = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchInfo"]["team2"]["teamName"]
    status = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchInfo"]["status"]

    i1_runs = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchScore"]["team1Score"]["inngs1"]["runs"]
    i1_wickets = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchScore"]["team1Score"]["inngs1"]["wickets"]
    i1_overs = data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"][i]["matchScore"]["team1Score"]["inngs1"]["overs"]

    
    msg = f""" Match: {seriesName}
        {team1} vs {team2}
        Status: {status}

        Inning 1:
        Runs : {i1_runs}
        Wickets : {i1_wickets}
        Overs : {i1_overs}
    """
    pywhatkit.sendwhatmsg_instantly(phone_num, msg, 15, True, 7)