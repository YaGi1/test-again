import requests
import json

if __name__ == '__main__':
    parameters = {
        "lat": 20.71,
        "lon": -74
    }
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    # print(response.status_code)
    print(response.json())


    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    pass_times = response.json()['response']
    jprint(pass_times)
    # jprint(response.json())
    risetimes = []

    for d in pass_times:
        time = d['risetime']
        risetimes.append(time)

    print(risetimes)

    times = []
    from datetime import datetime

    for rt in risetimes:
        time = datetime.fromtimestamp(rt)
        times.append(time)
        print(time)


