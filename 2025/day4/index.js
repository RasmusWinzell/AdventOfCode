import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let accessable = 0
    for (let y = 0; y < lines.length; y++) {
        for (let x = 0; x < lines[y].length; x++) {
            if (lines[y][x] === "@") {
                let neightbors = 0
                for (let dy = -1; dy <= 1; dy++) {
                    for (let dx = -1; dx <= 1; dx++) {
                        if (lines[y + dy] && lines[y + dy][x + dx] === "@") {
                            neightbors++
                        }
                    }
                }
                if (neightbors < 5) {
                    accessable++
                }
            }
        }
    }
    console.log(accessable)
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf8").trim().split("\n")
    let totalAccessable = 0
    let accessable = 0
    do {
        accessable = 0
        for (let y = 0; y < lines.length; y++) {
            for (let x = 0; x < lines[y].length; x++) {
                if (lines[y][x] === "@") {
                    let neightbors = 0
                    for (let dy = -1; dy <= 1; dy++) {
                        for (let dx = -1; dx <= 1; dx++) {
                            if (lines[y + dy] && lines[y + dy][x + dx] === "@") {
                                neightbors++
                            }
                        }
                    }
                    if (neightbors < 5) {
                        accessable++
                        lines[y] = lines[y].substring(0, x) + "x" + lines[y].substring(x + 1)
                    }
                }
            }
        }
        totalAccessable += accessable
    } while (accessable > 0)
    console.log(lines.join("\n"))
    console.log(totalAccessable)
}


partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")