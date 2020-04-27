var deepEqual = function (a, b) {
    if (a === b) {
      return true;
    }
    if (a == null || typeof a != "object" ||b == null || typeof b != "object") {
      if (Object.keys(a).length != Object.keys(b).length)
        return false;
  
      for (var item in a) {
        if (b.hasOwnProperty(item))
        {  
          if (!deepEqual(a[item], b[item]))
            return false;
        }
        return false;
      }
      return true;
    }
    return false;
  }
  
  console.log(deepEqual({key: "priya", value: 10}, {key:"an", value: 10}));