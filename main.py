from __future__ import print_function
import pickle
import os.path
import PySimpleGUI as sg

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import timedelta, date

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


def errorPage(message):
    errorLayout = []
    for i in message:
        errorLayout.append(sg.Button('Error: {}'.format(i)))
    layout = [[*errorLayout],
              [sg.Button("Try Again", key="tryAgain"), sg.Button("Exit", key="exit")]]
    window = sg.Window(title="Error", layout=layout, margins=(100, 20))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "exit":
            return 1
        elif event == "tryAgain":
            return 0


def api(start_dt, end_dt, classes, color):
    # start_dt = date(2020, 8, 18)
    # end_dt = date(2020, 12, 20)
    # winter_break_start = date(2020, 12, 19)
    # winter_break_end = date(2021, 1, 3)
    # no_school_dates = ["2020-11-09", "2020-11-25", "2020-11-26", "2020-11-27", "2021-01-18", "2021-01-29", "2021-02-12",
    #                    "2021-02-15", "2021-03-08", "2021-03-09", "2021-03-10", "2021-03-11", "2021-03-12", "2021-04-02",
    #                    "2021-04-03", "2021-04-04", "2021-04-05", "2021-05-03"]
    # for dt in daterange(winter_break_start, winter_break_end):
    #     no_school_dates.append(dt.strftime("%Y-%m-%d"))
    # weekdays = [5, 6]
    # days = [1, 2, 3, 4, 5, 6, 7]
    # schooldays = []
    # for dt in daterange(start_dt, end_dt):
    #     if dt.weekday() not in weekdays:  # to print only the weekdays
    #         if dt.strftime("%Y-%m-%d") not in no_school_dates:
    #             schooldays.append(dt.strftime("%Y-%m-%d"))
    #
    # schedule = dict()
    # for i in range(len(schooldays)):
    #     j = i % 7
    #     schedule[schooldays[i]] = days[j]
    #
    # for i in schedule:
    #     print(i, ":", schedule[i])
    schedule = dict()
    with open("dates.txt") as f:
        for line in f:
            (key, val) = line.split(' : ')
            if start_dt <= key <= end_dt:
                val = val.strip()
                schedule[key] = val

    creds = None
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    for key, value in schedule.items():
        if value == '1':
            event = {
                'summary': classes[1],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId="primary", body=event).execute()

            event = {
                'summary': classes[2],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '2':
            event = {
                'summary': classes[3],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'summary': classes[4],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '3':
            event = {
                'summary': classes[5],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'summary': classes[6],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '4':
            event = {
                'summary': classes[1],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'summary': classes[0],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '5':
            event = {
                'summary': classes[2],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'summary': classes[3],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '6':
            event = {
                'summary': classes[4],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'summary': classes[5],
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

        elif value == '7':
            event = {
                'summary': classes[6],
                'start': {'dateTime': key + 'T09:00:00', 'timeZone': 'America/Chicago', },
                'end': {'dateTime': key + 'T11:50:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()

            event = {
                'start': {'dateTime': key + 'T12:50:00', 'timeZone': 'America/Chicago', },
                'summary': classes[0],
                'end': {'dateTime': key + 'T15:40:00', 'timeZone': 'America/Chicago', },
                'colorId': color
            }
            event = service.events().insert(calendarId='primary', body=event).execute()


def userInput(classes):
    global start_dt
    global end_dt
    global color
    colorList = ["Lavender", "Sage", "Grape", "Flamingo", "Banana", "Tangerine", "Peacock", "Graphite", "Blueberry",
                 "Basil", "Tomato"]
    date_layout = [[sg.T("Start Date", size=(12, 1)), sg.In(size=(12, 1), key="startDate", default_text="2021-01-04")],
                   [sg.T("End Date", size=(12, 1)), sg.In(size=(12, 1), key="endDate", default_text="2021-05-28")]]

    frame_layout = [[sg.T("Period One", size=(12, 1)), sg.In(size=(15, 1), key="pdOne")],
                    [sg.T("Period Two", size=(12, 1)), sg.In(size=(15, 1), key="pdTwo")],
                    [sg.T("Period Three", size=(12, 1)), sg.In(size=(15, 1), key="pdThree")],
                    [sg.T("Period Four", size=(12, 1)), sg.In(size=(15, 1), key="pdFour")],
                    [sg.T("Period Five", size=(12, 1)), sg.In(size=(15, 1), key="pdFive")],
                    [sg.T("Period Six", size=(12, 1)), sg.In(size=(15, 1), key="pdSix")],
                    [sg.T("Flex Class", size=(12, 1), key="flexText"),
                     sg.In(key="pdFlex", size=(15, 1), visible=False)],
                    [sg.Checkbox("I have a class during flex", key="flex", enable_events=True, visible=True)]]

    layout = [[sg.Frame('Input start and end date (yyyy-mm-dd)', layout=date_layout)],
              [sg.Text("")],
              [sg.Frame('Input your classes to add them to Google Calendar.', layout=frame_layout)],
              [sg.Frame('Select event color', layout=[[sg.Listbox(colorList, size=(35, 11), key="colorListBox",
                                                                  default_values=["Lavender"])]])],
              [sg.Button("SUBMIT", key="submit"), sg.Button("EXIT", key="exit", visible=True)]]
    window = sg.Window(title="LCS Scheduling Tool", layout=layout, default_element_size=(15, 1), margins=(500, 200))

    toggle = False
    while True:
        event, values = window.read()
        if event == "flex":
            toggle = not toggle
            window["pdFlex"].update(visible=toggle)
        elif event == sg.WIN_CLOSED or event == "exit":
            window.close()
            return 1
        elif event == "submit":
            error = []
            start_dt = str(values["startDate"])
            end_dt = str(values["endDate"])
            if start_dt < "2020-08-18":
                error.append('Start date must be after 2020-08-18')
            if end_dt > "2021-05-29":
                error.append('End date must be before 2021-05-28')
            if start_dt > end_dt:
                error.append('Start date must be after end date')
            if not toggle:
                pdFlex = str("Flex Period")
            if toggle:
                classes.append(str(values["pdFlex"]))
            classes.append(str(values["pdOne"]))
            classes.append(str(values["pdTwo"]))
            classes.append(str(values["pdThree"]))
            classes.append(str(values["pdFour"]))
            classes.append(str(values["pdFive"]))
            classes.append(str(values["pdSix"]))
            for x in classes:
                if not x and not x.strip():
                    error.append('You must enter a class for all periods')
            for x in range(len(colorList)):
                if colorList[x] == values["colorListBox"]:
                    color = x + 1
            if error:
                return error
            if not error:
                window.close()
                return 0


def main():
    while True:
        start_dt = "2020-08-18"
        end_dt = "2021-05-28"
        classes = []
        color = 0
        output = userInput(classes)
        if output == 0:
            api(start_dt, end_dt, classes, color)
            break
        elif output == 1:
            break
        else:
            output2 = errorPage(output)
            if output2 == 1:
                break


if __name__ == '__main__':
    main()
#
# # https://console.cloud.google.com/apis/credentials?project=recent-videos-000
# # https://developers.google.com/calendar/create-events
#
# # https://stackoverflow.com/questions/54517136/i-want-to-get-all-dates-exclude-weekends-between-two-dates-in-python
# # https://careerkarma.com/blog/python-convert-list-to-dictionary/
