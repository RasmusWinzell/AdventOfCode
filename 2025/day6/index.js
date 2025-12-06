import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let rows = lines.map(l => l.match(/\S+/g))
    let nums = rows.slice(0, -1).map(r => r.map(Number))
    let ops = rows[rows.length - 1]
    console.log(rows.slice(0, -1))
    console.log(ops)
    let total = 0
    for (let i = 0; i < ops.length; i++) {
        let op = ops[i]
        let t = 0
        let arr = nums.map(n => n[i])
        if (op === "+") {
            t = arr.reduce((s,n) => s + n, 0)
        } else if (op === "*") {
            t = arr.reduce((s,n) => s * n, 1)
            console.log("MULT")
        }
        console.log({op, arr, t})
        total += t
    }
    console.log(total)
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").split("\n")
    let op = null
    let partTotal = 0
    let total = 0
    for (let col = 0; col < lines[0].length; col++) {
        console.log("---------------------")
        let part = ""
        for (let row = lines.length - 1; row >= 0; row--) {
            if (lines[row][col] !== " ") {
                console.log({row, col, char: lines[row][col], part, partTotal, total, op})
                if (row === lines.length - 1) {
                    total += partTotal
                    op = lines[row][col]
                    partTotal = op === "+" ? 0 : 1
                    console.log("NEW OP", {op, total})
                    continue
                }
                console.log("here")
                
                console.log("adding char", lines[row][col])
                part += lines[row][col]
            }
            if (!row && part.length > 0) {
                if (op === "+") {
                    partTotal += Number(part.split("").reverse().join(""))
                } else if (op === "*") {
                    partTotal *= Number(part.split("").reverse().join(""))
                }
                continue
            }

        }
    }
    total += partTotal
    console.log(total)
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")