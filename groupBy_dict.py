import json
data = [
    {"S":1, "date":"01/01/23"},
    {"F":1, "date":"01/01/23"},
    {"F":3, "date":"01/02/23"},
    {"PNP":3, "date":"01/02/23"},
    {"S":5, "date":"01/03/23"},
    {"PNP":5, "date":"01/03/23"},
    {"PNP":2, "date":"01/04/23"},
]

def group_by(data_list):

    result = []
    temp = {}
    jdx = 0 

    for record in data_list:

        s = record.get("S") if "S" in record else 0
        f = record.get("F") if "F" in record else 0
        pnp = record.get('PNP') if "PNP" in record else 0 

        if record.get('date') not in temp:
            # add record to result
            result.append({
                "date": record.get("date"),
                "S": s,
                "F": f,
                "PNP": pnp
            })
            # add record to temp
            temp.update({
                record.get('date'): jdx
            })
            jdx += 1
            continue

        if record.get('date') in temp:
            # update existing record in result
            r_idx = temp.get(record.get('date'))
            result[r_idx]['S'] +=  s 
            result[r_idx]['F'] += f 
            result[r_idx]['PNP'] += pnp

    return result


print(json.dumps(group_by(data),indent=2))
