import streamlit as st
import config
import json
import requests
import pywhatkit
import pprint



def main():

    # Requests Cricket API
    """
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
	    "X-RapidAPI-Key": config.api_key_2,
	    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    matchType = len(data["typeMatches"])
    seriesMatchType = len(data["typeMatches"][0]["seriesMatches"]) - 1
    cSeriesMatchType = len(data["typeMatches"][0]["seriesMatches"][0]["seriesAdWrapper"]["matches"])

    dataset = []
    for mb in range(matchType):
        val = []
        val.append(data["typeMatches"][mb]["matchType"])
        #print(val)
        for smt in range(seriesMatchType):
            ser = []
            #ser.append(data["typeMatches"][mb]["seriesMatches"][smt])
            ser.append(data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["seriesName"])
            #print(ser)
            for mat in range(cSeriesMatchType):
                matchdat = []
                team1 = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchInfo"]["team1"]["teamName"]
                team2 = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchInfo"]["team2"]["teamName"]
                status = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchInfo"]["status"]
                state = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchInfo"]["state"]
                
                try:
                    i1_runs = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team1Score"]["inngs1"]["runs"]
                    i1_wickets = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team1Score"]["inngs1"]["wickets"]
                    i1_overs = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team1Score"]["inngs1"]["overs"]
                except:
                    i1_runs = "NA";
                    i1_wickets = "NA";
                    i1_overs = "NA";

                try:
                    i2_runs = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team2Score"]["inngs1"]["runs"] 
                    i2_wickets = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team2Score"]["inngs1"]["wickets"]
                    i2_overs = data["typeMatches"][mb]["seriesMatches"][smt]["seriesAdWrapper"]["matches"][mat]["matchScore"]["team2Score"]["inngs1"]["overs"]
                except:
                    i2_runs = "NA";
                    i2_wickets = "NA";
                    i2_overs = "NA";

                matchdat = [team1, team2, status, state, i1_runs, i1_wickets, i1_overs, i2_runs, i2_wickets, i2_overs]
                #print(matchdat)
                datas = val + ser + matchdat
                dataset.append(datas)

    """
    #print(dataset) ## a=main data
    dataset = [['International', 'ICC Cricket World Cup 2023', 'Australia', 'England', "Complete", 'Australia won by 33 runs', 286, 10, 49.3, 253, 10, 48.1], 
               ['Domestic', 'CSA Four-Day Series Division Two 2023-24', 'Limpopo', 'Knights', "Complete", 'Day 2: Stumps - Knights lead by 187 runs', 288, 10, 93.1, 475, 4, 98.0]]
    ######


    st.title("WhatsApp Cricket Bot")
    st.text("Enter which cricket match you would like to see the scores of:")


    # Create a drop-down menu
    tourney_set = set()
    for entry in dataset:
        tourney_set.add(entry[0])

    tourney_list = list(tourney_set)    

    selected_option_1 = st.selectbox("Select What Kind of Tournament", tourney_list)
    st.write("You selected:", selected_option_1)

    sel_matches = []

    for entry in dataset:
        if(entry[0] == selected_option_1):
            sel_matches.append(entry)
    
    currMatch = []
    for entry in sel_matches:
        currMatch.append(f"{entry[2]} vs {entry[3]} -> {entry[1]}")

    selected_option_2 = st.selectbox("Select What Kind of Tournament", currMatch)
    st.write("You selected:", selected_option_2)

    main_val = currMatch.index(selected_option_2)
    main_ent = sel_matches[main_val]
    print(main_ent)
    # Add an input field for the user to enter a query
    # user_query = st.text_area("Enter your cricket option:")

    # radio button
    # first argument is the title of the radio button
    # second argument is the options for the radio button
    status = st.radio("Select whom to send it to: ", ('Whatsapp Number', 'Whatsapp Group'))
 
    # conditional statement to print 
    # Male if male is selected else print female
    # show the result using the success function
    wn = False
    wg = False

    if (status == 'Whatsapp Number'):
        #st.session_state["text"] = ""
        wn = True
        whatsapp_n = st.text_input("Enter your WhatsApp number:", key = "text")
    elif(status == "Whatsapp Group"):
        #st.session_state["text"] = ""
        wg = True
        whatsapp_n = st.text_input("Enter your WhatsApp Group:", key = "text")

    # Add a button to submit the form
    if st.button("Submit"):
        if(len(whatsapp_n) >= 10 and wn and whatsapp_n.isnumeric()):
            # You can add the code to handle the user query and WhatsApp number here
            # For example, you might process the query and send a response to the specified number
            ph_no = f"+91{whatsapp_n}"
            st.success(f"Query submitted number: {selected_option_1} :: {selected_option_2} --> {ph_no}")
        elif(len(whatsapp_n) > 0 and wg):

            gr_id = whatsapp_n[26:]
            st.success(f"Query submitted group: {selected_option_1} :: {selected_option_2} --> {gr_id}")

        else:
            st.warning("Please enter a WhatsApp number or a group link.")

if __name__ == "__main__":
    main()