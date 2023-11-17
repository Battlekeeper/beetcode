<script setup lang="ts">
import VueMarkdown from 'vue-markdown-render'
import navbar from '~/components/navbar.vue';
import { Codemirror } from 'vue-codemirror'
import { javascript } from '@codemirror/lang-javascript'
import { python } from '@codemirror/lang-python'
import { oneDark } from '@codemirror/theme-one-dark'

const view = shallowRef()
const handleReady = (payload: any) => {
    view.value = payload.view
}

var config = useRuntimeConfig()
var route = useRoute()

var fetch = await useFetch("/api/challenge/" + route.query.id, { baseURL: config.public.apiBaseUrl })
var challenge = fetch.data.value as any


const code = ref(challenge.code[Object.keys(challenge.code)[0]].setup)

var lang = javascript()
if (Object.keys(challenge.code)[0] == "python") {
    lang = python()
}
const selectedLang = ref(Object.keys(challenge.code)[0])
const extensions = ref<any>([lang, oneDark])
const showOutput = ref(false)
const codeOutput = ref("")
const runMsg = ref("Run Code")

function changeLang(event: any) {
    selectedLang.value = event.target.value
    if (event.target.value == "python") {
        extensions.value = [python(), oneDark]
    } else {
        extensions.value = [javascript(), oneDark]
    }
    code.value = challenge.code[selectedLang.value].setup
}

async function runCode() {
    runMsg.value = "Running..."

    showOutput.value = true
    var data = {}
    //@ts-ignore
    data.lang = selectedLang.value
    //@ts-ignore
    data.code = code.value

    var fetch = await useFetch("/api/runcode/" + route.query.id, { baseURL: config.public.apiBaseUrl, method: "POST", body: data })
    codeOutput.value = parseResultToHTML(fetch.data.value as any)
    runMsg.value = "Run Code"

}

function parseResultToHTML(result: string): string {
    const lines: string[] = result.split("\n");

    if (result.startsWith("<SYSTEM::>")) {
        return result.replace("<SYSTEM::>", "");
    }

    const parsedOutput: string[] = [];
    for (const line of lines) {
        if (line === "") {
            continue;
        }
        const [prefix, content] = line.split("::>");
        if (prefix === "<DESCRIBE") {
            parsedOutput.push(`<p>${content.trim()}</p>`);
        } else if (prefix === "<IT") {
            const currentTest = content.trim();
            parsedOutput.push(`<p style="margin-left: 20px;">${currentTest}</p>`);
        } else if (prefix === "<FAILED") {
            parsedOutput.push(
                `<p style="margin-left: 40px; color: red; font-weight: bold;">Failed:</p>` +
                `<p style="margin-left: 60px;">${content.trim()}</p>`
            );
        } else if (prefix === "<PASSED") {
            parsedOutput.push(
                `<p style="margin-left: 40px; color: green; font-weight: bold;">Passed:</p>` +
                `<p style="margin-left: 60px;">${content.trim()}</p>`
            );
        }
    }

    lines.reverse();
    let completedIn: number = 0.0;
    for (const line of lines) {
        if (line.startsWith("<COMPLETEDIN::>")) {
            completedIn = parseFloat(line.replace("<COMPLETEDIN::>", ""));
            break;
        }
    }

    return (
        `<div>${parsedOutput.join("\n")}</div>` +
        `<p style="margin-top: 10px;">Completed in: ${completedIn} seconds</p>`
    );
}

</script>

<template>
    <div class="flex w-full h-full flex-col" style="height: 100vh">
        <navbar></navbar>
        <div class="flex w-full h-full pt-10 pb-12 overflow-y-hidden px-12">
            <div class="flex flex-col w-1/2 h-full card-color rounded-md">
                <div class="flex flex-row mb-1 border-b-2 border-gray-500">
                    <button class="px-3 py-2 rounded-t-md text-white font-bold" :class="{ 'bg-gray-500': !showOutput }"
                        @click="showOutput = false">Instructions</button>
                    <button class="px-3 py-2 rounded-t-md text-white font-bold" :class="{ 'bg-gray-500': showOutput }"
                        @click="showOutput = true">Output</button>
                </div>
                <div class="overflow-y-scroll overflow-x-hidden">
                    <vue-markdown v-show="!showOutput" :source="challenge.description" :breaks="true"></vue-markdown>
                    <div v-show="showOutput" v-html="codeOutput">
                    </div>
                </div>
            </div>
            <div class="flex w-1/2 px-10">
                <div class="flex flex-col items-end card-color rounded-md h-full w-full p-5 gap-1">
                    <div class="flex flex-row justify-between w-full">
                        <div>
                            <button class="bg-gray-500 px-3 py-1 rounded-md text-white font-bold"
                                style="background-color: #2d7567;" @click="runCode()" :disabled="runMsg == 'Running...'">{{
                                    runMsg }}</button>
                        </div>
                        <select class="w-fit" @change="changeLang($event)">
                            <option v-for="lang in Object.keys(challenge.code)" :value="lang">{{ lang }}</option>
                        </select>
                    </div>
                    <codemirror v-model="code" placeholder="Write your code here" :style="{ height: '100%', width: '100%' }"
                        :autofocus="true" :indent-with-tab="true" :tab-size="4" :extensions="extensions"
                        @ready="handleReady" />
                </div>
            </div>
        </div>
    </div>
</template>

<style>
p {
    white-space: normal;
}

h1 {
    font-size: 2em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h2 {
    font-size: 1.5em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h3 {
    font-size: 1.17em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h4 {
    font-size: 1em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h5 {
    font-size: .83em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h6 {
    font-size: .67;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}



blockquote {
    border-left: 8px solid #fafafa;
    padding: 1rem;
}

pre,
code {
    background-color: #fafafa;
    color: black;
}

ul {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    padding-inline-start: 40px;
    list-styletype: disc;
    margin-inline-start: 0;
    margin-inline-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    counter-reset: list-item;
    list-style-image: none;
    list-style-position: outside;
    margin: 1em 0;
    padding: 0 0 0 30pt;
    color: white;
}

ol {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    padding-inline-start: 40px;
    list-styletype: decimal;
    margin-inline-start: 0;
    margin-inline-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    counter-reset: list-item;
    list-style-image: none;
    list-style-position: outside;
    margin: 1em 0;
    padding: 0 0 0 30pt;
}

li {
    display: list-item;
    text-align: match-parent;
    text-align: match-parent;
    text-align: match-parent;
    color: white;
}
</style>