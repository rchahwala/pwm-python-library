import json

data = [
    {"S":1, "date":"01/01/23"},
    {"F":1, "date":"01/01/23"},
    {"F":3, "date":"01/02/23"},
    {"S":5, "date":"01/03/23"},
    {"PNP":5, "date":"01/03/23"},
    {"S":5, "date":"01/03/23"},
]


class FormatData:
    def __init__(self, data):
        self.data = data
        self.result = []
        self.unique_category = []

    def get_result_length(self):
        return len(self.result)

    def get_result(self):
        if len(self.data) == 0:
            return "Empty list"
        return self.result

    def process_data(self):

        # loop through data
        for idx, record in enumerate(self.data):
            # check if result dic is empty
            if self.get_result_length() == 0:
                self.result.append({
                    "date": str(record["date"]),
                    "S": int(record["S"]) if "S" in record else 0,
                    "PNP": int(record["PNP"]) if "PNP" in record else 0,
                    'F': int(record["F"]) if "F" in record else 0,
                    "id": idx + 1
                })
                # add unique date in temp
                self.unique_category.append(
                    str(record["date"])
                )
                continue

            # check if result set is not empty
            if self.get_result_length() > 0:

                # check if date is already present in the temp variable
                if str(record["date"]) in self.unique_category:

                    # get index from result
                    dt_idx = self.unique_category.index(str(record["date"]))
                    self.result[dt_idx]["S"] = self.result[dt_idx]["S"] + int((record["S"]) if "S" in record else 0)
                    self.result[dt_idx]["PNP"] = self.result[dt_idx]["PNP"] + int((record["PNP"]) if "PNP" in record else 0)
                    self.result[dt_idx]["F"] = self.result[dt_idx]["F"] + int((record["F"]) if "F" in record else 0)
                    continue

                else:

                    self.result.append( {
                        "date": str(record["date"]),
                        "S": int(record["S"]) if "S" in record else 0,
                        "PNP": int(record["PNP"]) if "PNP" in record else 0,
                        'F': int(record["F"]) if "F" in record else 0,
                        "id": ++idx
                    })

                # add unique date in temp
                self.unique_category.append(
                    str(record["date"])
                )


result = FormatData(data)
result.process_data()
# print(json.dumps(len(result.data),indent=2))



# print(json.dumps(result.unique_category,indent=2))
print(json.dumps(result.get_result(),indent=2))
# p = process_data(data)
# print(result.result)
# print(json.dumps(p,indent=2))
