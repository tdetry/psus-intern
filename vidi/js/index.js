// @ts-check

const { marked } = require('marked')
const yargs = require('yargs')
const fs = require('fs/promises')
const { stdin, stdout } = require('process')
const readline = require('node:readline')
const util = require('util')

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
        this.writeOutput = util.promisify(this.output.write)
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
            await this.process(this.input.read())
        }
    }

    async process(line) {
        line = marked(line)
        // TODO: Make this work
        await this.writeOutput(line)
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