function covid19(arr){
    let list = [[0], [], [], [], []];
    let checked = [0];
    for (let meeting of arr) {
      for (let j = 0; j < list.length - 1; j++) {
        for (let member of meeting) {
          if (list[j].indexOf(member) != -1) {
            for (let suspect of meeting) {
              if (checked.indexOf(suspect) == -1) {
                list[j + 1].push(suspect);
                checked.push(suspect);
              }
            }
            break;
          }
        }
      }
    }
    return [list[1].length, list[2].length, list[3].length, list[4].length];
  }