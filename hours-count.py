import streamlit as st
from datetime import datetime, timedelta

def setIconPage():
    st.set_page_config(
        page_title = "Compteur d'heure Gan",
        page_icon = '24-hours.png',
        layout = 'wide'
    )

def data():
    col1, col2, col3 = st.columns(3)
    arrivalHours = col1.number_input("Heure d'arriver :",8,14,step=1)
    arrivalMin = col1.number_input("minutes d'arriver :",0,60,step=1)
    startDejHours = col2.number_input("Heure du déjeuner :",11,14,step=1)
    startDejMin = col2.number_input("minutes du déjeuner :",0,60,step=1)
    EndDejHours = col3.number_input("Heure fin de déjeuner :",11,14,step=1)
    EndDejMin = col3.number_input("Minutes fin de déjeuner :",0,60,step=1)

    button = st.button("Calculer")
    FMT = '%H:%M'

    if button :
        arrival = str(arrivalHours)+":"+str(arrivalMin)
        arrival = datetime.strptime(arrival, FMT)

        startDej = str(startDejHours)+":"+str(startDejMin)
        startDej = datetime.strptime(startDej, FMT)

        EndDej = str(EndDejHours)+":"+str(EndDejMin)
        EndDej = datetime.strptime(EndDej, FMT)

        
        morning = startDej - arrival

        st.subheader("Temps le matin : "+str(morning))

        timeToFinish = datetime.strptime("7:36", FMT) - morning

        st.subheader("Heure restante l'après-midi : "+str(timeToFinish)[11:])
        hoursToAdd = str(timeToFinish)[:4]
        minutesToAdd = str(timeToFinish)[14:16]
        hourToFinish = EndDej + timedelta(hours=int(hoursToAdd))
        hourToFinish = hourToFinish + timedelta(minutes=int(minutesToAdd))

        st.subheader("Heure de sortie minimum : "+str(hourToFinish)[11:])


def main():
    setIconPage()
    data()

if __name__ == "__main__":
    main()