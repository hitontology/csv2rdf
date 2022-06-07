from urllib import request
import subprocess

RESET = "\033[1;0m"
GREEN = "\033[1;32m"
sheets = {
    "Link/link.csv": {"key": "1MVlpWhI809C1Ifxe34eNayf1Em36cqnpzJxYZNMGaL4", "gid": 0},
    "Mb/applicationsystemtype.csv": {"key": "1t81QjGkrcesMJYXedmJo0Z6dUQhzzFXw_YEkkteAT6c", "gid": 1532284086},
    "JoshiPacs/feature.csv": {"key": "1YiEwhQUXmlT0iK8sc2HH4sE4_WkiGyEEUXVOvWBjfhE", "gid": 256105438},
    "WhoDhiSystemCategory/applicationsystemtype.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 1235425432},
    "WhoDhiClient/feature.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 73177652},
    "WhoDhiHealthcareProvider/function.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 0},
    "WhoDhiHealthcareProvider/feature.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 54553433},
    "WhoDhiHealthSystemManager/function.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 405952217},
    "WhoDhiHealthSystemManager/feature.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 754899153},
    "WhoDhiDataService/feature.csv": {"key": "1F0Rg1bbqYiZZEXL3DnyDjEZo-eexr7_HJk4eqtyx42Y", "gid": 799700984},
    "EhrSfm/feature.csv": {"key": "1Hghh5Nhn6LkS5ubz2Xq1l00NjvGbMEhEu-xtB85RX_8", "gid": 0},
    "Bb/applicationsystemtype.csv": {"key": "1o8WiAWB3AKDr9BHjF1W07JRbzDtQ-fmPT4IfCToL3RE", "gid": 1532284086},
    "Bb/function.csv": {"key": "1o8WiAWB3AKDr9BHjF1W07JRbzDtQ-fmPT4IfCToL3RE", "gid": 1259391562},
    "Bb/feature.csv": {"key": "1o8WiAWB3AKDr9BHjF1W07JRbzDtQ-fmPT4IfCToL3RE", "gid": 1234838117},
}

def csvUrl(key,sheet):
    return "https://docs.google.com/spreadsheets/d/" + key + "/export?format=csv&gid=" + str(sheet)


for file in sheets:
    s = sheets[file]
    url = csvUrl(s["key"],s["gid"])
    print("Downloading", GREEN, file, RESET, "from", GREEN, url, RESET + "...")
    request.urlretrieve(url, file)

print(GREEN,"Downloads finished",RESET)

# end of line conversion from CRLF to LF (\n) to match repository and not cause unnecessary diffs
try:
    subprocess.run("dos2unix */*.csv", shell=True)
except FileNotFoundError:
    print("dos2unix command not found. Skipping end of line conversion.")

try:
    subprocess.run(["git", "status"])
except FileNotFoundError:
    pass
