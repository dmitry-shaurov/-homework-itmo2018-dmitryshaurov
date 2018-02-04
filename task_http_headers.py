import json


def http_headers_to_json(a, b):
    dict = {}
    with open(a, "r") as f:
        for i in range(len(f.readlines())):
            f.seek(0)
            zzz =  f.readlines()[i] # save every string inside "for" cycle
            if "GET" in zzz:
                dict["method"] = zzz.split()[0]
                dict["uri"] = zzz.split()[1]
                dict["protocol"] = zzz.split()[2]
            elif "HTTP" in zzz:
                dict["protocol"] = zzz.split()[0]
                dict["status_code"] = zzz.split()[1]
                if "HTTP/1" in zzz:
                    dict["status_message"] = ' '.join(zzz.split()[2:]) # may consist of 1+ word
            else:
                key = zzz[:zzz.find(":")] # save string before ":"
                value = zzz[zzz.find(":")+2:] # save string after ":"
                dict[key.rstrip()] = value.rstrip()
        with open(b, 'w') as results:
            json.dump(dict, results, indent = 4)
