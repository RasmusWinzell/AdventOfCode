import fs from "fs"


function partOne(file) {
    const ranges = fs.readFileSync(file, "utf8").trim().split(",")
    let total = 0
    ranges.forEach((rng) => {
        let [rstart, rend] = rng.split("-")

        if (rstart.length % 2) rstart = String(10**(rstart.length))
        if (rend.length % 2) rend = String(10**(rend.length-1)-1)

        let rs1 = Number(rstart.slice(0, rstart.length/2))
        let rs2 = Number(rstart.slice(rstart.length/2))
        let rs = rs2 > rs1 ? rs1+1 : rs1

        let re1 = Number(rend.slice(0, rend.length/2))
        let re2 = Number(rend.slice(rend.length/2))
        let re = re2 < re1 ? re1-1 : re1

        Array(re-rs+1).keys().forEach((i) => total += Number(String(i + rs).repeat(2)))
    })
    console.log(total)
}

function partTwo(file) {
    const ranges = fs.readFileSync(file, "utf8").trim().split(",")
    let total = 0
    ranges.forEach((rng) => {
        let [r1, r2] = rng.split("-")
        let invalids = new Set()
        for (let div = 2; div <= r2.length; div++) {
            let rs = r1.length % div ? "" + (10**(Math.ceil(r1.length/div)*div-1)) : r1
            let re = r2.length % div ? "" + (10**(Math.floor(r2.length/div)*div)-1) : r2

            let rsm = rs.match(new RegExp(`.{1,${rs.length/div}}`, "g")).map((s) => +s)
            let rsv = rsm.reverse().reduce((a, b) => a > b ? b+1 : b)

            let rem = re.match(new RegExp(`.{1,${re.length/div}}`, "g")).map((s) => +s)
            let rev = rem.reverse().reduce((a, b) => a < b ? b-1 : b)

            Array(rev-rsv+1).keys().forEach((i) => invalids.add(("" + (i + rsv)).repeat(div)))
        }

        invalids.forEach((i) => total += +i)
    })
    console.log(total)
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example.txt")
partTwo("./input.txt")