import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")

    let total = 0
    lines.forEach((line) => {

        let res = line.split("").reduce((m, v1, i, arr) => {
            if (i == arr.length-1) return m
            let v2 = arr.slice(i+1).reduce((a, b) => b > a ? b : a)
            let tot = +(v1 + v2)
            return tot > m ? tot : m
        }, 0)
        console.log({line, res})
        total += res
    })
    console.log(total)
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let total = 0
    lines.map((l) => l.split("")).forEach((line) => {
        let res = ""
        let o1 = 0
        for (let o2 = -11; o2 < 1; o2++) {
            let sl = line.slice(o1, line.length+o2)
            let v = sl.reduce((im, v, i, arr) => v > arr[im] ? i : im, 0)
            res += ""+sl[v]
            // console.log({o: o2, line, sl, v, res})
            o1 += v+1
        }
        // console.log(res)
        total += +res
        // assert(0)
    })
    console.log(total)
}

// partOne("./example.txt")
// partOne("./input.txt")

// partTwo("./example.txt")
partTwo("./input.txt")