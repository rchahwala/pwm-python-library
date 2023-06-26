const  data = [
  {name: "Rahul", surname: "Chahwala"},
  {name: "testName3", surname: "test"},
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

const groupBy = (list) => {

    const result = []
    const temp = {}
    let idx = 0

    for(const item of list) {
      // check if surname is present in temp
      if(temp[item.surname] >= 0) {
        result[temp[item.surname]][item.surname].push(item.name)
        continue
      }

      if(!temp[item.surname]) { 
        result.push({
          [item.surname]: [item.name]
        })
        temp[item.surname] = idx++;
      }
    } // for end
    return result
}

const a = groupBy(data);
console.log(JSON.stringify(a,undefined,3))
