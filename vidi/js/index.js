// @ts-check

const { marked } = require('marked')
const yargs = require('yargs')
const fs = require('fs/promises')
const { stdin, stdout } = require('process')
const readline = require('node:readline')

async function main() {
    const args = await parseArgs()
    const isStdin = !args.in
    const input = args.in
        ? (await fs.open(args.in, 'r')).createReadStream({ encoding: 'utf-8' })
        : stdin
    const output = args.out
        ? (await fs.open(args.out, 'w')).createWriteStream({ encoding: 'utf-8' })
        : stdout
    const conv = new Converter(input, output, isStdin)
    await conv.run()
    await conv.close()
}

class Converter {
    /**
     * @param {NodeJS.ReadableStream} input 
     * @param {NodeJS.WritableStream} output 
     * @param {boolean} isStdin 
     */
    constructor(input, output, isStdin) {
        this.input = input
        this.output = output
        this.isStdin = isStdin
    }

    async run() {
        if (this.isStdin) {
            const rl = readline.createInterface({
                input: this.input
            })
            rl.prompt()
            rl.on('line', async line => {
                await this.process(line)
            })
        } else {
            this.input.read()
            // Don't ask, this is the way of Node.JS...
            this.input.on('data', data => {
                this.process(data)
            })
        }
    }

    async process(line) {
        line = marked(line)
        // Hack: util.promisify doesn't work, so this will have to do...
        return await new Promise((resolve, reject) => 
            resolve(this.output.write(line, err => err && reject(err))))
    }

    async close() {

    }
}

function parseArgs() {
    return yargs
        .option('out', {
            alias: 'o',
            type: 'string',
            desc: 'defaults to stdout'
        })
        .option('in', {
            alias: 'i',
            type: 'string',
            desc: 'defaults to stdin'
        })
        .help()
        .alias('help', 'h')
        .argv
}

main()