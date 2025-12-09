import fs from "fs"


function partOne(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n")
    let reds = lines.map(l => l.split(",").map(Number)).map(([x,y]) => ({x, y}))
    let pairs = reds.flatMap((a, i) => reds.slice(i+1).map(b => [a, b]))
    let maxArea = pairs.reduce((m, [a, b]) => Math.max(m, (Math.abs(a.x - b.x)+1) * (Math.abs(a.y - b.y)+1)), 0)
    console.log(maxArea)
}


// Should not work for all inputs... but worked for mine and the example
function partTwo(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n")

    let reds = lines.map(l => l.split(",").map(Number)).map(([x,y]) => ({x, y}))

    function checkIntersect(a, b, c, d) {
        // check if segments ab and cd intersect
        let ab1 = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        let ab2 = (b.x - a.x) * (d.y - a.y) - (b.y - a.y) * (d.x - a.x)
        let cd1 = (d.x - c.x) * (a.y - c.y) - (d.y - c.y) * (a.x - c.x)
        let cd2 = (d.x - c.x) * (b.y - c.y) - (d.y - c.y) * (b.x - c.x)

        return ab1 * ab2 < 0 && cd1 * cd2 < 0
    }

    let edges = reds.map((p1, i) => [p1, reds[(i + 1) % reds.length]])

    let maxArea = 0
    reds.forEach((a, i) => {
        reds.slice(i+1).forEach((b, j) => {
            let area = (Math.abs(a.x - b.x)+1) * (Math.abs(a.y - b.y)+1)

            if (area < maxArea) return

            let intersects = edges.some(([c, d]) => {
                return checkIntersect(a, {x: b.x, y: a.y}, c, d) ||
                        checkIntersect({x: b.x, y: a.y}, b, c, d) ||
                        checkIntersect(b, {x: a.x, y: b.y}, c, d) ||
                        checkIntersect({x: a.x, y: b.y}, a, c, d) ||
                        checkIntersect(a, b, c, d) ||
                        checkIntersect({x: b.x, y: a.y}, {x: a.x, y: b.y}, c, d)
            })
            if (!intersects) {
                maxArea = area
            }
        })
    })
    console.log(maxArea)
}


partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")