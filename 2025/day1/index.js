import fs from "fs"



function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let pointTo = 50
    let zeroCounts = 0
    lines.forEach((line) => {
        let dir = line.at(0) === "R" ? 1 : -1
        let num = Number(line.slice(1))
        pointTo += dir * num
        pointTo = (pointTo + 100) % 100        
        if (!pointTo) zeroCounts++
    })

    console.log({pointTo, zeroCounts})

}
// 0 448 0
// 0 348 1
// 0 248 2
// 0 148 3
// 0 48 4
function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let pointTo = 50
    let zeroCounts = 0
    lines.forEach((line) => {
        let dir = line.at(0) === "R" ? 1 : -1
        let diff = Number(line.slice(1))
        let newZeros = Math.floor(diff / 100)
        let oldPointTo = pointTo
        pointTo = (pointTo + dir * diff%100 + 100) % 100
        if (oldPointTo && pointTo) newZeros += Math.sign(pointTo-oldPointTo) !== dir
        if (!pointTo) newZeros++
        console.log({line, oldPointTo, pointTo, newZeros})
        zeroCounts += newZeros
    })

    console.log({pointTo, zeroCounts})

}


// partOne("./example.txt")
// partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")