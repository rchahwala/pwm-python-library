const  data = [
  {name: "Rahul", surname: "Chahwala"},
  {name: "Rhythm", surname: "Chahwala"},
  {name: "Riaan", surname: "Chahwala"},
  {name: "Kruti", surname: "Rana"},
  {name: "testName1", surname: "test"},
  {name: "Rhythm", surname: "Rana"},
  {name: "Riaan", surname: "Chahwala"},
  {name: "testName", surname: "test"},
]

const output = [
  {Chahwala: ["Rahul", "Riaan", "Rhythm"]},
  {Rana: ["Kruti"]}
]

const process = (list) => {

    const result = []
    const temp = {}
    let idx = 0

    for(const item of list) {
      if (result.length === 0) {
        result.push({
          [item.surname]: [item.name]
        })
        temp[item.surname] = idx
        continue
      }

      if (result.length > 0) {
        // check if surname is present in temp
        if(temp[item.surname] >= 0) {
          result[temp[item.surname]][item.surname].push(item.name)
          continue
        }
        else {
          result.push({
            [item.surname]: [item.name]
          })
          temp[item.surname] = ++idx;
        }
      }
    } // for end
    return result
}

const a = process(data);
console.log(a)
