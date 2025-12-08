import fs from "fs"


function partOne(file, cons) {
    const nums = fs.readFileSync(file, "utf-8").trim().split("\n").map(line => line.split(",").map(Number))

    let dists = []
    nums.forEach((a, i) => {
        nums.slice(i + 1).forEach((b, j) => {
            let dist = a.reduce((sum, val, idx) => sum + Math.abs(val - b[idx])**2, 0)
            dists.push([dist, i, i+1+j])
    })})
    dists.sort((a, b) => a[0] - b[0])

    let groups = []
    dists.slice(0, cons).forEach(([_, i, j]) => {
        let gi = groups.find(g => g.has(i))
        let gj = groups.find(g => g.has(j))
        if (gi && gj) {
            if (gi === gj) return
            gi.forEach(v => gj.add(v))
            groups.splice(groups.indexOf(gi), 1)
        } else if (gi) {
            gi.add(j)
        } else if (gj) {
            gj.add(i)
        } else {
            groups.push(new Set([i, j]))
        }
    })

    groups.sort((a, b) => b.size - a.size)
    let res = groups.slice(0,3).reduce((prod, g) => prod * g.size, 1)
    console.log(res)
}

function partTwo(file) {
    const nums = fs.readFileSync(file, "utf-8").trim().split("\n").map(line => line.split(",").map(Number))

    let dists = []
    nums.forEach((a, i) => {
        nums.slice(i + 1).forEach((b, j) => {
            let dist = a.reduce((sum, val, idx) => sum + Math.abs(val - b[idx])**2, 0)
            dists.push([dist, i, i + 1 + j])
    })})
    dists.sort((a, b) => a[0] - b[0])

    let groups = []
    let res = dists.find(([_, i, j]) => {
        let gi = groups.find(g => g.has(i))
        let gj = groups.find(g => g.has(j))
        if (gi && gj) {
            if (gi === gj) return
            gi.forEach(v => gj.add(v))
            groups.splice(groups.indexOf(gi), 1)
        } else if (gi) {
            gi.add(j)
        } else if (gj) {
            gj.add(i)
        } else {
            groups.push(new Set([i, j]))
        }
        if (groups[0].size === nums.length) return true
    })
    console.log(nums[res[1]][0] * nums[res[2]][0])
}

partOne("./example.txt", 10)
partOne("./input.txt", 1000)

partTwo("./example.txt")
partTwo("./input.txt")