import fs from "fs"

function partOne(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n")
    let connections = lines.map(line => line.match(/\w+/g)).reduce((c, [input, ...outputs]) => ({...c, [input]: outputs}), {})
    let f = (node) => node === "out" ? 1 : (connections[node] || []).reduce((sum, neighbor) => sum + f(neighbor), 0)
    console.log(f("you"))
}

function partTwo(file) {
    const lines = fs.readFileSync(file, "utf-8").trim().split("\n")
    let connections = lines.map(line => line.match(/\w+/g)).reduce((c, [input, ...outputs]) => ({...c, [input]: outputs}), {})
    let cache = {}
    let f = (n, g) => [n,g] in cache ? cache[[n,g]] : cache[[n,g]] = n === g ? 1 : (connections[n] || []).reduce((s, m) => s + f(m, g), 0)
    console.log((f("svr", "dac") * f("dac", "fft") * f("fft", "out")) + (f("svr", "fft") * f("fft", "dac") * f("dac", "out")))
}

partOne("./example.txt")
partOne("./input.txt")

partTwo("./example2.txt")
partTwo("./input.txt")