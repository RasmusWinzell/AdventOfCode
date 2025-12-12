import fs from "fs"


function partOne(file) {
    const chunks = fs.readFileSync(file, "utf-8").trim().split("\n")
    const shapeSize = 7

    let canFit = 0
    chunks.filter(l => l.length > 3).forEach(line => {
        let [width, height, ...numberOfShapes] = line.match(/\d+/g).map(Number)
        let sum = numberOfShapes.reduce((a, b) => a + b, 0)
        let spaceLeft = width * height - sum * shapeSize
        if (spaceLeft > 0) {
            canFit++
        }
    })
    console.log(canFit)
}

partOne("./input.txt")