import fs from "fs"


function partOne(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n").map(line => line.split(""))
    let S = lines[0].indexOf("S")
    lines[0][S] = "|"
    let splits = 0
    lines.forEach((line, r) => {
        line.forEach((char, c) => {
            if (char === "+") {
                lines[r][c-1] = "|"
                lines[r][c+1] = "|"
            }
        })
        if (r === lines.length - 1) return
        line.forEach((char, c) => {
            if (char === "|") {
                if (lines[r+1][c] === "^") {
                    lines[r+1][c] = "+"
                    splits++
                } else if(lines[r+1][c] === ".") {
                    lines[r+1][c] = "|"
                }
            }
        })
    })
    console.log(splits)
}


function partTwo(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n")
    let cache = {}
    let f = (r,i) => cache[[r,i]] || (cache[[r,i]] = r === lines.length || ((lines[r][i] === "^") ? f(r+1,i-1) + f(r+1,i+1) : f(r+1,i)))
    console.log(f(0, lines[0].indexOf("S")))
}


partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")